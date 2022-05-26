from PyQt5.QtWidgets import *
import sys,pickle
from PyQt5 import uic, QtWidgets ,QtCore, QtGui

# cmd창에서 pip freeze > requirements.txt 을 통해서 가상환경에서 설치된 라이브러리의 버전을 확인할 수 있다.
# 나중에 해당 파일만 있으면 같은 작업을 할 수 있지...

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi('mainwindow.ui',self)
        
        # self.show()
    if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        window = UI()
        window.show()
        
        sys.exit(app.exec_)