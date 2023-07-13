from PyQt5.QtCore import QThread, pyqtSignal

from Source.Client import Client
from Source.Main.DataClass import *

class ReceiveThread(QThread):
#0. 이 코드들 순서 이해
    # 시그널 선언
    res_message = pyqtSignal(ReqChat) # 1. Dataclass.py에서 온 자료형 클래스
    members_message = pyqtSignal(Members)
    def __init__(self, client:Client):
        super().__init__()
        self.client = client

    def run(self) -> None:
        while True:
            data = self.client.recevie()

            print("[ 데이터 수신 ]")
            print('여기는 리시브 스레드 파이 파일')
            print('받은 데이터는', data)
            # 수신된 데이터 타입에 따른 시그널 방향 제시
            if type(data) == ReqChat: # 2. 조건에 따라 시그널 보내줌
                self.res_message.emit(data)
            if type(data) == Members:
                self.members_message.emit(data)
