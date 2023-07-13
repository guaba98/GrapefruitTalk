import sqlite3
import pandas as pd
import datetime
import random

#이메일 전송을 위한 SMTP프로토콜 접근 지원을 위한 라이브러리
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 이메일의 유효성점검을 위한 정규 표현식 지원 라이브러리
import re




# class Membership():
# def __init__(self, parent):
#     self.parent = parent
#     # DB 연결 및 데이터 리스트업
#     self.conn = sqlite3.connect("../../data/grapefruit_talk.db", check_same_thread=False)
#
#     self.id_list = pd.read_sql("select USER_ID from USER_TABLE").to_list()
#     self.pwd_list = pd.read_sql("select USER_PASSWORD from USER_TABLE").to_list()
#
#     # Gmail sender
#     self.s_email = 'rhrnaka@gmail.com'
#     self.s_pwd = 'jqlhqjmuddnptivj'

#
#     # 메일 수신자
#     self.r_email = r_email
#     self.name = name
#
#     self.varify_num = int
#     self.list_v_num = []
#     self.permission_num = 0

# 아이디 중복 검거 및 아이디 생성 함수
# ㄴ self.create_id : 회원가입 아이디 입력 칸
def check_id_txt():
    user_id = edt_join_id.text()
    print(user_id)
    if user_id in self.id_list:
        check_popup = "사용 중인 아이디입니다."
        return None
    elif user_id not in self.id_list:
        check_popup = "사용할 수 있는 아이디입니다."
        return user_id

