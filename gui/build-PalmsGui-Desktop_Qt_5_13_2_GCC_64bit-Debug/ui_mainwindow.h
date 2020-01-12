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
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionopen_pnml;
    QWidget *centralwidget;
    QGroupBox *groupBoxMatrix;
    QVBoxLayout *verticalLayout;
    QLabel *label;
    QTableWidget *incMatrix_tw;
    QGroupBox *markingGroupBox;
    QVBoxLayout *verticalLayout_2;
    QLabel *marking_vector;
    QTableWidget *markingVector_tw;
    QLineEdit *serialConection_lineEdit;
    QLabel *label_3;
    QPushButton *confirmSerialConection_pushButton;
    QLabel *label_4;
    QLineEdit *matrix_array;
    QLabel *label_2;
    QLineEdit *marking_array;
    QGroupBox *groupBox_Labels;
    QVBoxLayout *verticalLayout_3;
    QLabel *places_label;
    QLabel *transitions_label;
    QLabel *label_5;
    QMenuBar *menubar;
    QMenu *menuFile;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(800, 600);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        MainWindow->setMinimumSize(QSize(50, 50));
        MainWindow->setStyleSheet(QString::fromUtf8("QTableWidget::section {\n"
"	background-color: transparent;\n"
"	border:0px solid transparent\n"
"}\n"
"\n"
"QHeaderView::section,QHeaderView{\n"
"	  background-color: white;\n"
"}\n"
"QMainWindow{\n"
"	background-color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"QGroupBox#groupBoxMatrix, QGroupBox#markingGroupBox{\n"
"	background-color: white;\n"
"	border:1px solid rgb(186, 189, 182);\n"
"}\n"
"QHeaderView::section:horizontal,QHeaderView::section:vertical\n"
"{\n"
"    background-color: white;\n"
"}\n"
"#places_label{color:rgb(48, 140, 198);\n"
"font: 75 14pt \"Courier 10 Pitch\";}\n"
"#transitions_label{color:rgb(60, 167, 61);\n"
"font: 75 14pt \"Courier 10 Pitch\";}\n"
"\n"
"QGroupBox#groupBox_Labels{\n"
"	background-color: white;\n"
"	border:0px solid rgb(186, 189, 182);\n"
"}"));
        actionopen_pnml = new QAction(MainWindow);
        actionopen_pnml->setObjectName(QString::fromUtf8("actionopen_pnml"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        groupBoxMatrix = new QGroupBox(centralwidget);
        groupBoxMatrix->setObjectName(QString::fromUtf8("groupBoxMatrix"));
        groupBoxMatrix->setGeometry(QRect(350, 30, 441, 381));
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
        incMatrix_tw->horizontalHeader()->setStretchLastSection(false);
        incMatrix_tw->verticalHeader()->setMinimumSectionSize(30);
        incMatrix_tw->verticalHeader()->setDefaultSectionSize(30);
        incMatrix_tw->verticalHeader()->setStretchLastSection(false);

        verticalLayout->addWidget(incMatrix_tw);

        markingGroupBox = new QGroupBox(centralwidget);
        markingGroupBox->setObjectName(QString::fromUtf8("markingGroupBox"));
        markingGroupBox->setGeometry(QRect(210, 30, 131, 381));
        verticalLayout_2 = new QVBoxLayout(markingGroupBox);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        marking_vector = new QLabel(markingGroupBox);
        marking_vector->setObjectName(QString::fromUtf8("marking_vector"));
        marking_vector->setMinimumSize(QSize(30, 30));
        marking_vector->setMaximumSize(QSize(120, 16777215));
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
        markingVector_tw->verticalHeader()->setMinimumSectionSize(30);

        verticalLayout_2->addWidget(markingVector_tw);

        serialConection_lineEdit = new QLineEdit(centralwidget);
        serialConection_lineEdit->setObjectName(QString::fromUtf8("serialConection_lineEdit"));
        serialConection_lineEdit->setGeometry(QRect(10, 80, 191, 51));
        label_3 = new QLabel(centralwidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(16, 50, 181, 20));
        label_3->setAlignment(Qt::AlignCenter);
        confirmSerialConection_pushButton = new QPushButton(centralwidget);
        confirmSerialConection_pushButton->setObjectName(QString::fromUtf8("confirmSerialConection_pushButton"));
        confirmSerialConection_pushButton->setGeometry(QRect(10, 140, 191, 51));
        label_4 = new QLabel(centralwidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(30, 420, 741, 20));
        label_4->setLayoutDirection(Qt::LeftToRight);
        label_4->setAlignment(Qt::AlignCenter);
        matrix_array = new QLineEdit(centralwidget);
        matrix_array->setObjectName(QString::fromUtf8("matrix_array"));
        matrix_array->setGeometry(QRect(10, 440, 781, 41));
        matrix_array->setAlignment(Qt::AlignCenter);
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(30, 490, 741, 20));
        label_2->setAlignment(Qt::AlignCenter);
        marking_array = new QLineEdit(centralwidget);
        marking_array->setObjectName(QString::fromUtf8("marking_array"));
        marking_array->setGeometry(QRect(10, 510, 781, 41));
        marking_array->setAlignment(Qt::AlignCenter);
        groupBox_Labels = new QGroupBox(centralwidget);
        groupBox_Labels->setObjectName(QString::fromUtf8("groupBox_Labels"));
        groupBox_Labels->setGeometry(QRect(10, 320, 191, 91));
        verticalLayout_3 = new QVBoxLayout(groupBox_Labels);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        places_label = new QLabel(groupBox_Labels);
        places_label->setObjectName(QString::fromUtf8("places_label"));
        places_label->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        verticalLayout_3->addWidget(places_label);

        transitions_label = new QLabel(groupBox_Labels);
        transitions_label->setObjectName(QString::fromUtf8("transitions_label"));
        transitions_label->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        verticalLayout_3->addWidget(transitions_label);

        label_5 = new QLabel(centralwidget);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(20, 0, 181, 41));
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 800, 24));
        menuFile = new QMenu(menubar);
        menuFile->setObjectName(QString::fromUtf8("menuFile"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuFile->menuAction());
        menuFile->addSeparator();
        menuFile->addAction(actionopen_pnml);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        actionopen_pnml->setText(QCoreApplication::translate("MainWindow", "Open PNML file", nullptr));
#if QT_CONFIG(shortcut)
        actionopen_pnml->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+O", nullptr));
#endif // QT_CONFIG(shortcut)
        groupBoxMatrix->setTitle(QString());
        label->setText(QCoreApplication::translate("MainWindow", "Incidence Matrix Tranpose", nullptr));
        markingGroupBox->setTitle(QString());
        marking_vector->setText(QCoreApplication::translate("MainWindow", "Marking Vector", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "Serial Connection", nullptr));
        confirmSerialConection_pushButton->setText(QCoreApplication::translate("MainWindow", "Confim", nullptr));
        label_4->setText(QCoreApplication::translate("MainWindow", "Incidence Matrix Array", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "Marking Array", nullptr));
        marking_array->setText(QString());
        groupBox_Labels->setTitle(QString());
        places_label->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", nullptr));
        transitions_label->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", nullptr));
        label_5->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p><a href=\"data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxAPEBAQDxQQDxUVEBgWGBYVEhgWFREWFRYWFhUVFhYYKDQgGBolHRUVIjEhJSsrMC8uFx8zODMsNygtLisBCgoKDg0OGhAQGCsdHx8rLS0rLSswLS0tLS0tLS0tLS0tLS0rLS0tLS0tLS0tLS0tLS0tLS0tKystKystNys3Lf/AABEIAJcBTQMBIgACEQEDEQH/xAAcAAEAAQUBAQAAAAAAAAAAAAAABwEEBQYIAwL/xABKEAABAwIBBQgNCgYCAwEAAAABAAIDBBESBRchk9EGBxMUMUFT4iI0NVFUYWRxcnOys9IWIzIzQlKBkZKxFUNjdKHBYoWDo+GC/8QAGAEBAAMBAAAAAAAAAAAAAAAAAAECAwT/xAAiEQEAAgEEAwEBAQEAAAAAAAAAAQISAxETUSExMkFxYSL/2gAMAwEAAhEDEQA/AJwRFaZWNqecjR8y/wBkoLtFzkMoT9LNrHbVXj8/Szax21b8E9qZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujEXOfH5+lm"
                        "1jtqcfn6WbWO2pwT2ZujEXOfH5+lm1jtqcfn6WbWO2pwT2ZujFQrnTj8/Szax21bJvdVcr8pQNdJI4Wk0Oe4g/NP5iVWdGYjfcyTQiIslxWmV+15/Uv9gq7Vplftef1L/YKQOdWqqo1VXexEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAWzb23dOn80nunrWVs29t3Tp/NJ7p6rf5kj2m5ERcTYVplftef1L/YKu1aZX7Xn9S/2CkDnVqqqNVV3sVxk6jdUTRwssHSPDRfQLnvra82df96n/W74VhNx3dCj9e391Pix1LzWfC1YiUPZs6/71P8Ard8KZs6/71P+t3wqYUWfLZbGEPZs6/71P+t3wr5l3tq5rS4up7AE/TdzfgpjXhXfVSerd7JTlsYw5/yHkuStmbBEWhzgSMRIHYguNz5gtmzZ1/3qf9bvhVjvYd0qf0JPduU3q+pqTE+EVrEoezZ1/wB6n/W74UzZ1/3qf9bvhUwoqctk4wh7NnX/AHqf9bvhVvlDe/rIIpJnugwsYXGzyTYaTbQppWI3X9oVn9u/9kjVtuYwhXIGQpq6R0UGDE1mI4jYWuB/tZ3NrlD+hrDsVzvRduTf259tqltX1NS0W2hWtYmEN5tcof0NYdiZtcof0NYdimRFTmsnCEN5tcof0NYdiZtcof0NYdimRE5rGEIbza5Q/oaw7F4VW97lFguI2SehI2/5OsprROaxhDnGrpJIXmOZj43D7LhY/wD1Uo6Z00scTLYpJGsF+S7iGi/4lT1uiyFDXQuilAvbsH27KN3MQf8AXOoVyJA6LKNNG/Q5lbGw+dswB/Za11MolWY2Z7NnX/ep/wBbvhTNnX/ep/1u+FTCiy5bL4wh7NnX/ep/1u+FM2df96n/AFu+FTCictjGEOu3tK8AnFT6B993wrTSF0jN9F3mP7Lm93KfOVrpXm3tW0bKKivsj5KmrJWwwNxOPLzNaOdzjzBSvue3v6SmDXTAVMnfeOw"
                        "af+LNt1a94qiImUS0WTKifRBFLL42sJH58izVPuDyk/8AkYPTkYP8Xv8A4U3MYGgAAADmAsB+C+ljOtP4thCEq7cFXQRSTSCENjYXutJc2aLmwstYU+bsO59b/ayewVAa10rTaPKto2Fs29t3Tp/NJ7p61lbNvbd06fzSe6erX+ZRHtNyIi4mwrTK/a8/qX+wVdq0yv2vP6l/sFIHOrVVUaqrvYvaiqnwSMljOF7HBzTYGxHJoPKthzgZT6Zuqj2LCZFoRU1EMBOASSBtwL4b89lIWaqPwl+qG1Z3mkfSYifxrGcDKfTN1UexM4GU+mbqo9i2fNVH4S/VDamaqPwl+qG1Uy0k7WaxnAyn0zdVHsXzJu+yk4FplaQRY/NM5D+C2nNVH4S/VDavKq3r42Rvfxl5wsLrcGNNgT30y0zazQMk5RlpJWzQOwvaCAS0G1wQdB8RWdzgZT6Zuqj2LGblckiuqY6dzzHjDjiAuRhaXch8y3rNVH4S/VDarXmkT5RET+NYzgZT6Zuqj2JnAyn0zdVHsWz5qo/CX6obUzVR+Ev1Q2quWknazWM4GU+mbqo9i8a3dtlCaN8UkrXMe0tcODYLg6DpAuFtuaqPwl+qG1WOXN7llNTTTioe8xxl2ExgA25r30KYtp/htZ4b0Xbk39ufbapbUR70Xbkv9ufaapcWet9LV9MFu1ylLS0Us0JDXtLbEgEaXAHQfEVGWcPKXSR6pqkLfL7mz+kz3jVCsTcTmt5LkD8zZX0qxMeYRaZ38Nozh5S6SPVNQb4eUukj1TVsWapvhTtSPiXnU717WMe/jLjhYTbghpsCfvJlpo2stsi75k4e1tW2N7CbFzAWOYPvW5CB3tClQG65qPJ+H+l0Zks3ghP9FnshV1axHpNZ3XSgbdNO6LKdTIw2cyrL2m17Oa4EG3PpCnlQXl2l4bK8sJOHhK3BfltjeG3tz8qjR9yXe+cDKfTN1TNiZwMp9M3VR7Fs+aqPwl+qG1M1UfhL9UNqvlpI2s1jOBlPpm6q"
                        "PYmcDKfTN1UexbPmqj8JfqhtTNVH4S/VDamWkbWau7d/lIggyt1TNi1glSbJvWRhpPGXmwJ+qHN+K0fcrSiaupYzpBnbfxhpxH/DSr1tXacUTE/qXtxG58UNM0EDhXgOkPPc8jfMBo89zzrYkXhXVAiikkPIyNzv0gn/AEuWZ3ndr6a/uq3aU9AeDsZpbXwNIAb3sbvs+bSVo1VvmVzj822CId7CXH8yf9LT6qodK98shxOe4uce+TpK81010qxHllNpbJX7ua+eKSKR0eF7S1wEYFw4WOnmWtoi0isR6RM7i2be27p0/mk909aytm3tu6dP5pPdPUX+ZI9puREXE2FaZX7Xn9S/2CrtWmV+15/Uv9gpA51aqqjVVd7FmNx3dCj9e391PigPcd3Qo/Xt/dT4ubW9r09CLxrD83J6Dv2K54blCew+dm1jtqpSmSZts6NVtlP6ib1T/ZK58/iE/Szax21DXzHQZZj/AOR21acM9ozZ7ex7pU/oSe7cpuUJb2ndOD0ZPduU2qut9Jr6EWI3XPLaCsLSWkU7yCDYg4TpB5lBX8Qn6WbWO2qKaeRNtnRiwu7TufWeocoN/iE/Szax21fL62ZwIdJK4HlBkcQfOLq8aPn2jNuW9F25N/bn22qXFEm9F25N/bn22qW1TV+k09NX3y+5s/pM941QtTfWM9Nv7qad8vubP6TPeNULU31jPTb+610vmVbe3SKt8o/Uzeqf7JVwrfKP1M3qn+yVzQ0c4834LovJHa8HqWewFzpzfgui8kdrwepZ7AXRrfjOi7UJ1nd3/sme9apsUJ1nd3/sme9aqaX7/FrJsRFQrJZVFzk3KM9h87NydI7aq/xCfpZtY7atuH/VM3RFR9B/on9lBm4Z4GUqQnpSPza4BYr+IT9LNrHbVTJ1WYJophyxyNf58JBt/haV08YlE23l0asduijLqSqa3lNO8D9JV7TztkY17DdrmhwPfBFwvsi/KuX00c1hVWw7sdzEtDM8hpMDnEseBoaCb4HHmIvbx"
                        "2Wuruid43Y7bKoqKqkFs29t3Tp/NJ7p61lbNvbd06fzSe6eq3+ZI9puREXE2FaZX7Xn9S/2CrtWmV+15/Uv9gpA51aqqjVVd7FmNx3dCj9e391Pi5/3KTNjrqV7yGNbM0lzjYNF+Uk8gU2fKSh8KptczaubWjyvRfVv1cnoO/Yrm9vIFPlXuiojG8CppiSx385mnQfGoEbyBW0f1F1URFuq2fe07pwejJ7tym1QbvfVMcOUIZJXsjaGyXc5waBeNwFyVL3yjofCqbXM2rm1o/6aV9L2tpWTRvikGJj2lrhci4Ogi40ha/m/yZ0J1snxLJ/KOh8KptczanyjofCqbXM2rOMo9J8MZm/yZ0J1snxLGbptxdBBR1MsURa9kRc08JIbEcmgmxWzfKOh8KptczasRuty7RyUNUyOop3udC4BrZWkuPeAB0q0TbdExDTt6Ltyb+3PttUuKHd62sihqpXTPZEDAQC9waCcbdFypR/j9H4RT61m1Tq/RX0xG+X3Nn9JnvGqFqb6xnpt/dS5vhZWppcnzMjmhkcXMs1sjST2bSbAFRHTmz2H/m391ppfMq29ukVb5R+pm9U/2Srb+PUfhFPrmbVb1+XaMxSgVFOSY3aBK257E+Nc+0roC5vwXReSO14PUs9kLnTm/BT3kvLlI2CEGopwREwEGVtwQ0aOVb634pRm1CdZ3d/7JnvWqWv4/R+EU+uZtUQVdQz+M8LiZg4+x2PEMOESNOK/Ja3OqaX7/E2TiixfyjofCqbXM2p8o6Hwqm1zNqz2lfeGMG9/kzoTrZPiT5AZM6E62T4lk/lHQ+FU2uZtT5R0PhVNrmbVbe3+o8MTNuByaGuIhOhpP1sne9JQqf8Aan2fdFQlrgKmmPYn+czvedQEttGZ87qW2SLvb7rmxtbRVLg0A/NPcdAufq3E8niPjt3ryddc1rZ9z+7irowGEieMfYk5WjvNfyj8bqL6W/mExbtNj4w4EOAcDygi4P4FYOq3G5OkN3U8YP8Awuz2SFhcn75tG+"
                        "wmZLAfMHt/Nun/AAs1Buyyc/kqYh6RLfaWO1oW3iWD3Sbicnw0lTNHEWvZA9zTwshsWtJBsTYqJVNm6nLtJJQ1bI6ine51NIAGytJJLTYAXUJro0t9p3UtsLZt7bunT+aT3T1rK2be27p0/mk909Xv8yrHtNyIi4mwrTK/a8/qX+wVdq0yv2vP6l/sFIHOrVVUaqrvYqIqogoqoiAiIgoiqiCiKqIKIqogollVEFEVUQUsiqiAqWVUQUsiqiCiKqIKIqogoiqiAiIgoqoiCiqiIC2be27p0/mk909aytm3tu6dP5pPdPVb/Mke03IiLibCtMr9rz+pf7BV2vGsh4SOSO9sTHNv3sQIv/lBzg1VUlDep8p/9PWTNT5UdV1l18tO2WMo1RSVmp8qOq6yZqfKTqusnLTsxlGqKSs1PlR1PWTNT5SdV1k5admMo1RSVmp8qOq6yZqfKTqusnLTsxlGqKSs1PlR1PWTNT5UdT1k5admMo1RSVmp8qOp6yZqfKjqesnLTsxlGqKSs1PlJ1PWTNT5SdT1k5admMo1RSVmp8qOp6yZqfKjqesnLTsxlGqKSs1PlR1PWTNT5UdT1k5admMo1RSVmp8qOp6yZqfKjqesnLTsxlGqKSs1PlJ1XWTNT5UdT1k5admMo1RSVmp8qOp6yZqfKjqesnLTsxlGqKSs1PlJ1XWTNT5UdT1k5admMo1RSVmp8qOp6yZqfKjqesnLTsxlGqKSs1PlR1PWTNT5SdT1k5admMo1RSVmp8qOq6yZqfKjqesnLTsxlGqKRmb2LHFzW1YJabOAjBLbi4uMWhemanyo6nrJy07MZRqikrNT5UdT1kzU+UnVdZOWnZjKNVs29t3Tp/NJ7p62TNT5SdV1lk9ze4DiVTHUcPwmAO7Hg8N8TS3lv41W+pWYmITFZ3buiIuZoIiINenramSsngilhhbHFE7s4sZcZDJfTiHJgH5rzy/lyanfGGYHNjjE1QS06IsbWdj3jpe7n0MK9HZBZNXVMtRDFLGYYWs"
                        "MjWv0tMmOwPJytXhFkCSZ1VJLLNTiZ5ZwbOCI4Fg4Nl7tPKMTrX+0reEMhlfKMolgpqbBwkoc/G8Ymxxstd2EEYiS5oAv31bZSrKulgL5HwynjELGuEZb2MkrGPDm3IvYmxB/BWNNk+siFHPwfCywMkgezG0GaInsJGOOjF2DDY25Sr3KkNRW00jeC4u5r43xte9pL3RSNks7BcNBwgcp5UF/leufFJSNZa0tRgdcX7HA92jvG7QmR658zqoPt83UujbYW7ENaRfx6SrBwqKuamL4HUzIZDI4vexxe7A5jWsDCdF3E3NuRUye6op5qlvFpZGy1ReJGyRBoa4MFyHODtFjzJsPOlrK+Zs8kT6c4KiVjYnRO7MRuIA4QO0E25bL3qMuuko4JqYASVDmsja8XDXuvixAcuENef8A8q2yfxyBtRFHTFzn1Mz2SOljEdpHktJAJfz8mFedNuclDqWISSRR01ObSswYpJpCcZwuBsAMXN9tT4F1Pl2Q5NNWwNbKGAOBFwyQPDJGkeI3516S11VSyQ8YdFNFLK2LEyMxvie/QwkFxDmk6OayxlVkOpjgyhTsxTtlLJY3OcwFz3OHCssLAfQB5AOyWQqIqisfA2SE00UczZXF8jHPkdHpY1ojJAGKxJJ5lHgedLlGomnqGCop4RHUmNrHRgvcAGnlLhpNyORZHdLXvpqSeaO2Jjbi4uL4gNI5+VYmlpJIp6lz6Iz46oyMlBg0NIaB9NwcLEFZTdTSST0c8UTcT3NAaLgX7IG1zo5kn2R6W81bVUskPGHRTxSSCPEyMxvie76BIuQ5pOjmtdeFLlGommqG8PTwiOqMTWOjBe5oDDe+IaTiI5F61MdRWPgbJCaWKOZsri97HPkLLljWiMkAXsSSebkVpS0kkM9S59EZy+qMjJQYNDS1gH03BwsWkoMzuirX09LNLHhDmtFsQuASQNI/FWoq5mQ1EpngqMELnAMjthcGkjFZxuNHiXvunpXzUk8UbcbnNFm3AxWcDa50c3OrNsLn"
                        "wVUTKM0pfA5o0w2kcWkAfNuPf50j0StGbpJuIzyPDG1EIZiFjgIkLSx4H3S135g95ZKrr55Kh9PTGOMRMa6WV7S+xffCxjbjTYXJPfCxO6LIE8kETqdoMvAMglbiAxsGF17nQXMc248RKvq6jliqJpo4hVxTxtbJHdoe1zAQHAP7F7S0gEE8yeB95SrqmmpJ5XPgke0twOawgWc5rezbflFzyFfUlbNFT1U3DwVBjge9oZHYNc1rnDFZxuNHJo5FiBkSXite2OnbDw0rHxwAxg4WiMEHCcIJwu0XWSlgfJTVkUdGaVz6d7RphAlc5jg1vzbj3+U25UHhFuimNFK94Y2ohcxrwAcJEjmFj2g/Zcx1/PfvLJDK2GsmgkfGxjYIntxENJLzIHaSdP0QsPuhyFO+OF9O0GTgo4ZWFwAfG1zXh1+TExzdHicVkzkgSV08s0TJGGnia0va13ZNdJiAB0jQ5qeB95LyxjZWySOYWQ1D2hzeTg2Rsfckcp7I6V5bl8rTT8IyqDWSARygNFvmpm3YD33NIc0+MLHPyJMYqqmYzgmT5QxXbgAZT4Yi5wb4ywttbn5FetyPPBV087ZJakFropcfBjBGRiY4YQ29nDk0/STwLGmy/VcHBO58EgkquC4ERkSYTM6PE04tJAGI3HJdZ6hrnvqayJ1sMXBYdFj2bC51z51r9Juekhghmiia2qiqHvNsAdNG6V2KNz+Q3YRa50EBXdfQVJdlHgmkGoELGOxN7EYMEj+X7IJ8/Mk7Hl67nsuyzzPbKGhkkfDQEAguiD3MIdfldoY7zPCut1NfPBCw02DhHzNYMYJacV9Fh5lj5sgywPpJYZZqjgXhmB/BNAheMDwMLRyDCbX+yspl+kfKKbgxiwVcbzpAs1pNzpTxuPKfLl6OOoiAxyhjY2npZCGhrgO84m/olYwZdqHU1A/HDE+eZzHvcy7GhokNwCRb6A5+detBkWVlY7Fbi0cj5otI0yz/AExbmDTwhHrVaOyTO2mye10HDmGoe6SPF"
                        "Hpa4SgfTOE/TbzpGyPLJ1eU5oYYwHw1Ms04iiLW4YwSCSXWJuGhrjoPiV/QR1TXHh5IZWFvK2Isc11/OQW2v41iq2hllihkgpxTSU9QJWROMYEgwlrheMkNuHu098L1raqtmhmZHTPhc6PC0vljxYnkNLgGkizWlzrkg6NARKw3M1DXVLrxxxtex76dzb4nxiQtk4Qk9mScDwT95XeTcvSmtmgmDBGZXxwuAIOKJrXOY898tcCPRcvGbc9LBxR8Es1QaeRrWxu4JrRE4COQAho5G6dJ+z316nIkkkdY0/NvdWGaB9wcLmtZwb9HNdpBHev31PgUgy7M6GlecF5Movgd2P8ALbLOwW7xtG3T517srKqplnFO+KGOKQxhz4zI6V7QC82xCzQTbvmxWPoMk1IpqFskYbIzKLp5GhzSGNdJO8kG+n6xv5q8p2VNHJUNZA6pilmMrCx7GuY54GNjw8jRcEgi/Konb8HvlvKFTFDDHFwRqZThAsTHdjTJIbHTazSBfncFksk1zaiCKdugPjDrd4kaWnxg3H4LDSZNqampE0jn0gjgaxnBuY673nFNpeDoFmDkF7FXG5qhkpeHgfidGJi+N7i27mydk4EN5CHYuYcoSfQziIiqkREQEsiICIiAiIgJZEQEsiICWREBERAsiIgJZEQEREBERAREQLIiICIiAiIgIiICIiAiIgJZEQEREH//2Q==\"><span style=\" text-decoration: underline; color:#0000ff;\">TextLabel</span></a></p></body></html>", nullptr));
        menuFile->setTitle(QCoreApplication::translate("MainWindow", "File", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
