/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.13.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionopen_pnml;
    QAction *actionExit;
    QWidget *centralwidget;
    QHBoxLayout *horizontalLayout_3;
    QTabWidget *setup_tabWidget;
    QWidget *tab_setup;
    QVBoxLayout *verticalLayout_5;
    QHBoxLayout *horizontalLayout_2;
    QVBoxLayout *verticalLayout_4;
    QLabel *label_5;
    QHBoxLayout *horizontalLayout_6;
    QVBoxLayout *bgPnrd_verticalLayout;
    QGroupBox *setupBg_groupBox;
    QVBoxLayout *verticalLayout_8;
    QLabel *label_6;
    QComboBox *comboBox;
    QVBoxLayout *verticalLayout_9;
    QHBoxLayout *horizontalLayout_9;
    QLabel *label_7;
    QLineEdit *lineEdit;
    QLabel *label_3;
    QComboBox *serialConection_comboBox;
    QPushButton *addSerial_pushButton;
    QLabel *setupInfo_label;
    QPushButton *createSetup_pushButton;
    QGroupBox *markingGroupBox;
    QVBoxLayout *verticalLayout_2;
    QLabel *marking_vector;
    QTableWidget *markingVector_tw;
    QGroupBox *groupBoxMatrix;
    QVBoxLayout *verticalLayout;
    QLabel *label;
    QTableWidget *incMatrix_tw;
    QHBoxLayout *horizontalLayout_5;
    QVBoxLayout *verticalLayout_6;
    QLabel *label_4;
    QLineEdit *matrix_array;
    QVBoxLayout *verticalLayout_7;
    QLabel *label_2;
    QLineEdit *marking_array;
    QWidget *tab_petrinet;
    QGroupBox *groupBox_Labels;
    QVBoxLayout *verticalLayout_3;
    QLabel *exception_label;
    QLabel *reader_label;
    QLabel *id_label;
    QLabel *places_label;
    QLabel *transitions_label;
    QPushButton *confirmSerialConection_pushButton;
    QLineEdit *serialConection_lineEdit;
    QWidget *widget;
    QHBoxLayout *horizontalLayout_4;
    QLabel *info_label;
    QPushButton *stopConnection_pushButton;
    QMenuBar *menubar;
    QMenu *menuFile;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(931, 609);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        MainWindow->setMinimumSize(QSize(50, 50));
        MainWindow->setStyleSheet(QString::fromUtf8("QMainWindow{\n"
"	background-color: rgb(55, 60, 85);\n"
"}\n"
"QTabWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:1px solid rgb(221, 216, 216);\n"
"}\n"
"QTabWidget::pane{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:1px solid rgb(221, 216, 216);\n"
"}\n"
"\n"
"#setupBg_groupBox{\n"
"background-color: rgb(243, 243, 243)!important;\n"
"border:1px solid rgb(221, 216, 216);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"	background-color: rgb(238, 238, 236);\n"
"	border:1px solid rgb(221, 216, 216);\n"
"	alignment: center;\n"
"}\n"
"QTabBar::tab {\n"
"    background-color: white;\n"
"	border-color:rgb(186, 189, 182);\n"
"    padding: 5px;\n"
"	margin-bottom:0px;\n"
"	\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	border-color: rgb(136, 138, 133);\n"
"	background-color: rgb(46, 52, 54);\n"
"	color:rgb(255, 255, 255);\n"
"}\n"
"QTableWidget {\n"
"	border:1px  solid rgb(221, 216, 216);\n"
"	\n"
"}\n"
"\n"
"QTableWidget::section {\n"
"	background-color: transparent;\n"
"	border:0px solid transparent"
                        ";\n"
"}\n"
"\n"
"QHeaderView::section,QHeaderView{\n"
"	  background-color: white;\n"
"}\n"
"\n"
"QGroupBox#groupBoxMatrix, QGroupBox#markingGroupBox{\n"
"	background-color: white;\n"
"	border:1px, solid ,rgb(221, 216, 216);\n"
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
"font: 75 12pt \"Courier 10"
                        " Pitch\";\n"
"}\n"
"\n"
"QGroupBox#groupBox_Labels{\n"
"	background-color: white;\n"
"	border:0px ,solid ,rgb(186, 189, 182);\n"
"}\n"
"\n"
"QTabWidget{\n"
"	background-color:rgb(242, 242, 242);\n"
"}\n"
"//rgb(238, 238, 236)"));
        actionopen_pnml = new QAction(MainWindow);
        actionopen_pnml->setObjectName(QString::fromUtf8("actionopen_pnml"));
        QIcon icon;
        icon.addFile(QString::fromUtf8("images/xml.svg"), QSize(), QIcon::Normal, QIcon::Off);
        actionopen_pnml->setIcon(icon);
        actionExit = new QAction(MainWindow);
        actionExit->setObjectName(QString::fromUtf8("actionExit"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        horizontalLayout_3 = new QHBoxLayout(centralwidget);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        setup_tabWidget = new QTabWidget(centralwidget);
        setup_tabWidget->setObjectName(QString::fromUtf8("setup_tabWidget"));
        setup_tabWidget->setTabPosition(QTabWidget::South);
        setup_tabWidget->setTabShape(QTabWidget::Rounded);
        tab_setup = new QWidget();
        tab_setup->setObjectName(QString::fromUtf8("tab_setup"));
        verticalLayout_5 = new QVBoxLayout(tab_setup);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        label_5 = new QLabel(tab_setup);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setMaximumSize(QSize(230, 120));
        label_5->setPixmap(QPixmap(QString::fromUtf8("images/femec.jpeg")));
        label_5->setScaledContents(true);
        label_5->setAlignment(Qt::AlignCenter);

        verticalLayout_4->addWidget(label_5);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setSpacing(6);
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        horizontalLayout_6->setContentsMargins(0, 0, -1, -1);
        bgPnrd_verticalLayout = new QVBoxLayout();
        bgPnrd_verticalLayout->setObjectName(QString::fromUtf8("bgPnrd_verticalLayout"));
        bgPnrd_verticalLayout->setContentsMargins(0, 0, 0, 0);
        setupBg_groupBox = new QGroupBox(tab_setup);
        setupBg_groupBox->setObjectName(QString::fromUtf8("setupBg_groupBox"));
        setupBg_groupBox->setAlignment(Qt::AlignCenter);
        verticalLayout_8 = new QVBoxLayout(setupBg_groupBox);
        verticalLayout_8->setObjectName(QString::fromUtf8("verticalLayout_8"));
        label_6 = new QLabel(setupBg_groupBox);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setAlignment(Qt::AlignCenter);

        verticalLayout_8->addWidget(label_6);

        comboBox = new QComboBox(setupBg_groupBox);
        comboBox->addItem(QString());
        comboBox->addItem(QString());
        comboBox->setObjectName(QString::fromUtf8("comboBox"));
        comboBox->setMinimumSize(QSize(0, 60));
        comboBox->setMaximumSize(QSize(100, 16777215));
        QFont font;
        font.setKerning(true);
        comboBox->setFont(font);
        comboBox->setLayoutDirection(Qt::LeftToRight);

        verticalLayout_8->addWidget(comboBox);


        bgPnrd_verticalLayout->addWidget(setupBg_groupBox);


        horizontalLayout_6->addLayout(bgPnrd_verticalLayout);

        verticalLayout_9 = new QVBoxLayout();
        verticalLayout_9->setObjectName(QString::fromUtf8("verticalLayout_9"));
        verticalLayout_9->setContentsMargins(-1, 0, -1, -1);
        horizontalLayout_9 = new QHBoxLayout();
        horizontalLayout_9->setObjectName(QString::fromUtf8("horizontalLayout_9"));
        horizontalLayout_9->setContentsMargins(-1, 0, -1, -1);
        label_7 = new QLabel(tab_setup);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        horizontalLayout_9->addWidget(label_7);

        lineEdit = new QLineEdit(tab_setup);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));

        horizontalLayout_9->addWidget(lineEdit);


        verticalLayout_9->addLayout(horizontalLayout_9);

        label_3 = new QLabel(tab_setup);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setMaximumSize(QSize(16777215, 30));
        label_3->setAlignment(Qt::AlignCenter);

        verticalLayout_9->addWidget(label_3);

        serialConection_comboBox = new QComboBox(tab_setup);
        serialConection_comboBox->setObjectName(QString::fromUtf8("serialConection_comboBox"));

        verticalLayout_9->addWidget(serialConection_comboBox);

        addSerial_pushButton = new QPushButton(tab_setup);
        addSerial_pushButton->setObjectName(QString::fromUtf8("addSerial_pushButton"));
        addSerial_pushButton->setMinimumSize(QSize(0, 40));

        verticalLayout_9->addWidget(addSerial_pushButton);


        horizontalLayout_6->addLayout(verticalLayout_9);


        verticalLayout_4->addLayout(horizontalLayout_6);

        setupInfo_label = new QLabel(tab_setup);
        setupInfo_label->setObjectName(QString::fromUtf8("setupInfo_label"));

        verticalLayout_4->addWidget(setupInfo_label);

        createSetup_pushButton = new QPushButton(tab_setup);
        createSetup_pushButton->setObjectName(QString::fromUtf8("createSetup_pushButton"));
        createSetup_pushButton->setMinimumSize(QSize(0, 50));

        verticalLayout_4->addWidget(createSetup_pushButton);


        horizontalLayout_2->addLayout(verticalLayout_4);

        markingGroupBox = new QGroupBox(tab_setup);
        markingGroupBox->setObjectName(QString::fromUtf8("markingGroupBox"));
        markingGroupBox->setMinimumSize(QSize(100, 0));
        markingGroupBox->setMaximumSize(QSize(120, 16777215));
        markingGroupBox->setLayoutDirection(Qt::LeftToRight);
        markingGroupBox->setAlignment(Qt::AlignCenter);
        verticalLayout_2 = new QVBoxLayout(markingGroupBox);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        marking_vector = new QLabel(markingGroupBox);
        marking_vector->setObjectName(QString::fromUtf8("marking_vector"));
        marking_vector->setMinimumSize(QSize(30, 30));
        marking_vector->setMaximumSize(QSize(120, 16777215));
        marking_vector->setLayoutDirection(Qt::LeftToRight);
        marking_vector->setAlignment(Qt::AlignCenter);

        verticalLayout_2->addWidget(marking_vector);

        markingVector_tw = new QTableWidget(markingGroupBox);
        markingVector_tw->setObjectName(QString::fromUtf8("markingVector_tw"));
        markingVector_tw->setMinimumSize(QSize(30, 0));
        markingVector_tw->setMaximumSize(QSize(120, 16777215));
        markingVector_tw->setRowCount(0);
        markingVector_tw->setColumnCount(0);
        markingVector_tw->horizontalHeader()->setMinimumSectionSize(30);
        markingVector_tw->horizontalHeader()->setDefaultSectionSize(30);
        markingVector_tw->horizontalHeader()->setStretchLastSection(true);
        markingVector_tw->verticalHeader()->setMinimumSectionSize(30);

        verticalLayout_2->addWidget(markingVector_tw);


        horizontalLayout_2->addWidget(markingGroupBox);

        groupBoxMatrix = new QGroupBox(tab_setup);
        groupBoxMatrix->setObjectName(QString::fromUtf8("groupBoxMatrix"));
        groupBoxMatrix->setMinimumSize(QSize(350, 0));
        verticalLayout = new QVBoxLayout(groupBoxMatrix);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        label = new QLabel(groupBoxMatrix);
        label->setObjectName(QString::fromUtf8("label"));
        label->setMaximumSize(QSize(16777215, 30));
        label->setAlignment(Qt::AlignCenter);

        verticalLayout->addWidget(label);

        incMatrix_tw = new QTableWidget(groupBoxMatrix);
        incMatrix_tw->setObjectName(QString::fromUtf8("incMatrix_tw"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(incMatrix_tw->sizePolicy().hasHeightForWidth());
        incMatrix_tw->setSizePolicy(sizePolicy1);
        incMatrix_tw->setMinimumSize(QSize(250, 0));
        incMatrix_tw->setMaximumSize(QSize(16777215, 16777215));
        incMatrix_tw->setSizeAdjustPolicy(QAbstractScrollArea::AdjustToContentsOnFirstShow);
        incMatrix_tw->setAutoScroll(true);
        incMatrix_tw->setGridStyle(Qt::SolidLine);
        incMatrix_tw->setRowCount(0);
        incMatrix_tw->setColumnCount(0);
        incMatrix_tw->horizontalHeader()->setVisible(true);
        incMatrix_tw->horizontalHeader()->setCascadingSectionResizes(false);
        incMatrix_tw->horizontalHeader()->setMinimumSectionSize(30);
        incMatrix_tw->horizontalHeader()->setDefaultSectionSize(30);
        incMatrix_tw->horizontalHeader()->setProperty("showSortIndicator", QVariant(false));
        incMatrix_tw->horizontalHeader()->setStretchLastSection(true);
        incMatrix_tw->verticalHeader()->setMinimumSectionSize(30);
        incMatrix_tw->verticalHeader()->setDefaultSectionSize(30);
        incMatrix_tw->verticalHeader()->setStretchLastSection(false);

        verticalLayout->addWidget(incMatrix_tw);


        horizontalLayout_2->addWidget(groupBoxMatrix);


        verticalLayout_5->addLayout(horizontalLayout_2);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        horizontalLayout_5->setContentsMargins(-1, 0, -1, -1);
        verticalLayout_6 = new QVBoxLayout();
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        verticalLayout_6->setContentsMargins(-1, 0, -1, -1);
        label_4 = new QLabel(tab_setup);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setLayoutDirection(Qt::LeftToRight);
        label_4->setAlignment(Qt::AlignCenter);

        verticalLayout_6->addWidget(label_4);

        matrix_array = new QLineEdit(tab_setup);
        matrix_array->setObjectName(QString::fromUtf8("matrix_array"));
        matrix_array->setMinimumSize(QSize(500, 40));
        matrix_array->setAlignment(Qt::AlignCenter);

        verticalLayout_6->addWidget(matrix_array);


        horizontalLayout_5->addLayout(verticalLayout_6);

        verticalLayout_7 = new QVBoxLayout();
        verticalLayout_7->setObjectName(QString::fromUtf8("verticalLayout_7"));
        verticalLayout_7->setContentsMargins(0, 0, -1, -1);
        label_2 = new QLabel(tab_setup);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setAlignment(Qt::AlignCenter);

        verticalLayout_7->addWidget(label_2);

        marking_array = new QLineEdit(tab_setup);
        marking_array->setObjectName(QString::fromUtf8("marking_array"));
        marking_array->setMinimumSize(QSize(0, 40));
        marking_array->setAlignment(Qt::AlignCenter);

        verticalLayout_7->addWidget(marking_array);


        horizontalLayout_5->addLayout(verticalLayout_7);


        verticalLayout_5->addLayout(horizontalLayout_5);

        setup_tabWidget->addTab(tab_setup, QString());
        tab_petrinet = new QWidget();
        tab_petrinet->setObjectName(QString::fromUtf8("tab_petrinet"));
        groupBox_Labels = new QGroupBox(tab_petrinet);
        groupBox_Labels->setObjectName(QString::fromUtf8("groupBox_Labels"));
        groupBox_Labels->setGeometry(QRect(10, 210, 250, 150));
        groupBox_Labels->setMaximumSize(QSize(250, 150));
        verticalLayout_3 = new QVBoxLayout(groupBox_Labels);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        exception_label = new QLabel(groupBox_Labels);
        exception_label->setObjectName(QString::fromUtf8("exception_label"));

        verticalLayout_3->addWidget(exception_label);

        reader_label = new QLabel(groupBox_Labels);
        reader_label->setObjectName(QString::fromUtf8("reader_label"));

        verticalLayout_3->addWidget(reader_label);

        id_label = new QLabel(groupBox_Labels);
        id_label->setObjectName(QString::fromUtf8("id_label"));

        verticalLayout_3->addWidget(id_label);

        places_label = new QLabel(groupBox_Labels);
        places_label->setObjectName(QString::fromUtf8("places_label"));
        places_label->setMaximumSize(QSize(16777215, 16777215));
        places_label->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        verticalLayout_3->addWidget(places_label);

        transitions_label = new QLabel(groupBox_Labels);
        transitions_label->setObjectName(QString::fromUtf8("transitions_label"));
        transitions_label->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        verticalLayout_3->addWidget(transitions_label);

        confirmSerialConection_pushButton = new QPushButton(tab_petrinet);
        confirmSerialConection_pushButton->setObjectName(QString::fromUtf8("confirmSerialConection_pushButton"));
        confirmSerialConection_pushButton->setGeometry(QRect(10, 370, 251, 50));
        confirmSerialConection_pushButton->setMinimumSize(QSize(0, 50));
        confirmSerialConection_pushButton->setMaximumSize(QSize(16777215, 16777215));
        serialConection_lineEdit = new QLineEdit(tab_petrinet);
        serialConection_lineEdit->setObjectName(QString::fromUtf8("serialConection_lineEdit"));
        serialConection_lineEdit->setGeometry(QRect(10, 160, 251, 30));
        serialConection_lineEdit->setMinimumSize(QSize(0, 30));
        serialConection_lineEdit->setMaximumSize(QSize(16777215, 16777215));
        serialConection_lineEdit->setAlignment(Qt::AlignCenter);
        widget = new QWidget(tab_petrinet);
        widget->setObjectName(QString::fromUtf8("widget"));
        widget->setGeometry(QRect(430, 390, 151, 41));
        horizontalLayout_4 = new QHBoxLayout(widget);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        horizontalLayout_4->setContentsMargins(0, 0, 0, 0);
        info_label = new QLabel(widget);
        info_label->setObjectName(QString::fromUtf8("info_label"));
        info_label->setMinimumSize(QSize(500, 0));
        info_label->setAlignment(Qt::AlignCenter);

        horizontalLayout_4->addWidget(info_label);

        stopConnection_pushButton = new QPushButton(widget);
        stopConnection_pushButton->setObjectName(QString::fromUtf8("stopConnection_pushButton"));
        stopConnection_pushButton->setMinimumSize(QSize(0, 30));
        stopConnection_pushButton->setMaximumSize(QSize(9999999, 16777215));

        horizontalLayout_4->addWidget(stopConnection_pushButton);

        setup_tabWidget->addTab(tab_petrinet, QString());

        horizontalLayout_3->addWidget(setup_tabWidget);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 931, 24));
        menuFile = new QMenu(menubar);
        menuFile->setObjectName(QString::fromUtf8("menuFile"));
        MainWindow->setMenuBar(menubar);

        menubar->addAction(menuFile->menuAction());
        menuFile->addSeparator();
        menuFile->addAction(actionopen_pnml);
        menuFile->addSeparator();
        menuFile->addAction(actionExit);

        retranslateUi(MainWindow);
        QObject::connect(actionExit, SIGNAL(triggered()), MainWindow, SLOT(close()));

        setup_tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        actionopen_pnml->setText(QCoreApplication::translate("MainWindow", "Open PNML file", nullptr));
