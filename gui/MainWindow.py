# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/qtGui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 609)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(50, 50))
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(55, 60, 85);\n"
"}\n"
"QTabWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid rgb(221, 216, 216);\n"
"}\n"
"QTabWidget::pane{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid rgb(221, 216, 216);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    background-color: rgb(238, 238, 236);\n"
"    border:1px solid rgb(221, 216, 216);\n"
"    alignment: center;\n"
"}\n"
"QTabBar::tab {\n"
"    background-color: white;\n"
"    border-color:rgb(186, 189, 182);\n"
"    padding: 5px;\n"
"    margin-bottom:0px;\n"
"    \n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: rgb(136, 138, 133);\n"
"    background-color: rgb(46, 52, 54);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QTableWidget {\n"
"    border:1px  solid rgb(221, 216, 216);\n"
"    \n"
"}\n"
"\n"
"QTableWidget::section {\n"
"    background-color: transparent;\n"
"    border:0px solid transparent;\n"
"}\n"
"\n"
"QHeaderView::section,QHeaderView{\n"
"      background-color: white;\n"
"}\n"
"\n"
"QGroupBox#groupBoxMatrix, QGroupBox#markingGroupBox{\n"
"    background-color: white;\n"
"    border:1px, solid ,rgb(221, 216, 216);\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    background-color: white;\n"
"}\n"
"QHeaderView::section:horizontal{background-color:rgb(238, 238, 236);}\n"
"\n"
"\n"
"#places_label{color:rgb(60, 167, 61);\n"
"font: 75 12pt \"Courier 10 Pitch\";}\n"
"#transitions_label{color:rgb(60, 167, 61);\n"
"font: 75 12pt \"Courier 10 Pitch\";}\n"
"\n"
"#id_label{color:rgb(48, 140, 198);\n"
"font: 75 12pt \"Courier 10 Pitch\";}\n"
"\n"
"#reader_label{color:rgb(60, 167, 61);\n"
"font: 75 12pt \"Courier 10 Pitch\";}\n"
"\n"
"#exception_label{color:rgb(204, 0, 0);\n"
"font: 75 12pt \"Courier 10 Pitch\";}\n"
"\n"
"#info_label{color:rgb(204, 0, 0);\n"
"font: 75 12pt \"Courier 10 Pitch\";}\n"
"\n"
"QGroupBox#groupBox_Labels{\n"
"    background-color: white;\n"
"    border:0px ,solid ,rgb(186, 189, 182);\n"
"}\n"
"\n"
"QTabWidget{\n"
"    background-color:rgb(242, 242, 242);\n"
"}\n"
"//rgb(238, 238, 236)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.setup_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.setup_tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.setup_tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.setup_tabWidget.setObjectName("setup_tabWidget")
        self.tab_setup = QtWidgets.QWidget()
        self.tab_setup.setObjectName("tab_setup")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_setup)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.tab_setup)
        self.label_5.setMaximumSize(QtCore.QSize(230, 120))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("gui/qtGui/images/femec.jpeg"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.tab_setup)
        self.label_3.setMaximumSize(QtCore.QSize(250, 30))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.serialConection_lineEdit = QtWidgets.QLineEdit(self.tab_setup)
        self.serialConection_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.serialConection_lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        self.serialConection_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.serialConection_lineEdit.setObjectName("serialConection_lineEdit")
        self.verticalLayout_4.addWidget(self.serialConection_lineEdit)
        self.confirmSerialConection_pushButton = QtWidgets.QPushButton(self.tab_setup)
        self.confirmSerialConection_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.confirmSerialConection_pushButton.setMaximumSize(QtCore.QSize(250, 16777215))
        self.confirmSerialConection_pushButton.setObjectName("confirmSerialConection_pushButton")
        self.verticalLayout_4.addWidget(self.confirmSerialConection_pushButton)
        self.groupBox_Labels = QtWidgets.QGroupBox(self.tab_setup)
        self.groupBox_Labels.setMaximumSize(QtCore.QSize(250, 150))
        self.groupBox_Labels.setTitle("")
        self.groupBox_Labels.setObjectName("groupBox_Labels")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_Labels)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.exception_label = QtWidgets.QLabel(self.groupBox_Labels)
        self.exception_label.setText("")
        self.exception_label.setObjectName("exception_label")
        self.verticalLayout_3.addWidget(self.exception_label)
        self.reader_label = QtWidgets.QLabel(self.groupBox_Labels)
        self.reader_label.setText("")
        self.reader_label.setObjectName("reader_label")
        self.verticalLayout_3.addWidget(self.reader_label)
        self.id_label = QtWidgets.QLabel(self.groupBox_Labels)
        self.id_label.setText("")
        self.id_label.setObjectName("id_label")
        self.verticalLayout_3.addWidget(self.id_label)
        self.places_label = QtWidgets.QLabel(self.groupBox_Labels)
        self.places_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.places_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.places_label.setObjectName("places_label")
        self.verticalLayout_3.addWidget(self.places_label)
        self.transitions_label = QtWidgets.QLabel(self.groupBox_Labels)
        self.transitions_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.transitions_label.setObjectName("transitions_label")
        self.verticalLayout_3.addWidget(self.transitions_label)
        self.verticalLayout_4.addWidget(self.groupBox_Labels)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.markingGroupBox = QtWidgets.QGroupBox(self.tab_setup)
        self.markingGroupBox.setMinimumSize(QtCore.QSize(100, 0))
        self.markingGroupBox.setMaximumSize(QtCore.QSize(120, 16777215))
        self.markingGroupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.markingGroupBox.setTitle("")
        self.markingGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.markingGroupBox.setObjectName("markingGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.markingGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.marking_vector = QtWidgets.QLabel(self.markingGroupBox)
        self.marking_vector.setMinimumSize(QtCore.QSize(30, 30))
        self.marking_vector.setMaximumSize(QtCore.QSize(120, 16777215))
        self.marking_vector.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.marking_vector.setAlignment(QtCore.Qt.AlignCenter)
        self.marking_vector.setObjectName("marking_vector")
        self.verticalLayout_2.addWidget(self.marking_vector)
        self.markingVector_tw = QtWidgets.QTableWidget(self.markingGroupBox)
        self.markingVector_tw.setMinimumSize(QtCore.QSize(30, 0))
        self.markingVector_tw.setMaximumSize(QtCore.QSize(120, 16777215))
        self.markingVector_tw.setRowCount(0)
        self.markingVector_tw.setColumnCount(0)
        self.markingVector_tw.setObjectName("markingVector_tw")
        self.markingVector_tw.horizontalHeader().setDefaultSectionSize(30)
        self.markingVector_tw.horizontalHeader().setMinimumSectionSize(30)
        self.markingVector_tw.horizontalHeader().setStretchLastSection(True)
        self.markingVector_tw.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout_2.addWidget(self.markingVector_tw)
        self.horizontalLayout_2.addWidget(self.markingGroupBox)
        self.groupBoxMatrix = QtWidgets.QGroupBox(self.tab_setup)
        self.groupBoxMatrix.setMinimumSize(QtCore.QSize(350, 0))
        self.groupBoxMatrix.setTitle("")
        self.groupBoxMatrix.setObjectName("groupBoxMatrix")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxMatrix)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBoxMatrix)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.incMatrix_tw = QtWidgets.QTableWidget(self.groupBoxMatrix)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.incMatrix_tw.sizePolicy().hasHeightForWidth())
        self.incMatrix_tw.setSizePolicy(sizePolicy)
        self.incMatrix_tw.setMinimumSize(QtCore.QSize(250, 0))
        self.incMatrix_tw.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.incMatrix_tw.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.incMatrix_tw.setAutoScroll(True)
        self.incMatrix_tw.setGridStyle(QtCore.Qt.SolidLine)
        self.incMatrix_tw.setRowCount(0)
        self.incMatrix_tw.setColumnCount(0)
        self.incMatrix_tw.setObjectName("incMatrix_tw")
        self.incMatrix_tw.horizontalHeader().setVisible(True)
        self.incMatrix_tw.horizontalHeader().setCascadingSectionResizes(False)
        self.incMatrix_tw.horizontalHeader().setDefaultSectionSize(30)
        self.incMatrix_tw.horizontalHeader().setMinimumSectionSize(30)
        self.incMatrix_tw.horizontalHeader().setSortIndicatorShown(False)
        self.incMatrix_tw.horizontalHeader().setStretchLastSection(True)
        self.incMatrix_tw.verticalHeader().setDefaultSectionSize(30)
        self.incMatrix_tw.verticalHeader().setMinimumSectionSize(30)
        self.incMatrix_tw.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.incMatrix_tw)
        self.horizontalLayout_2.addWidget(self.groupBoxMatrix)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.tab_setup)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.matrix_array = QtWidgets.QLineEdit(self.tab_setup)
        self.matrix_array.setMinimumSize(QtCore.QSize(500, 40))
        self.matrix_array.setAlignment(QtCore.Qt.AlignCenter)
        self.matrix_array.setObjectName("matrix_array")
        self.verticalLayout_6.addWidget(self.matrix_array)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.tab_setup)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.marking_array = QtWidgets.QLineEdit(self.tab_setup)
        self.marking_array.setMinimumSize(QtCore.QSize(0, 40))
        self.marking_array.setText("")
        self.marking_array.setAlignment(QtCore.Qt.AlignCenter)
        self.marking_array.setObjectName("marking_array")
        self.verticalLayout_7.addWidget(self.marking_array)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.info_label = QtWidgets.QLabel(self.tab_setup)
        self.info_label.setMinimumSize(QtCore.QSize(500, 0))
        self.info_label.setText("")
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setObjectName("info_label")
        self.horizontalLayout_4.addWidget(self.info_label)
        self.stopConnection_pushButton = QtWidgets.QPushButton(self.tab_setup)
        self.stopConnection_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.stopConnection_pushButton.setMaximumSize(QtCore.QSize(9999999, 16777215))
        self.stopConnection_pushButton.setObjectName("stopConnection_pushButton")
        self.horizontalLayout_4.addWidget(self.stopConnection_pushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.setup_tabWidget.addTab(self.tab_setup, "")
        self.tab_petrinet = QtWidgets.QWidget()
        self.tab_petrinet.setObjectName("tab_petrinet")
        self.setup_tabWidget.addTab(self.tab_petrinet, "")
        self.horizontalLayout_3.addWidget(self.setup_tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionopen_pnml = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui/qtGui/images/xml.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionopen_pnml.setIcon(icon)
        self.actionopen_pnml.setObjectName("actionopen_pnml")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionopen_pnml)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.setup_tabWidget.setCurrentIndex(0)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Serial Connection"))
        self.confirmSerialConection_pushButton.setText(_translate("MainWindow", "CONNECT"))
        self.places_label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.transitions_label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.marking_vector.setText(_translate("MainWindow", "Marking Vector"))
        self.label.setText(_translate("MainWindow", "Incidence Matrix Transpose"))
        self.label_4.setText(_translate("MainWindow", "Incidence Matrix Array"))
        self.label_2.setText(_translate("MainWindow", "Marking Array"))
        self.stopConnection_pushButton.setText(_translate("MainWindow", "STOP"))
        self.setup_tabWidget.setTabText(self.setup_tabWidget.indexOf(self.tab_setup), _translate("MainWindow", "PNRD SETUP"))
        self.setup_tabWidget.setTabText(self.setup_tabWidget.indexOf(self.tab_petrinet), _translate("MainWindow", "Petri Net"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionopen_pnml.setText(_translate("MainWindow", "Open PNML file"))
        self.actionopen_pnml.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
