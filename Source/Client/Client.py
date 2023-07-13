import socket
import pickle

class Client:
    # "10.10.20.117"
    # "121.148.180.97"
    def __init__(self, server_ip="10.10.20.103", server_port=1121):
        self.server_ip = server_ip # ip
        self.server_port = server_port #포트번호
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 생성

    # 소켓 닫기
    def disconnect(self):
        """소켓 연결을 닫습니다(클라이언트)"""
        self.sock.close()

    # 서버 연결
    def connect(self):
        """서버를 연결합니다(클라이언트)"""
        try:
            self.sock.connect((self.server_ip, self.server_port))
            return True
        except socket.error:
            return False

    # 데이터 수신
    def recevie(self):
        """데이터를 수신합니다(클라이언트)"""
        try:
            recevie_bytes = self.sock.recv(4096)
            if not recevie_bytes:
                raise

            data = pickle.loads(recevie_bytes)
            return data
        except socket.error:
            self.disconnect()
            return None

    # 데이터 발송
    def send(self, data):
        """데이터를 발송합니다(클라이언트)"""
        try:
            self.sock.sendall(pickle.dumps(data))
            return True
        except socket.error:
            self.disconnect()
            return False

    # 클라이언트의 어드레스 반환
    def address(self):
        """클라이언트의 주소를 반환합니다(클라이언트)"""
        return self.sock.getsockname()