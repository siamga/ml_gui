from PyQt5.QtWidgets import *
import sys,pickle
from PyQt5 import uic, QtWidgets ,QtCore, QtGui
from data_visualise import data_ 

# cmd창에서 pip freeze > requirements.txt 을 통해서 가상환경에서 설치된 라이브러리의 버전을 확인할 수 있다.
# 나중에 해당 파일만 있으면 같은 작업을 할 수 있지...

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi('mainwindow.ui',self)
        
        global data, steps
        data = data_()
        
        self.Browse = self.findChild(QPushButton, 'Browse')
        self.columns = self.findChild(QListWidget, 'column_list')
        
        self.Browse.clicked.connect(self.getCSV)
        
    def filldetails(self, flag = 1):
        if flag == 0 :
            self.df = data.read_file(str(self.filePath))
        
        # self.columns.clear()
        self.column_list = data.get_column_list(self.df)
        print(self.column_list)
        
        for i , j in enumerate(self.column_list):
            stri = f'{j}......{str(self.df[j].dtype)}'
            # print(stri)
            self.columns.insertItem(i, stri)
            
    
    
    def getCSV(self):
        self.filePath , _ = QtWidgets.QFileDialog.getOpenFileName(self,'Open file',"","csv(*.csv)")
        self.columns.clear()
        print(self.filePath)
        
        if self.filePath != "":
            self.filldetails(0)
        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    window.show()
    
    sys.exit(app.exec_)