#if QT_CONFIG(shortcut)
        actionopen_pnml->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+O", nullptr));
#endif // QT_CONFIG(shortcut)
        actionExit->setText(QCoreApplication::translate("MainWindow", "Exit", nullptr));
#if QT_CONFIG(shortcut)
        actionExit->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+X", nullptr));
#endif // QT_CONFIG(shortcut)
        label_5->setText(QString());
        setupBg_groupBox->setTitle(QString());
        label_6->setText(QCoreApplication::translate("MainWindow", "Setup Type", nullptr));
        comboBox->setItemText(0, QCoreApplication::translate("MainWindow", "PNRD", nullptr));
        comboBox->setItemText(1, QCoreApplication::translate("MainWindow", "iPNRD", nullptr));

        label_7->setText(QCoreApplication::translate("MainWindow", "Reader Name: ", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "Serial COM", nullptr));
        addSerial_pushButton->setText(QCoreApplication::translate("MainWindow", "Add", nullptr));
        setupInfo_label->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>", nullptr));
        createSetup_pushButton->setText(QCoreApplication::translate("MainWindow", "CREATE SETUP FILE", nullptr));
        markingGroupBox->setTitle(QString());
        marking_vector->setText(QCoreApplication::translate("MainWindow", "Marking Vector", nullptr));
        groupBoxMatrix->setTitle(QString());
        label->setText(QCoreApplication::translate("MainWindow", "Incidence Matrix Transpose", nullptr));
        label_4->setText(QCoreApplication::translate("MainWindow", "Incidence Matrix Array", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "Marking Array", nullptr));
        marking_array->setText(QString());
        setup_tabWidget->setTabText(setup_tabWidget->indexOf(tab_setup), QCoreApplication::translate("MainWindow", "SETUP", nullptr));
#if QT_CONFIG(whatsthis)
        setup_tabWidget->setTabWhatsThis(setup_tabWidget->indexOf(tab_setup), QCoreApplication::translate("MainWindow", "Informa\303\247\303\265es da PNRD", nullptr));
#endif // QT_CONFIG(whatsthis)
        groupBox_Labels->setTitle(QString());
        exception_label->setText(QString());
        reader_label->setText(QString());
        id_label->setText(QString());
        places_label->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", nullptr));
        transitions_label->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", nullptr));
        confirmSerialConection_pushButton->setText(QCoreApplication::translate("MainWindow", "SAVE SETUP", nullptr));
        info_label->setText(QString());
        stopConnection_pushButton->setText(QCoreApplication::translate("MainWindow", "STOP", nullptr));
        setup_tabWidget->setTabText(setup_tabWidget->indexOf(tab_petrinet), QCoreApplication::translate("MainWindow", "RUNTIME", nullptr));
        menuFile->setTitle(QCoreApplication::translate("MainWindow", "File", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
