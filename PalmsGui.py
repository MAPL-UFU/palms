'''
Created on Jan , 2020

@author: Roger H. Carrijo
git: roger1618
'''
import os
import datetime
import sys
import json
from time import sleep
from PyQt5 import QtCore, QtWidgets, QtSql
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from MsgThreadQt import MsgThreadQt
from gui.MainWindow import Ui_MainWindow
from pprint import pprint

from palms.Pnrd import Pnrd
from palms.utils.find_serial_port import serial_ports
from palms.FileCreator import FileCreator
import serial



class PalmsGui():
   
    def __init__(self):
        #Variables
        
        self.pnrd = Pnrd()
        self.pnrd_setup_is_ok = False
        self.serial_port_verify, self.serial_port = serial_ports()
        self.pnrd_serial = dict()
        self.msg_thread = ''
        self.count_antenna = 0   
        self.qtd_antena = 0    
        self.reader_list = []
        self.transition_names = []
        self.palms_type = ''
        self.text_setup = ''
        app = QtWidgets.QApplication(sys.argv)
        
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow) 
       
#----------------------------------------------------------------------------------------------  
        # self.ui.serialConection_lineEdit.setText(self.serial_port)
        self.ui.actionopen_pnml.triggered.connect(self.open_file)
        self.ui.confirmSerialConection_pushButton.clicked.connect(self.verify_pnml_loader)
        self.ui.stopConnection_pushButton.clicked.connect(self.stop_connection)   
        self.ui.addSerial_pushButton.clicked.connect(self.append_reader)  
        self.ui.createSetup_pushButton.clicked.connect(self.create_palms_file)  
        self.set_comboBox(self.serial_port,'COM')
