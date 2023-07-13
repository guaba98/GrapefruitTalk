import socket
import pickle

from Source.Main.DBConnetor import DBConnector
from Source.Main.DataClass import *
from threading import Thread


class Server:
    def __init__(self, port=1121, listener=1):
        self.db = DBConnector()

        # 접속한 클라이언트 정보 key :(ip,포트번호), value : [소켓정보, 아이디]
        # {('10.10.20.117', 57817): [<socket.socket fd=384, family=2, type=1, proto=0, laddr=('10.10.20.117', 1234), raddr=('10.10.20.117', 57817)>, '']}
        self.client : dict[tuple, list[socket.socket, str]] = {}

        # 서버 소켓 생성
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', port))  # 서버의 주소, 포트번호 저장
        self.sock.listen(listener)  # 서버 소켓 연결 요청 대시 상태로 설정

        self.count = 0 # 궁금3. 이 변수는 무엇인가요

        print("[ 서버 시작 ]")

    def return_connected_numbers(self):
        """접속된 멤버들의 숫자를 출력합니다."""
        print('접속된 멤버들의 숫자를 출력합니다.')
        print(len(self.client.keys()))
        connected_members_num = Members(len(self.client.keys()))

        return connected_members_num

    # 접속한 클라이언트가 있는지 확인 (있으면 True, 없으면 False)
    def connected(self):
        """접속한 클라이언트가 있는지 확인. 있으면 True, 없으면 False (서버)"""
        if len(self.client):
            return True
        else:
            return False

    # 클라이언트 연결
    def accept(self):
        """클라이언트 연결시 소켓과 어드레스 반환(서버)"""
        sock, addr = self.sock.accept()

        print(f"[{addr} 클라이언트 접속 ]")
        self.client[addr] = [sock, ""]
        # self.return_connected_numbers() # 접속된 멤버들의 숫자 출력
        return sock, addr

    # 클라이언트 연결 종료
    def disconnect(self, addr):
        """접속 종료한 클라이언트의 정보가 존재한다면 삭제(서버)"""
        # 접속 종료한 클라이언트의 정보가 존재한다면
        if addr in self.client:

            # 클라이언트 정보 삭제
            del self.client[addr]

    # 데이터 전송
    def send(self, sock:socket.socket, data):
        """결과값을 가지고 실행하는 부분(서버)""" #6. 보기

        # 데이터 타입에따른 데이터 전송
        if type(data) in [ReqChat]: # 만약 데이터 유형이 채팅이라면 데이터를 전달해 준다.
            self.send_message(data)

        elif type(data) == str: # 8. 일단 임시로 아이디 지정해준 부분을 위해 가생성
            # 궁금3 getpeername()함수는 무엇인가?
            # -> 소켓 지시자 sockfd에 연결한 상대의 주소 정보를 가져온다. 주소 정보는 addr로 너어온다.
            # addrien은 addr구조체의 크기이다. 함수가 반환된 다음에는 가져온 addr 자료구조의 크기 값을 바이트로 돌려준다.
            print('self.client 출력: ',self.client)
            self.client[sock.getpeername()][1] = data
            print('self.client 재출력: ',self.client)
            print(self.client[sock.getpeername()][1])

    # 접속한 모든 클라이언트에게 전송
    # def send_all_client(self, data):
    #     """접속한 모든 클라이언트들에게 정보를 전달한다(서버, 현재 호출부분 없음)"""
    #     if self.connected():
    #         for client in self.client.values():
    #             client[0].sendall(pickle.dumps(data)) #클라이언트 소켓에 정보 전달
    #         return True
    #     else:
    #         return False

    # 발송자를 제외한 나머지 접속자에세 메시지 발송
    def send_message(self, data:ReqChat):
        """접속한 모든 클라이언트에게(발송자 제외) 나머지 접속자에게 메세지를 발송한다(서버)"""
        print(data, '를 보냅니다.')
        if self.connected():
            # {('10.10.20.117', 57817): [<socket.socket fd=384, family=2, type=1, proto=0, laddr=('10.10.20.117', 1234), raddr=('10.10.20.117', 57817)>, '']}
            # 연결된 모든 클라이언트에 데이터 발송 # 7. 접속한사람 and 나 외에 정보 보내는 부분 db에서 받아오기
            print('클라이언트들의 value값을 출력합니다.')
            for client in self.client.values():
                print(data.user_id, client[1])
                if data.user_id != client[1]:
                    client[0].sendall(pickle.dumps(data)) # 피클 모듈을 사용하여 이진 파일로 저장한 데이터를 sendal로 손실없이 정보를 보내준다.
                    client[0].sendall(pickle.dumps(self.return_connected_numbers())) # 몇 명이 참가하고 있는지 보내준다.
                    self.db.insert_content(data)
            print('value값 출력 완료')
            return True
        else:
            return False

    # 데이터 수신
    def recevie(self, sock:socket.socket):
        """데이터를 발송한 클라이언트의 어드레스를 얻는다(서버)"""
        # 데이터를 발송한 클라이언트의 어드레스 얻기
        addr = sock.getpeername()
        print('클라이언트의 어드레스', addr)
        try:
            receive_bytes = sock.recv(4096)

            # 데이터 수신 실패시 오류 발생
            if not receive_bytes:
                raise

            # 수신 받은 데이터 변환 하여 반환
            data = pickle.loads(receive_bytes)
            return data

        except:
            sock.close()
            self.disconnect(addr)
            return None

    # 받은 데이터에 대한 처리 결과 반환 내용 넣기
    # 5. 데이터 분기처리 필요(채팅 부분만 되어있음)
    def process_data(self, sock, data):
        """받은 데이터(dataclass)에 대한 처리 결과 """
        print('client.py에서 받은 데이터 타입:', type(data))
        if type(data) == ReqChat: # 받은 데이터 타입이
            return data
        else:
            return data

    def handler(self, sock,):
        """"""
        while True:
            data = self.recevie(sock) #유저 아이디를 받아옴

            if not data:
                break

            print("[ 데이터 수신 ]")

            # 수신된 데이터에 따른 결과 반환값을 클라이언트로 보내주기
            process_data = self.process_data(sock, data) # 소켓과 아이디를 넣어주고 유형dataclass(채팅, 등등)에 따라 데이터를 반환받아옴

            print("[ 데이터 처리 ]")
            self.send(sock, process_data) # 데이터 보내주기(소켓, 데이터)
            print("처리 완료")


if __name__ == "__main__":
    server = Server()

    while True:
        print("대기중...")

        c_sock, c_addr = server.accept()
        c_thread = Thread(target=server.handler, args=(c_sock,), daemon=True)
        c_thread.start()
