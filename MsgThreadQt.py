import os
from time import sleep

from PyQt5.QtCore import QThread, pyqtSignal
from palms.async_serial_comu import start
import asyncio
import serial_asyncio

class MsgThreadQt(QThread):   
    msg_status = pyqtSignal(str,dict, name='msg_status')            # define new Signal    
    def __init__(self,serial_port,parent=None):

        super(MsgThreadQt, self).__init__(parent)
        self.serial_port = serial_port
        self.is_running = True
        self.pnrd = dict()
        self.loop = asyncio.get_event_loop()

    def run(self):
        while True:
            if not self.is_running:
                break
            try:
                port =self.serial_port #'/dev/ttyUSB0'
                done,_  = self.loop.run_until_complete(start(self.loop,port))
                for fut in done:
                    self.pnrd = fut.result()
                try:
                    self.msg_status.emit("Receiving date",self.pnrd)
                    print(f"{self.pnrd}")
                    sleep(5)
                except:
                    self.msg_status.emit("Serial Connection Error",dict())
                    print(f"{self.pnrd}")
                    sleep(5)
            except:
                self.msg_status.emit("Permission Denied Serial Port",dict())
                self.loop.stop()
                
        # is_ok,file_names_array = firebird.connect(self.query_dict, location_dir='dados')
        # if is_ok:
            
        #     self.msg_status.emit('Enviando para o Destino...','')
        #     is_sended,msg = postgres.send_csv(file_names_array)

        #     #Envia os dados em forma Csv para o pasta especificada no location_dir
        #     self.msg_status.emit('Enviar Dados',msg)
        #     sleep(0.1)
        #     self.stop()

        # else:
        #     mgs = "Erro na Comunicação com a Origem"
        #     self.msg_status.emit('Enviar Dados',mgs)
        #     sleep(0.1)
        #     self.stop()

    def stop(self):
        self.is_running = False
        print('stopping thread...')
        self.terminate()
        print('Thread morta')
        self.loop.stop()
        self.loop.close()