#---------------------------------------------------------------------------------------------
        self.MainWindow.show()
        sys.exit(app.exec_()) 


    def create_palms_file(self):
        self.palms_type = self.ui.setupPalms_comboBox.currentText()
        self.get_transition_names(self.pnrd.len_transitions,self.pnrd.len_places)

        dict_palms = {
            "pnmlFile": self.pnrd.file,
            "type": self.palms_type,
            "qtdReaders":len(self.reader_list),
            "readerListConfig": self.reader_list,
            "transitionNames": self.transition_names
        }
        palms_file = FileCreator('palmsSetup','setup','palms')
        palms_file.set_text(json.dumps(dict_palms, indent=4, sort_keys=True))


    def append_reader(self):
        temp_antenna = self.set_antennas()
        if temp_antenna >0 :
            reader_name = self.ui.readerName_lineEdit.text()
            qtd_antena = temp_antenna
            serial_connection = self.ui.serialConection_comboBox.currentText()
            self.serial_port.remove(serial_connection)
            self.set_comboBox(self.serial_port,'COM')
            self.reader_list.append({"readerName":reader_name,"qtdAntenna":qtd_antena,"serialPort":serial_connection})
            print(self.reader_list)
            self.text_setup += f"Reader: {reader_name} Port: '{serial_connection}' Ant: {qtd_antena} units\n"
           
            self.ui.setupInfo_label.setText(f'P: {self.pnrd.len_places} | T: {self.pnrd.len_transitions}\n{self.text_setup}')

    def get_transition_names(self,n_row,n_col):
        self.transition_names = []
        for i in range(n_row):
            matrix_transition_item = self.ui.incMatrix_tw.item(i,n_col)
            self.transition_names.append(matrix_transition_item.text())


    def set_antennas(self):
        if self.count_antenna>=self.ui.nAntennas_spinBox.value():
            self.count_antenna -=self.ui.nAntennas_spinBox.value() 

        self.ui.nAntennas_spinBox.setMaximum(self.count_antenna)    
        self.ui.qtdTotalTansitions_label.setText(f'(Left: {self.count_antenna})')
        if self.count_antenna>0:
            self.ui.nAntennas_spinBox.setMaximum(self.count_antenna)
        if self.count_antenna==0:
            self.ui.nAntennas_spinBox.setMaximum(0)
            self.ui.nAntennas_spinBox.setMinimum(0)

        return self.pnrd.len_transitions - self.count_antenna


    def set_comboBox(self,lista,fonte):
        if fonte =='setup':
            pass
            # self.ui.comboBox_tabela_origem.clear()
            # self.ui.comboBox_tabela_origem.addItems(lista)
        elif fonte =='COM':
            self.ui.serialConection_comboBox.clear()
            self.ui.serialConection_comboBox.addItems(lista)


    def pnrd_setup(self,filename):
        _,ok = self.pnrd.set_pnml(filename)
        if ok:
            _,created = self.pnrd.create_net()
            if created:
                self.setup_matrix(self.pnrd.len_transitions,self.pnrd.len_places)
                self.setup_marking_vector(self.pnrd.len_places)
                self.pnrd_setup_is_ok = True
                self.count_antenna = self.pnrd.len_transitions
                self.ui.nAntennas_spinBox.setRange(1, self.pnrd.len_transitions)
                self.ui.qtdTotalTansitions_label.setText(f'(Left: {self.count_antenna})')


    def setup_matrix(self,n_row,n_col):
        self.ui.incMatrix_tw.setRowCount(n_row)
        self.ui.incMatrix_tw.setColumnCount(n_col+1)
        count_row = 0
        horizontalHeader = []
        verticalHeader = []
        self.array_matrix = []
        for row in self.pnrd.incidence_matrix:
            count_col = 0
            for i in row:
                    if len(horizontalHeader) < n_col:
                        horizontalHeader.append(f" P{count_col} ")
                    if count_col==(n_col -1):
                        self.ui.incMatrix_tw.setItem( count_row,count_col+1, QTableWidgetItem(f"transition {count_col}{count_row}"))
                    self.ui.incMatrix_tw.setItem( count_row,count_col, QTableWidgetItem(f"{i}"))
                    count_col+=1
                    self.array_matrix.append(i)
                   

            verticalHeader.append(f" T{count_row} ")

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
        self.serial_port = self.ui.serialConection_lineEdit.text()
        if self.pnrd_setup_is_ok:
            try:
                ard = serial.Serial(self.serial_port,9600,timeout=5)
                print(self.serial_port)
                ard.flush()
                ard.close()
                sleep(0.1)
                self.connect_serial_port()
            except:
                self.ui.info_label.setText("Problem with your Serial Connection")
        else:
            self.ui.info_label.setStyleSheet('QLabel#info_label {color: red}')
            self.ui.info_label.setText("You need to load PNML file first")

    def connect_serial_port(self):

        self.serial_port = self.ui.serialConection_lineEdit.text()
        self.msg_thread = MsgThreadQt(self.serial_port, parent=None)
        self.msg_thread.start()
        self.msg_thread.msg_status.connect(self.set_msg_status)
        self.ui.confirmSerialConection_pushButton.setEnabled(False)
        self.ui.info_label.setStyleSheet('QLabel#info_label {color: green}')
        self.ui.info_label.setText("Successfully connected")

    def set_msg_status(self, msg_status, msg):

        try:
            self.pnrd_serial['id'] = msg["id"]
            self.pnrd_serial['reader'] = msg["readerId"]
            self.pnrd_serial['error'] = msg["pnrd"]
            
            self.ui.id_label.setText("TagId: "+str( self.pnrd_serial['id']))
            self.ui.reader_label.setText("Reader: "+str( self.pnrd_serial['reader']))
            self.ui.exception_label.setText("PNRD: "+str( self.pnrd_serial['error']))
            self.ui.info_label.setStyleSheet('QLabel#info_label {color: green}')
            self.ui.info_label.setText(msg_status)  
            self.update_pnrd(msg)
        except:
            if  msg_status !=None: 
                self.ui.info_label.setStyleSheet('QLabel#info_label {color: red}')
                self.ui.info_label.setText(msg_status) 
                self.ui.confirmSerialConection_pushButton.setEnabled(True)

            else:
                self.ui.info_label.setStyleSheet('QLabel#info_label {color: red}')
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
            self.ui.info_label.setStyleSheet('QLabel#info_label {color: red}')
            self.ui.info_label.setText("Close Your Serial Connection before Stop")
            self.ui.confirmSerialConection_pushButton.setEnabled(False)
            self.ui.stopConnection_pushButton.setEnabled(False)