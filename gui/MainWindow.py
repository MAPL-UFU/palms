# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/qtGui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

#-------------------------------------------------------------
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS,
        # and places our data files in a folder relative to that temp
        # folder named as specified in the datas tuple in the spec file
        base_path = os.path.join(sys._MEIPASS, 'data')
    except Exception:
        # sys._MEIPASS is not defined, so use the original path
        base_path = 'C:'

    return os.path.join(base_path, relative_path)

#--------------------------------------------------------------------
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 609)
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
"#setupBg_groupBox{\n"
"background-color: rgb(243, 243, 243)!important;\n"
"border:1px solid rgb(221, 216, 216);\n"
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
"QGroupBox#groupBoxMatrix, QGroupBox#markingGroupBox,QGroupBox#groupBoxMatrix2, QGroupBox#markingGroupBox2{\n"
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
"#setupInfo_label{\n"
"background-color: white;\n"
"color:rgb(60, 167, 61);\n"
"font: 75 12pt \"Courier 10 Pitch\";\n"
"}\n"
"#palmsType_label{color:rgb(2, 160, 200);\n"
"font: 75 14pt \"Courier 10 Pitch\";}\n"
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
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
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
        self.label_5.setPixmap(QtGui.QPixmap(resource_path("femec.jpeg")))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bgPnrd_verticalLayout = QtWidgets.QVBoxLayout()
        self.bgPnrd_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bgPnrd_verticalLayout.setObjectName("bgPnrd_verticalLayout")
        self.setupBg_groupBox = QtWidgets.QGroupBox(self.tab_setup)
        self.setupBg_groupBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.setupBg_groupBox.setTitle("")
        self.setupBg_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.setupBg_groupBox.setObjectName("setupBg_groupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.setupBg_groupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.setupBg_groupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.setupPalms_comboBox = QtWidgets.QComboBox(self.setupBg_groupBox)
        self.setupPalms_comboBox.setMinimumSize(QtCore.QSize(0, 60))
        self.setupPalms_comboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.setupPalms_comboBox.setFont(font)
        self.setupPalms_comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setupPalms_comboBox.setObjectName("setupPalms_comboBox")
        self.setupPalms_comboBox.addItem("")
        self.setupPalms_comboBox.addItem("")
        self.verticalLayout_8.addWidget(self.setupPalms_comboBox)
        self.bgPnrd_verticalLayout.addWidget(self.setupBg_groupBox)
        self.horizontalLayout_6.addLayout(self.bgPnrd_verticalLayout)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.tab_setup)
        self.label_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.readerName_lineEdit = QtWidgets.QLineEdit(self.tab_setup)
        self.readerName_lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.readerName_lineEdit.setObjectName("readerName_lineEdit")
        self.horizontalLayout_9.addWidget(self.readerName_lineEdit)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.tab_setup)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.qtdTotalTansitions_label = QtWidgets.QLabel(self.tab_setup)
        self.qtdTotalTansitions_label.setText("")
        self.qtdTotalTansitions_label.setObjectName("qtdTotalTansitions_label")
        self.horizontalLayout_10.addWidget(self.qtdTotalTansitions_label)
        self.nAntennas_spinBox = QtWidgets.QSpinBox(self.tab_setup)
        self.nAntennas_spinBox.setObjectName("nAntennas_spinBox")
        self.horizontalLayout_10.addWidget(self.nAntennas_spinBox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.label_3 = QtWidgets.QLabel(self.tab_setup)
        self.label_3.setMaximumSize(QtCore.QSize(400, 30))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.IP_lineEdit = QtWidgets.QLineEdit(self.tab_setup)
        self.IP_lineEdit.setObjectName("IP_lineEdit")
        self.verticalLayout_9.addWidget(self.IP_lineEdit)
        self.addIP_pushButton = QtWidgets.QPushButton(self.tab_setup)
        self.addIP_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.addIP_pushButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.addIP_pushButton.setObjectName("addIP_pushButton")
        self.verticalLayout_9.addWidget(self.addIP_pushButton)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.setupInfo_label = QtWidgets.QLabel(self.tab_setup)
        self.setupInfo_label.setMaximumSize(QtCore.QSize(500, 16777215))
        self.setupInfo_label.setObjectName("setupInfo_label")
        self.verticalLayout_4.addWidget(self.setupInfo_label)
        self.createSetup_pushButton = QtWidgets.QPushButton(self.tab_setup)
        self.createSetup_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.createSetup_pushButton.setMaximumSize(QtCore.QSize(500, 16777215))
        self.createSetup_pushButton.setObjectName("createSetup_pushButton")
        self.verticalLayout_4.addWidget(self.createSetup_pushButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.markingGroupBox = QtWidgets.QGroupBox(self.tab_setup)
        self.markingGroupBox.setMinimumSize(QtCore.QSize(100, 0))
        self.markingGroupBox.setMaximumSize(QtCore.QSize(130, 16777215))
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
        self.incMatrix_tw.horizontalHeader().setVisible(False)
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
        self.setup_tabWidget.addTab(self.tab_setup, "")
        self.tab_petrinet = QtWidgets.QWidget()
        self.tab_petrinet.setObjectName("tab_petrinet")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_petrinet)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.groupBox_Labels = QtWidgets.QGroupBox(self.tab_petrinet)
        self.groupBox_Labels.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_Labels.setMaximumSize(QtCore.QSize(9999999, 16777215))
        self.groupBox_Labels.setTitle("")
        self.groupBox_Labels.setObjectName("groupBox_Labels")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_Labels)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.palmsType_label = QtWidgets.QLabel(self.groupBox_Labels)
        self.palmsType_label.setMinimumSize(QtCore.QSize(0, 30))
        self.palmsType_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.palmsType_label.setFont(font)
        self.palmsType_label.setText("")
        self.palmsType_label.setAlignment(QtCore.Qt.AlignCenter)
        self.palmsType_label.setObjectName("palmsType_label")
        self.verticalLayout_3.addWidget(self.palmsType_label)
        self.qtdReader_label = QtWidgets.QLabel(self.groupBox_Labels)
        self.qtdReader_label.setMinimumSize(QtCore.QSize(0, 20))
        self.qtdReader_label.setText("")
        self.qtdReader_label.setObjectName("qtdReader_label")
        self.verticalLayout_3.addWidget(self.qtdReader_label)
        self.readerList_label = QtWidgets.QLabel(self.groupBox_Labels)
        self.readerList_label.setObjectName("readerList_label")
        self.verticalLayout_3.addWidget(self.readerList_label)
        self.exception_label = QtWidgets.QLabel(self.groupBox_Labels)
        self.exception_label.setMinimumSize(QtCore.QSize(0, 20))
        self.exception_label.setText("")
        self.exception_label.setObjectName("exception_label")
        self.verticalLayout_3.addWidget(self.exception_label)
        self.reader_label = QtWidgets.QLabel(self.groupBox_Labels)
        self.reader_label.setMinimumSize(QtCore.QSize(0, 20))
        self.reader_label.setText("")
        self.reader_label.setObjectName("reader_label")
        self.verticalLayout_3.addWidget(self.reader_label)
        self.id_label = QtWidgets.QLabel(self.groupBox_Labels)
        self.id_label.setMinimumSize(QtCore.QSize(0, 20))
        self.id_label.setText("")
        self.id_label.setObjectName("id_label")
        self.verticalLayout_3.addWidget(self.id_label)
        self.places_label = QtWidgets.QLabel(self.groupBox_Labels)
        self.places_label.setMinimumSize(QtCore.QSize(0, 20))
        self.places_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.places_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.places_label.setObjectName("places_label")
        self.verticalLayout_3.addWidget(self.places_label)
        self.transitions_label = QtWidgets.QLabel(self.groupBox_Labels)
        self.transitions_label.setMinimumSize(QtCore.QSize(0, 20))
        self.transitions_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.transitions_label.setObjectName("transitions_label")
        self.verticalLayout_3.addWidget(self.transitions_label)
        self.verticalLayout_15.addWidget(self.groupBox_Labels)
        self.horizontalLayout.addLayout(self.verticalLayout_15)
        self.markingGroupBox2 = QtWidgets.QGroupBox(self.tab_petrinet)
        self.markingGroupBox2.setMinimumSize(QtCore.QSize(100, 0))
        self.markingGroupBox2.setMaximumSize(QtCore.QSize(130, 16777215))
        self.markingGroupBox2.setTitle("")
        self.markingGroupBox2.setObjectName("markingGroupBox2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.markingGroupBox2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_9 = QtWidgets.QLabel(self.markingGroupBox2)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_13.addWidget(self.label_9)
        self.markingVector2_tw = QtWidgets.QTableWidget(self.markingGroupBox2)
        self.markingVector2_tw.setMaximumSize(QtCore.QSize(120, 16777215))
        self.markingVector2_tw.setObjectName("markingVector2_tw")
        self.markingVector2_tw.setColumnCount(0)
        self.markingVector2_tw.setRowCount(0)
        self.markingVector2_tw.horizontalHeader().setDefaultSectionSize(30)
        self.markingVector2_tw.horizontalHeader().setMinimumSectionSize(30)
        self.markingVector2_tw.horizontalHeader().setStretchLastSection(True)
        self.markingVector2_tw.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout_13.addWidget(self.markingVector2_tw)
        self.horizontalLayout.addWidget(self.markingGroupBox2)
        self.groupBoxMatrix2 = QtWidgets.QGroupBox(self.tab_petrinet)
        self.groupBoxMatrix2.setMinimumSize(QtCore.QSize(350, 0))
        self.groupBoxMatrix2.setTitle("")
        self.groupBoxMatrix2.setObjectName("groupBoxMatrix2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBoxMatrix2)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_10 = QtWidgets.QLabel(self.groupBoxMatrix2)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_14.addWidget(self.label_10)
        self.incMatrix2_tw = QtWidgets.QTableWidget(self.groupBoxMatrix2)
        self.incMatrix2_tw.setMinimumSize(QtCore.QSize(250, 0))
        self.incMatrix2_tw.setObjectName("incMatrix2_tw")
        self.incMatrix2_tw.setColumnCount(0)
        self.incMatrix2_tw.setRowCount(0)
        self.incMatrix2_tw.horizontalHeader().setDefaultSectionSize(30)
        self.incMatrix2_tw.horizontalHeader().setMinimumSectionSize(30)
        self.incMatrix2_tw.horizontalHeader().setStretchLastSection(True)
        self.incMatrix2_tw.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout_14.addWidget(self.incMatrix2_tw)
        self.horizontalLayout.addWidget(self.groupBoxMatrix2)
        self.verticalLayout_10.addLayout(self.horizontalLayout)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.info_label = QtWidgets.QLabel(self.tab_petrinet)
        self.info_label.setMinimumSize(QtCore.QSize(500, 0))
        self.info_label.setText("")
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setObjectName("info_label")
        self.verticalLayout_12.addWidget(self.info_label)
        self.confirmSerialConection_pushButton = QtWidgets.QPushButton(self.tab_petrinet)
        self.confirmSerialConection_pushButton.setObjectName("confirmSerialConection_pushButton")
        self.verticalLayout_12.addWidget(self.confirmSerialConection_pushButton)
        self.stopConnection_pushButton = QtWidgets.QPushButton(self.tab_petrinet)
        self.stopConnection_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.stopConnection_pushButton.setMaximumSize(QtCore.QSize(9999999, 16777215))
        self.stopConnection_pushButton.setObjectName("stopConnection_pushButton")
        self.verticalLayout_12.addWidget(self.stopConnection_pushButton)
        self.verticalLayout_10.addLayout(self.verticalLayout_12)
        self.setup_tabWidget.addTab(self.tab_petrinet, "")
        self.verticalLayout_11.addWidget(self.setup_tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionopen_pnml = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("xml.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionopen_pnml.setIcon(icon)
        self.actionopen_pnml.setObjectName("actionopen_pnml")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen_Setup_File_palms = QtWidgets.QAction(MainWindow)
        self.actionOpen_Setup_File_palms.setObjectName("actionOpen_Setup_File_palms")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionopen_pnml)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_Setup_File_palms)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.setup_tabWidget.setCurrentIndex(1)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Setup Type"))
        self.setupPalms_comboBox.setItemText(0, _translate("MainWindow", "PNRD"))
        self.setupPalms_comboBox.setItemText(1, _translate("MainWindow", "iPNRD"))
        self.label_7.setText(_translate("MainWindow", "Reader Name: "))
        self.label_8.setText(_translate("MainWindow", "Number of Antennas"))
        self.label_3.setText(_translate("MainWindow", "ESP32 IP Address"))
        self.IP_lineEdit.setInputMask(_translate("MainWindow", "000.000.000.000"))
        self.IP_lineEdit.setText(_translate("MainWindow", "..."))
        self.addIP_pushButton.setText(_translate("MainWindow", "Add"))
        self.setupInfo_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.createSetup_pushButton.setText(_translate("MainWindow", "CREATE SETUP FILE"))
        self.marking_vector.setText(_translate("MainWindow", "Marking Vector"))
        self.label.setText(_translate("MainWindow", "Incidence Matrix"))
        self.label_4.setText(_translate("MainWindow", "Incidence Matrix Transpose Array"))
        self.label_2.setText(_translate("MainWindow", "Marking Array"))
        self.setup_tabWidget.setTabText(self.setup_tabWidget.indexOf(self.tab_setup), _translate("MainWindow", "SETUP"))
        self.readerList_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.places_label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.transitions_label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Marking Vector"))
        self.label_10.setText(_translate("MainWindow", "Incidence Matrix"))
        self.confirmSerialConection_pushButton.setText(_translate("MainWindow", "CONNECT"))
        self.stopConnection_pushButton.setText(_translate("MainWindow", "STOP"))
        self.setup_tabWidget.setTabText(self.setup_tabWidget.indexOf(self.tab_petrinet), _translate("MainWindow", "RUNTIME"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionopen_pnml.setText(_translate("MainWindow", "Open PNML file"))
        self.actionopen_pnml.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionOpen_Setup_File_palms.setText(_translate("MainWindow", "Open Setup File (*.palms)"))
        self.actionOpen_Setup_File_palms.setShortcut(_translate("MainWindow", "Ctrl+F"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
