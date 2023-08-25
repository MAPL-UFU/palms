"""
Created on Jan , 2020
@author: Roger H. Carrijo
git: roger1618

Updated on Ago 20, 2023
@author: Roger H. Carrijo

"""

import sys
import json
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from MqttThreadQt import MqttThreadQt
from gui.MainWindow import Ui_MainWindow
from gui.PopupInfo import PopupInfo

from palms.Pnrd import Pnrd
from palms.FileCreator import FileCreator


class PalmsGui:
    def __init__(
        self,
        wifi_ssid,
        wifi_password,
        mqtt_broker,
        mqtt_port,
        mqtt_username,
        mqtt_password,
    ):
        # Variables
        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port
        self.mqtt_username = mqtt_username
        self.mqtt_password = mqtt_password
        self.wifi_ssid = wifi_ssid
        self.wifi_password = wifi_password
        self.pnrd = Pnrd()
        self.pnrd_setup_is_ok = False
        self.pnrd_comm = dict()
        self.msg_thread = dict()
        self.count_antenna = 0
        self.qtd_antena = 0
        self.reader_list = []
        self.transition_names = []
        self.array_marking = []
        self.palms_type = ""
        self.text_setup = ""
        app = QtWidgets.QApplication(sys.argv)

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        # ----------------------------------------------------------------------------------------------
        self.ui.actionopen_pnml.triggered.connect(self.open_pnml_file)
        self.ui.actionOpen_Setup_File_palms.triggered.connect(self.open_palms_file)
        self.ui.setupPalms_comboBox.currentIndexChanged.connect(self.setup_palms_type)
        self.ui.addIP_pushButton.clicked.connect(self.append_reader)
        self.ui.createSetup_pushButton.clicked.connect(self.create_palms_file)
        self.ui.nAntennas_spinBox.setMinimum(1)
        self.ui.setup_tabWidget.setCurrentIndex(0)

        # ---------------------------------------------------------------------------------------------
        # RUNTIME
        self.ui.confirmSerialConection_pushButton.clicked.connect(
            self.verify_palms_loader
        )
        self.ui.stopConnection_pushButton.clicked.connect(self.stop_connection)
        # --------------------------------------------------------------------------
        self.MainWindow.show()
        sys.exit(app.exec_())

    def setup_palms_type(self):
        self.palms_type = self.ui.setupPalms_comboBox.currentText()
        if self.palms_type == "iPNRD":
            self.ui.nAntennas_spinBox.setMaximum(1)
            self.ui.nAntennas_spinBox.setMinimum(1)
            self.ui.qtdTotalTansitions_label.setText(f"(Left: {1})")
        if self.palms_type == "PNRD":
            self.ui.nAntennas_spinBox.setMinimum(1)
            self.ui.qtdTotalTansitions_label.setText(f"(Left: {self.count_antenna})")
        return self.palms_type

    def create_palms_file(self):
        self.palms_type = self.ui.setupPalms_comboBox.currentText()
        self.get_transition_names(self.pnrd.len_transitions, self.pnrd.len_places)

        dict_palms = {
            "pnmlFile": self.pnrd.file,
            "type": self.palms_type,
            "qtdReaders": len(self.reader_list),
            "readerListConfig": self.reader_list,
            "transitionNames": self.transition_names,
        }
        wifi = {"ssid": self.wifi_ssid, "password": self.wifi_password}
        mqtt = {
            "broker": self.mqtt_broker,
            "port": self.mqtt_port,
            "username": self.mqtt_username,
            "password": self.mqtt_password,
        }
        self.pnrd.create_palms_file(dict_palms)

        if self.palms_type == "PNRD":
            self.pnrd.create_pnrd_init_file(mqtt=mqtt, wifi=wifi)
            self.pnrd.create_pnrd_reader_file(
                readers=self.reader_list, mqtt=mqtt, wifi=wifi
            )
        elif self.palms_type == "iPNRD":
            self.pnrd.create_ipnrd_init_file(mqtt=mqtt, wifi=wifi)
            self.pnrd.create_ipnrd_reader_file(
                readers=self.reader_list, mqtt=mqtt, wifi=wifi
            )

        self.ui.popup_info = PopupInfo(
            "Successfully created PALMS file!\nTo open file and use runtime mode press (Ctrl + F)"
        )
        self.ui.popup_info.show()
        self.ui.createSetup_pushButton.setEnabled(False)
        self.ui.addIP_pushButton.setEnabled(False)

    def _get_reader_data(self):
        return {
            "readerName": self.ui.readerName_lineEdit.text(),
            "IP": self.ui.IP_lineEdit.text(),
            "qtdAntenna": 0,
        }

    def append_reader(self):
        palms_type = self.setup_palms_type()
        reader_data = self._get_reader_data()

        if palms_type == "PNRD":
            qtd_antenna, count_antennas = self.set_antennas()
            if count_antennas <= 0:
                self.ui.addIP_pushButton.setEnabled(False)
            reader_data["qtdAntenna"] = qtd_antenna
        else:
            reader_data["qtdAntenna"] = 1
            self.ui.addIP_pushButton.setEnabled(False)

        self.reader_list.append(reader_data)
        self.text_setup += f"Reader: {reader_data['readerName']} Port: '{reader_data['IP']}' Ant: {reader_data['qtdAntenna']} unit{'s' if reader_data['qtdAntenna'] > 1 else ''}\n"
        self.ui.setupInfo_label.setText(
            f"P: {self.pnrd.len_places} | T: {self.pnrd.len_transitions}\n{self.text_setup}"
        )

    def get_transition_names(self, n_row, n_col):
        self.transition_names = []
        for i in range(n_row):
            matrix_transition_item = self.ui.incMatrix_tw.item(i, n_col)
            self.transition_names.append(matrix_transition_item.text())

    def set_antennas(self):
        if self.count_antenna >= self.ui.nAntennas_spinBox.value():
            self.count_antenna -= self.ui.nAntennas_spinBox.value()
        qtd_reader_antenna = self.ui.nAntennas_spinBox.value()
        self.ui.nAntennas_spinBox.setMaximum(1)
        self.ui.qtdTotalTansitions_label.setText(f"(Left: {self.count_antenna})")
        if self.count_antenna > 0 and self.count_antenna <= 3:
            self.ui.nAntennas_spinBox.setMaximum(self.count_antenna)
        if self.count_antenna == 0:
            self.ui.nAntennas_spinBox.setMaximum(0)
            self.ui.nAntennas_spinBox.setMinimum(0)
        return qtd_reader_antenna, self.count_antenna

    def pnrd_setup(self, filename):
        _, created = self.pnrd.pnrd_setup(filename)
        if created:
            self.setup_matrix_view(self.pnrd.len_transitions, self.pnrd.len_places)
            self.ui.matrix_array.setText(f"{self.pnrd.incidence_vector}")
            self.setup_marking_vector(self.pnrd.len_places)
            self.pnrd_setup_is_ok = True
            self.count_antenna = self.pnrd.len_transitions
            self.ui.nAntennas_spinBox.setRange(1, self.pnrd.len_transitions)
            self.ui.qtdTotalTansitions_label.setText(f"(Left: {self.count_antenna})")
            self.setup_palms_type()
        else:
            self.ui.popup_info = PopupInfo("Error loading PNML file")
            self.ui.popup_info.show()

    def pnrd_palms_for_runtime(self, filename):
        with open(filename, "r") as palms_file:
            palms = json.load(palms_file)
            _, created = self.pnrd.pnrd_setup(palms["pnmlFile"])
            if created:
                self.pnrd.transition_names = palms["transitionNames"]
                self.setup_matrix_view(
                    self.pnrd.len_transitions, self.pnrd.len_places, "palms"
                )
                self.ui.matrix_array.setText(f"{self.pnrd.incidence_vector}")
                self.setup_marking_vector(self.pnrd.len_places)
                self.pnrd_setup_is_ok = True
                self.setup_palms_type()
                self.ui.palmsType_label.setText(f'Type: {palms["type"]}')
                self.ui.qtdReader_label.setText(f'Qtd Readers: {palms["qtdReaders"]}')
                readers_list = ""
                for i in palms["readerListConfig"]:
                    readers_list += f'Reader: {i["readerName"]} \n  Topic: client_{i["readerName"]} \n  IP: {i["IP"]}\n\n'
                self.ui.readerList_label.setText(readers_list)
                self.reader_list = palms["readerListConfig"]

    def setup_matrix_view(self, n_row, n_col, _type="pnml"):
        self.ui.incMatrix_tw.setRowCount(n_row)
        self.ui.incMatrix_tw.setColumnCount(n_col + 1)
        self.ui.incMatrix2_tw.setRowCount(n_row)
        self.ui.incMatrix2_tw.setColumnCount(n_col + 1)
        count_row = 0
        horizontalHeader = []
        verticalHeader = []
        for row in self.pnrd.incidence_matrix:
            count_col = 0
            for i in row:
                if len(horizontalHeader) < n_col:
                    horizontalHeader.append(f" P{count_col} ")
                if count_col == (n_col - 1):
                    if _type == "palms":
                        self.ui.incMatrix_tw.setItem(
                            count_row,
                            count_col + 1,
                            QTableWidgetItem(
                                f"{self.pnrd.transition_names[count_row]}"
                            ),
                        )
                        self.ui.incMatrix2_tw.setItem(
                            count_row,
                            count_col + 1,
                            QTableWidgetItem(
                                f"{self.pnrd.transition_names[count_row]}"
                            ),
                        )
                    else:
                        self.ui.incMatrix_tw.setItem(
                            count_row,
                            count_col + 1,
                            QTableWidgetItem(f"transition {count_row}"),
                        )
                        self.ui.incMatrix2_tw.setItem(
                            count_row,
                            count_col + 1,
                            QTableWidgetItem(f"transition {count_row}"),
                        )

                self.ui.incMatrix_tw.setItem(
                    count_row, count_col, QTableWidgetItem(f"{i}")
                )
                self.ui.incMatrix2_tw.setItem(
                    count_row, count_col, QTableWidgetItem(f"{i}")
                )
                count_col += 1
            verticalHeader.append(f" T{count_row} ")
            count_row += 1
        horizontalHeader.append("  ")
        self.ui.incMatrix_tw.setHorizontalHeaderLabels(horizontalHeader)
        self.ui.incMatrix2_tw.setHorizontalHeaderLabels(horizontalHeader)
        self.ui.incMatrix_tw.setVerticalHeaderLabels(verticalHeader)
        self.ui.incMatrix2_tw.setVerticalHeaderLabels(verticalHeader)
        self.ui.places_label.setText(f"Places: {self.pnrd.len_places}")
        self.ui.transitions_label.setText(f"Transitions: {self.pnrd.len_transitions}")

    def setup_marking_vector(self, n_row):
        count_row = 0

        self.ui.markingVector_tw.setRowCount(n_row)
        self.ui.markingVector_tw.setColumnCount(1)
        self.ui.markingVector2_tw.setRowCount(n_row)
        self.ui.markingVector2_tw.setColumnCount(1)
        verticalHeader = []

        for i in self.pnrd.marking_vector:
            verticalHeader.append(f" P{count_row} ")
            self.ui.markingVector_tw.setItem(count_row, 0, QTableWidgetItem(f"{i}"))
            self.ui.markingVector2_tw.setItem(count_row, 0, QTableWidgetItem(f"{i}"))

            count_row += 1

        self.ui.marking_array.setText(f"{self.pnrd.marking_vector}")
        self.ui.markingVector_tw.setHorizontalHeaderLabels([""])
        self.ui.markingVector_tw.setVerticalHeaderLabels(verticalHeader)
        self.ui.markingVector2_tw.setHorizontalHeaderLabels([""])
        self.ui.markingVector2_tw.setVerticalHeaderLabels(verticalHeader)

    def open_pnml_file(self):
        self.ui.createSetup_pushButton.setEnabled(True)
        self.ui.addIP_pushButton.setEnabled(True)
        filename, _ = QFileDialog.getOpenFileName(filter="pnml(*.pnml)")
        self.ui.setup_tabWidget.setCurrentIndex(0)
        self.ui.setup_tabWidget.setTabEnabled(0, True)
        self.ui.setup_tabWidget.setTabEnabled(1, False)
        if filename != "":
            self.pnrd_setup(filename)

    def open_palms_file(self):
        filename, _ = QFileDialog.getOpenFileName(filter="palms(*.palms)")
        self.ui.setup_tabWidget.setTabEnabled(1, True)
        self.ui.setup_tabWidget.setTabEnabled(0, False)
        self.ui.setup_tabWidget.setCurrentIndex(1)
        if filename != "":
            self.pnrd_palms_for_runtime(filename)

    # ----------------------------------------------------------

    def fire_vector(self, vector):
        return self.pnrd.update_pnml(fire_vector=vector)

    def token_vector(self, vector):
        return self.pnrd.update_pnml(token=vector, _type="token")

    def connect_mqtt(self):
        self.msg_thread = MqttThreadQt(
            mqtt_broker=self.mqtt_broker,
            mqtt_port=self.mqtt_port,
            mqtt_username=self.mqtt_username,
            mqtt_password=self.mqtt_password,
            readers=self.reader_list,
        )
        self.msg_thread.start()
        self.msg_thread.msg_status.connect(self.set_msg_status)
        self.ui.confirmSerialConection_pushButton.setEnabled(False)
        self.ui.info_label.setStyleSheet("QLabel#info_label {color: green}")
        self.ui.info_label.setText("Successfully connected")

    def verify_palms_loader(self):
        if self.pnrd_setup_is_ok:
            self.connect_mqtt()
        else:
            self.ui.info_label.setStyleSheet("QLabel#info_label {color: red}")
            self.ui.info_label.setText("You need to load PALMS file first")

    def set_msg_status(self, msg_status, msg):
        try:
            payload = self.pnrd.decode_pnrd_reader_msg(msg["payload"])
            self.pnrd_comm["id"] = payload["id"]
            self.pnrd_comm["reader"] = payload["readerId"]
            self.pnrd_comm["error"] = payload["pnrd"]
            self.pnrd_comm["antenna"] = payload["ant"]
            self.pnrd_comm["fire"] = int(payload["fire"])
            # ----------------------------------------------------
            runtime_file = FileCreator("palmsSetup", self.pnrd.file, "runtime", "json")
            runtime_file.set_text_increment(
                json.dumps(payload, indent=4, sort_keys=True)
            )
            self.ui.id_label.setText("TagId: " + str(self.pnrd_comm["id"]))
            self.ui.reader_label.setText("Reader: " + str(self.pnrd_comm["reader"]))
            self.ui.exception_label.setText("PNRD: " + str(self.pnrd_comm["error"]))
            self.ui.info_label.setStyleSheet("QLabel#info_label {color: green}")
            self.ui.info_label.setText(msg_status)
            if self.pnrd_comm["error"] != "INIT_TAG":
                self.update_pnrd(payload)
                for i in range(self.pnrd.len_transitions):
                    if i != self.pnrd_comm["fire"]:
                        self.ui.incMatrix2_tw.item(
                            i, self.pnrd.len_places
                        ).setBackground(QtGui.QColor(255, 255, 255))
                    else:
                        self.ui.incMatrix2_tw.item(
                            i, self.pnrd.len_places
                        ).setBackground(QtGui.QColor(0, 255, 0))

        except Exception as error:
            print(error)
            if msg_status is not None:
                self.ui.info_label.setStyleSheet("QLabel#info_label {color: red}")
                self.ui.info_label.setText(msg_status)
                self.ui.confirmSerialConection_pushButton.setEnabled(True)

            else:
                self.ui.info_label.setStyleSheet("QLabel#info_label {color: red}")
                self.ui.info_label.setText("Erro ao carregar dados")

    def update_pnrd(self, pnrd):
        token = pnrd["token"]
        msg, is_ok = self.token_vector(token)
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
        except Exception:
            self.ui.info_label.setStyleSheet("QLabel#info_label {color: red}")
            self.ui.info_label.setText("Close Your  Connection before Stop")
            self.ui.confirmSerialConection_pushButton.setEnabled(False)
            self.ui.stopConnection_pushButton.setEnabled(False)

    def __str__(self) -> str:
        return f"PalmsGui: {self.pnrd}"
