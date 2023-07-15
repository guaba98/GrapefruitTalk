import sqlite3
from datetime import datetime

# 정규식 표현
import re

import pandas as pd

from Source.Main.DataClass import *

class DBConnector:      # DB를 총괄하는 클래스
    def __init__(self):
        self.conn = sqlite3.connect("../Client/data.db", check_same_thread=False)
        self.user_id = ""

    def set_user_id(self, user_id):
        print("db class set user_id", user_id)
        self.user_id = user_id

    def end_conn(self):  # db 종료
        self.conn.close()

    def commit_db(self):  # db 커밋
        self.conn.commit()

    # 테이블 비우기
    def clear_table(self, col_name):
        self.conn.execute(f"delete from {col_name}")
        self.commit_db()

    # 원하는 테이블의 원하는 정보 가져오기
    def get_table(self, tb_name: str, user_id="", add_where=""):
        sql = f"select * from {tb_name}"

        if user_id:
            sql += f" where USER_ID = '{user_id}'"

        if add_where:
            if user_id:
                sql += " and"
            else:
                sql += " where"

            sql += add_where

        df = pd.read_sql(sql, self.conn)
        return df

    # 원하는 데이터에 정도 일괄 추가
    def insert_data(self, tb_name, data: list):
        size = len(data[0])
        column = ""
        for i in range(size):
            column += "?, "
        column = column[:-2]
        print(column)

        for d in data:
            self.conn.execute(f"insert into {tb_name} values ({column})", d)
        self.commit_db()

    ## CREATE TABLES ======================================================================== ##

    # 테이블 초기 설정
    def init_tables(self):
        # 단체 방 정보추가
        self.conn.execute("insert into CTB_CHATROOM values ('PA_1', '[단체방] 자몽톡 가입자');")

        # 단체방 대화 테이블 생성
        self.conn.executescript("""
            CREATE TABLE "CTB_CONTENT_PA_1" (
                "USER_ID" TEXT,
                "CNT_ID" INTEGER,
                "CNT_CONTENT" TEXT,
                "CNT_SEND_TIME" TEXT,
                PRIMARY KEY ("CNT_ID" AUTOINCREMENT) );
                """)

        # 단체방 관리자 정보 추가
        self.conn.execute("insert into CTB_USER_CHATROOM values ('PA_1', 'admin');")

        self.commit_db()

    ## TB_USER ================================================================================ ##

    # user_id를 기준으로 행 조회
    def find_user_by_id(self, user_id: str):
        row = self.conn.execute("select * from TB_USER where USER_ID = ?", (user_id,)).fetchall()
        id = row[0]
        return id

    # user_id를 기준으로 행 삭제
    def delete_user(self, user_id: str):
        self.conn.execute("delete from TB_USER where USER_ID = ?", (user_id,))
        self.commit_db()


    # 회원 ID, PW 결과값 가져오기
    def login(self, data: ReqLogin) -> PerLogin:
        print("[ login ]")
        """클라이언트 로그인 요청 -> 서버 로그인 허가 """
        result: PerLogin = PerLogin(rescode=2, id=data.id, pw=data.password)
        sql = f"SELECT * FROM TB_USER WHERE USER_ID = '{data.id}' AND USER_PW = '{data.password}'"
        df = pd.read_sql(sql, self.conn)
        row = len(df)
        print("row",row)

        if row in [None, 0]:
            result.rescode = 0
        # 입력한 아이디와 비밀번호, db에서 가진 아이디와 비밀번호
        # elif data.id != row[1] or data.password != row[2]:
        #     result.rescode = 1
        else:
            result.rescode = 2
        return result

    def regist(self, data: ReqMembership) -> PerRegist:
        result: PerRegist = PerRegist(True)
        try:
            sql = f"INSERT INTO CTB_USER (USER_ID, USER_PW, USER_NM, USER_EMAIL, USER_CREATE_DATE, USER_IMG, USER_STATE)" \
                  f"VALUES ('{data.id}','{data.pw}','{data.nm}','{data.email}','{data.c_date}',0, 0)"
            self.conn.execute(sql)

            self.conn.execute(f"insert into CTB_USER_CHATROOM values ('PA_1', '{data.id}');")

            self.conn.commit()
        except:
            self.conn.rollback()
            result.Success = False
        finally:
            self.conn.close()
        return result

    ## TB_friend ================================================================================ ##
    # 친구 목록 정보 테이블 값 입력
    def insert_friend(self, data:ReqSuggetsFriend):
        self.conn.execute("insert into CTB_FRIEND (USER_ID, FRD_ID, FRD_ACCEPT) values (?, ?, ?)", get_data_tuple(data))
        self.commit_db()

    # 친구 목록 가져오기
    def get_all_friend(self, user_id):
        df = pd.read_sql(f"select * from CTB_FRIEND where USER_ID = '{user_id}'", self.conn)
        return df

    # 수락/거절 조건에 따른 친구 조회
    def get_accept_friend(self, user_id, accept=True):
        df = pd.read_sql(f"select * from CTB_FRIEND where USER_ID = '{user_id}' and FRD_ACCEPT = {accept}", self.conn)
        return df

    # 친구 삭제
    def delete_friend(self, user_id, frd_id: str):
        self.conn.execute(f"delete from CTB_FRIEND where USER_ID = {user_id} FRD_ID = {frd_id}")
        self.commit_db()

    ## TB_log ================================================================================ ##
    # LOG 정보 테이블 값 입력
    def insert_log(self, user_id, login_time, logout_time):
        self.conn.execute("insert into TB_LOG (USER_ID, LOGIN_TIME, LOGOUT_TIME) values (?, ?, ?)", (user_id, login_time, logout_time))
        self.commit_db()

    # LOG 테이블 전체 조회
    def find_log(self):
        rows_data = self.conn.execute("select * from TB_LOG").fetchall()
        if len(rows_data) == 0:
            return None

        find_result_list = list()
        for row in rows_data:
            find_result_list.append(row)
        return rows_data

    ## TB_chatroom ================================================================================ ##

    # 채팅방 개설
    def create_chatroom(self, data:JoinChat):
        # data = JoinChat("admin", ["song030s"], "1:1 대화방 입니다.")
        # 인원 확인
        if len(data.member) == 0:
            return False

        # 타입 확인 - OE_ 1:1, OA_ 1:N
        elif len(data.member) == 1:
            _type = "OE_"
        else:
            _type = "OA_"

        # 일련번호 부여
        df = pd.read_sql(f"select MAX(CR_ID) from CTB_CHATROOM where CR_ID like '{_type}%'", self.conn)
        df = df["MAX(CR_ID)"].iloc[0]

        if df is None:
            _num = 1
        else:
            _cr_id = df[3:]
            _cr_id = int(_cr_id)
            _num = _cr_id+1

        _cr_id = f"{_type}{_num}"

        # 채팅방 정보 추가
        self.conn.execute(f"insert into CTB_CHATROOM values (?, ?)", (_cr_id, data.title))

        # 방장 추가
        self.conn.execute(f"insert into CTB_USER_CHATROOM values (?, ?)", (_cr_id, data.user_id))
        # 채팅 맴버 추가
        for member in data.member:
            self.conn.execute(f"insert into CTB_USER_CHATROOM values (?, ?)", (_cr_id, member))

        # 대화 테이블 생성
        self.conn.execute(f""" CREATE TABLE CTB_CONTENT_{_cr_id} (
                    "USER_ID" TEXT,
                    "CNT_ID" INTEGER,
                    "CNT_CONTENT" TEXT,
                    "CNT_SEND_TIME" TEXT,
                    PRIMARY KEY ("CNT_ID" AUTOINCREMENT));""")

        self.conn.commit()

        return df

    ## TB_user_chatroom ================================================================================ ##

    # 방 맴버 정보 조회
    def get_chatroom_title(self, cr_id):
        df = pd.read_sql(f"select CR_NM from TB_USER_CHATROOM where cr_id = '{cr_id}'", self.conn)
        return df["CR_NM"].iloc[0]

    # 유저의 방 정보 조회
    def find_user_chatroom_by_to(self, user_id):
        df = pd.read_sql(f"select * from TB_USER_CHATROOM natural join TB_CHATROOM where USER_ID = {user_id}", self.conn)
        return df

    # 채팅방 나가기
    def delete_chatroom_member(self, cr_id: str, user_id):
        self.conn.execute("delete from TB_USER_CHATROOM where CR_ID = ? and USER_ID", (cr_id,user_id))
        self.commit_db()

    ## TB_content ================================================================================ ##
    # 대화 추가
    def insert_content(self, data:ReqChat):
        print("insert_content")
        self.conn.execute(f"insert into CTB_CONTENT_{data.cr_id} (USER_ID, CNT_CONTENT, CNT_SEND_TIME) "
                          "values (?, ?, ?)",
                          (data.user_id, data.msg, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        self.commit_db()
        print("save complete")

    def get_content(self, cr_id):
        df = pd.read_sql(f"select * from CTB_CONTENT_{cr_id} natural join CTB_USER;", self.conn)
        return df

    ## 오른쪽 리스트 메뉴 출력용 함수 ================================================================================ ##

    def get_list_menu_info(self, t_type, cr_id="PA_1"):
        if t_type == "single":
            sql = "select CR_ID, CR_NM from CTB_CHATROOM NATURAL JOIN CTB_USER_CHATROOM where cr_ID like 'OE%' group by cr_id;"

        elif t_type == "multi":
            sql = "select CR_ID, CR_NM, count(USER_ID) from CTB_CHATROOM NATURAL JOIN CTB_USER_CHATROOM where cr_ID like '_A%' group by cr_id;"

        elif t_type == "member":
            sql = f"select CTB_USER.USER_ID, CTB_USER.USER_NM, CTB_USER.USER_IMG, CTB_USER.USER_STATE FROM CTB_USER_CHATROOM left join CTB_USER on CTB_USER_CHATROOM.USER_ID = CTB_USER.USER_ID WHERE CTB_USER_CHATROOM.CR_ID = '{cr_id}';"

        elif t_type == "friend":
            sql = f"select CTB_FRIEND.FRD_ID, CTB_USER.USER_NM, CTB_USER.USER_IMG, CTB_USER.USER_STATE FROM CTB_FRIEND left join CTB_USER on CTB_FRIEND.FRD_ID = CTB_USER.USER_ID WHERE CTB_FRIEND.USER_ID = '{self.user_id}';"
        else:
            return False

        df = pd.read_sql(sql, self.conn)
        return df


if __name__ == "__main__":
    DBConnector().create_chatroom("")
    pass