# 아이디 최대 16자 조건 확인 함수
# ㄴ self.create_id : 회원가입 아이디 입력 칸
# def check_id_condition(self):
#     if len(self.create_id.text()) >= 16:
#         check_popup = "아이디는 최대 16자까지 입력 가능"
#         return False
#     else:
#         return True
#
# # 비밀번호 영대문자(1), 특수문자(1) 필수포함 및 최대 16자 조건 확인 함수
# def check_pwd_condition(self):
#
#     insert_pwd = self.create_pwd_1.text()
#     num_ = 0
#     upper_ = 0
#     special_ = 0
#     list_special = ['!', '@', '#', '$', '%', '^', '&', '*']
#
#     for word in insert_pwd:
#         if word.isupper():
#             upper_ += 1
#         if word.isdecimal():
#             num_ += 1
#         if word in list_special:
#             special_ += 1
#
#     if upper_ == 0:
#         check_popup = "비밀번호에 최소 영대문자 1글자 이상 포함되어야 합니다."
#         return False
#     elif special_ == 0:
#         check_popup = "비밀번호에 최소 특수문자 1글자 이상 포함되어야 합니다."
#         return False
#     elif len(insert_pwd) >= 17:
#         check_popup = "비밀번호는 최대 16자까지 입력가능합니다."
#         return False
#     elif insert_pwd == '':
#         check_popup = "비밀번호를 입력해주세요"
#         return False
#     else:
#         return True
#
# # 비밀번호_1, 비밀번호_2 일치 확인 함수
# def check_between_pwd(self):
#     insert_pwd_1 = self.create_pwd_1.text()
#     insert_pwd_2 = self.create_pwd_2.text()
#
#     if insert_pwd_1 != insert_pwd_2:
#         check_popup = "비밀번호가 서로 일치하지 않습니다."
#         return False
#     else:
#         return insert_pwd_2
#
# # 닉네임 최대 20자 조건 확인 함수
# # ㄴ 닉네임은 20자 이하로 한글/영문/숫자 조합
# def check_nickname_condition(self):
#     insert_nickname = self.create_nickname.text()
#     if len(insert_nickname) > 20:
#         check_popup = "닉네임은 최대 20자까지 가능합니다."
#         return False
#     else:
#         return True
#
# # 이메일 입력 시 옳은 이메일 형식인지 확인함수 : 이메일은 @gmail로 고정됨
# def check_email_condition(self):
#     reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
#     if bool(re.match(reg, self.r_email)):
#         check_popup = "유효한 이메일 주소 입니다."
#         return True
#     else:
#         check_popup = "유효한 이메일 주소가 아닙니다."
#         return False
#
# # 인증메일 txt값만 리턴하는 함수
# # ㄴ 인증번호를 랜덤으로 생성한다. 이때 이전에 보낸 인증번호와 겹치지 않도록 filtering한다.
# def make_email_content(self):
#     self.varify_num = random.sample(range(0, 10), k=4)
#     self.list_v_num = [str(num) for num in self.varify_num]
#     print(self.list_v_num)
#     for num in self.list_v_num:
#         if num == self.varify_num:
#             continue
#         else:
#             break
#
#     To = f'{self.r_email}'
#     e_content_1 = f"이메일 계정 인증을 위한 인증번호 4자리를 보내드립니다."
#     e_content_2 = f"아래의 인증번호 4자리를 인증번호 칸에 입력하세요."
#     e_content_3 = f"인증번호 : {self.varify_num[0]} {self.varify_num[1]} {self.varify_num[2]} {self.varify_num[3]}"
#     title = "[자몽톡] 회원가입용 이메일 계정을 인증해주세요"
#
#     html = f"""\
#     <!DOCTYPE html>
#      <html lang="en">
#      <head>
#          <meta charset="UTF-8" />
#          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#          <title>{title}</title>
#      </head>
#      <body>
#          <h4>안녕하세요. {self.name}님. </h4>
#          <p style="padding:5px 0 0 0;">{e_content_1} </p>
#          <p style="padding:5px 0 0 0;">{e_content_2} </p>
#          <p style="padding:5px 0 0 0;">{e_content_3} </p>
#      </body>
#      </html>
#      """
#
#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = title
#     msg['From'] = self.s_email
#     msg['To'] = self.r_email
#     html_msg = MIMEText(html, 'html')
#     msg.attach(html_msg)
#
#     return msg
#
# # 입력한 이메일로 인증메일 발송함수
# def send_membership_email(self):
#     # SMTP()서버의 도메인 및 포트를 인자로 접속하여 객체 생성
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     # SSL : SMTP_SSL('smtp.gmail.com', 465)
#
#     # 접속 후 프로토콜에 맞춰 먼저 SMTP서버에 HELLO 메세지를 전송한다.
#     server.ehlo()
#
#     # 서버의 암호화 방식을 설정하는 메소드, TLS, SSL방식이 있다. (TLS : Gmail 권장, SSL보다 향상된 보안)
#     server.starttls()
#
#     # 서버 로그인
#     server.login(self.s_email, self.s_pwd)
#
#     # 이메일 발송
#     try:
#         server.sendmail(self.s_email, self.r_email, self.make_email_content().as_string())
#         email_popup_txt = "가입을 위한 인증번호 이메일이 발송되었습니다."
#         print("이메일 전송 성공")
#     except:
#         print("이메일 전송 실패")
#
#     #작업을 마친 후 SMTP와의 연결을 끊는다.
#     server.quit()
#
# # 발송한 인증번호와 입력한 인증번호의 일치 여부를 확인한다.
# def check_varify_number(self):
#     insert_v_num = self.insert_varify_number.text()
#     if self.v_num == insert_v_num:
#         check_popup = "이메일 인증 완료"
#         return True
#     else:
#         check_popup = "이메일 인증 실패, 확인 후 재입력 해주시기 바랍니다."
#         return False
#
# # 랜덤으로 프로필 사진을 배정하는 함수
# def assign_random_image(self):
#     num = random.randrange(1,5)
#     img = f'./Images/{num}.png'
#     return img
#
# # 회원가입 완료 및 내역을 USER_TABLE에 저장한다.
# # ㄴ self.user_state : 상태메세지 입력 칸
# def welcome_membership(self):
#     user_state_ment = self.user_state.text()
#     welcome_popup = f"{self.name}님 [자몽톡] 가입 완료!"
#     permission_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
#     self.permission_num += 1
#
#     # 아이디
#     if self.check_id_txt() is None:
#         pass
#     elif self.check_id_condition():
#         pass
#     # 패스워드
#     elif not self.check_pwd_condition():
#         pass
#     elif not self.check_between_pwd():
#         pass
#     # 닉네임
#     elif not self.check_nickname_condition():
#         pass
#     # 이메일
#     elif not self.check_email_condition():
#         pass
#     elif not self.check_varify_number():
#         pass
#     else:
#         user_id = self.check_id_txt()
#         user_pwd = self.check_between_pwd()
#         img_path = self.assign_random_image()
#
#     sql = f"INSERT INTO TB_USER (?,?,?,?,?,?,?,?) " \
#           f"VALUES ({self.permission_num},{user_id},{self.name},{self.r_email}," \
#           f"{user_pwd}, {permission_time},{img_path}, {user_state_ment}) FROM TB_USER"
#
#     self.conn.execute(sql)
#     self.conn.commit()


