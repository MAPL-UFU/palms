'''
Created on Jan , 2020

@author: Roger H. Carrijo
git: roger1618
'''
import os
import datetime
import sys
from time import sleep
from PyQt5 import QtCore, QtWidgets, QtSql
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from MsgThreadQt import MsgThreadQt
from gui.MainWindow import Ui_MainWindow
from pprint import pprint
from palms.Pnrd import Pnrd


class PalmsGui():
   
    def __init__(self):
        #Variables
        
        self.pnrd = Pnrd()
        self.pnrd_setup_is_ok = False
        self.serial_port = '/dev/ttyUSB0'
        self.pnrd_serial = dict()
        self.msg_thread = ''
        app = QtWidgets.QApplication(sys.argv)
        

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow) 
#----------------------------------------------------------------------------------------------
        self.ui.actionopen_pnml.triggered.connect(self.open_file)
        self.ui.confirmSerialConection_pushButton.clicked.connect(self.verify_pnml_loader)
        self.ui.serialConection_lineEdit.setText(self.serial_port)
        self.ui.stopConnection_pushButton.clicked.connect(self.stop_connection)
#---------------------------------------------------------------------------------------------
        self.MainWindow.show()
        sys.exit(app.exec_()) 


    def pnrd_setup(self,filename):
        _,ok = self.pnrd.set_pnml(filename)
        if ok:
            _,created = self.pnrd.create_net()
            if created:
                self.setup_matrix(self.pnrd.len_places,self.pnrd.len_transitions)
                self.setup_marking_vector(self.pnrd.len_places)
                self.pnrd_setup_is_ok = True

    def setup_matrix(self,n_row,n_col):

        self.ui.incMatrix_tw.setRowCount(n_row)
        self.ui.incMatrix_tw.setColumnCount(n_col+1)
        count_row = 0
        horizontalHeader = []
        verticalHeader = []
        self.array_matrix = []
        for row in self.pnrd.incidence_matrix_t:
            count_col = 0
            for i in row:
                    if len(horizontalHeader) < n_col:
                        horizontalHeader.append(f" T{count_col} ")
                    self.ui.incMatrix_tw.setItem( count_row,count_col, QTableWidgetItem(f"{i}"))
                    count_col+=1
                    self.array_matrix.append(i)
            
            verticalHeader.append(f" P{count_row} ")

            count_row+=1
        horizontalHeader.append(f"  ")
        self.ui.matrix_array.setText(f"{self.array_matrix}")
        self.ui.incMatrix_tw.setHorizontalHeaderLabels(horizontalHeader)
        self.ui.incMatrix_tw.setVerticalHeaderLabels(verticalHeader)   
        self.ui.places_label.setText(f'Places: {self.pnrd.len_places}')
        self.ui.transitions_label.setText(f'Transitions: {self.pnrd.len_transitions}')


    def setup_marking_vector(self,n_row):

        count_row = 0

        self.ui.markingVector_tw.setRowCount(n_row)
        self.ui.markingVector_tw.setColumnCount(1)
        verticalHeader = []
        self.array_marking= []

        for i in self.pnrd.marking_vector:

            verticalHeader.append(f" P{count_row} ")
            self.ui.markingVector_tw.setItem(count_row,0, QTableWidgetItem(f"{i}"))
            self.array_marking.append(i)
            count_row+=1

        self.ui.marking_array.setText(f"{self.array_marking}")    
        self.ui.markingVector_tw.setHorizontalHeaderLabels([""])    
        self.ui.markingVector_tw.setVerticalHeaderLabels(verticalHeader) 


    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(filter ="pnml(*.pnml)")
        self.pnrd_setup(filename)
        
    #----------------------------------------------------------

    def fire_vector(self,vector):
        return self.pnrd.update_pnml(fire_vector=fire_vector)

    def token_vector(self,vector):

        return self.pnrd.update_pnml(token=vector, _type='token')
    

    def verify_pnml_loader(self):

        if self.pnrd_setup_is_ok:
            self.connect_serial_port()
        else:
            self.ui.info_label.setText("You need to load PNML file first")

    def connect_serial_port(self):

        self.serial_port = self.ui.serialConection_lineEdit.text()
        self.msg_thread = MsgThreadQt(self.serial_port, parent=None)
        self.msg_thread.start()
        self.ui.confirmSerialConection_pushButton.setEnabled(False)
        self.msg_thread.msg_status.connect(self.set_msg_status)


    def set_msg_status(self, msg_status, msg):

        try:
            self.pnrd_serial['id'] = msg["id"]
            self.pnrd_serial['reader'] = msg["readerId"]
            self.pnrd_serial['error'] = msg["pnrd"]
            self.ui.id_label.setText("TagId: "+str( self.pnrd_serial['id']))
            self.ui.reader_label.setText("Reader: "+str( self.pnrd_serial['reader']))
            self.ui.exception_label.setText("PNRD: "+str( self.pnrd_serial['error']))
            self.ui.info_label.setText(msg_status)  
            self.update_pnrd(msg)
        except:
            self.ui.info_label.setText("Erro ao carregar dados") 

        
           
        

    def update_pnrd(self,pnrd):
        token = pnrd['token']
        msg,is_ok = self.token_vector(token)
        if not is_ok:
            self.ui.info_label.setText(str(msg))
        self.setup_marking_vector(self.pnrd.len_places)
        self.pnrd_setup_is_ok = True
        

    def stop_connection(self):
        try:
            self.msg_thread.stop()
            self.ui.info_label.setText("Connection Closed")
            self.ui.confirmSerialConection_pushButton.setEnabled(True)
            self.ui.stopConnection_pushButton.setEnabled(False)
        except:
            self.ui.info_label.setText("Close Your Serial Connection before Stop")