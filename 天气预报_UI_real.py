# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '天气预报_UI_real.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QHeaderView, QLCDNumber,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QTableView, QTableWidget, QTableWidgetItem,
    QTextBrowser, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)
import 图标_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(718, 612)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 708, 607))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.labelV = QLabel(self.tab)
        self.labelV.setObjectName(u"labelV")
        self.labelV.setGeometry(QRect(-30, 560, 551, 21))
        self.labelV.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 311, 31))
        self.label.setStyleSheet(u"color: rgb(85, 85, 255);\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 255, 127);")
        self.Filedirectorycity1 = QLineEdit(self.tab)
        self.Filedirectorycity1.setObjectName(u"Filedirectorycity1")
        self.Filedirectorycity1.setGeometry(QRect(290, 510, 191, 41))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        self.Filedirectorycity1.setFont(font)
        self.Filedirectorycity1.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 22pt \"Microsoft YaHei UI\";")
        self.Helpbut = QToolButton(self.tab)
        self.Helpbut.setObjectName(u"Helpbut")
        self.Helpbut.setGeometry(QRect(420, 10, 24, 22))
        self.SaveBtnnow = QPushButton(self.tab)
        self.SaveBtnnow.setObjectName(u"SaveBtnnow")
        self.SaveBtnnow.setGeometry(QRect(500, 510, 121, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveBtnnow.sizePolicy().hasHeightForWidth())
        self.SaveBtnnow.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Microsoft New Tai Lue"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        self.SaveBtnnow.setFont(font1)
        self.SaveBtnnow.setStyleSheet(u"font: 700 14pt \"Microsoft New Tai Lue\";\n"
"")
        self.lablename1 = QLabel(self.tab)
        self.lablename1.setObjectName(u"lablename1")
        self.lablename1.setGeometry(QRect(80, 10, 321, 20))
        self.lablename1.setMaximumSize(QSize(1000, 20))
        self.lablename1.setStyleSheet(u"font: 700 15pt \"Microsoft YaHei UI\";\n"
"border-color: rgb(0, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.Fig1 = QTextBrowser(self.tab)
        self.Fig1.setObjectName(u"Fig1")
        self.Fig1.setGeometry(QRect(10, 10, 50, 30))
        self.Fig1.setMaximumSize(QSize(50, 30))
        self.Fig1.setStyleSheet(u"border-image: url(:/svg/smog-solid.svg);")
        self.textEditNowTime1 = QTextEdit(self.tab)
        self.textEditNowTime1.setObjectName(u"textEditNowTime1")
        self.textEditNowTime1.setGeometry(QRect(340, 60, 311, 31))
        self.textEditNowTime1.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";\n"
"alternate-background-color: rgb(170, 255, 127);\n"
"font: 700 11pt \"Microsoft YaHei UI\";")
        self.layoutWidget_2 = QWidget(self.tab)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(440, 130, 211, 304))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.textEditwinddir = QTextEdit(self.layoutWidget_2)
        self.textEditwinddir.setObjectName(u"textEditwinddir")
        self.textEditwinddir.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"font: 20pt \"Microsoft YaHei UI\";")

        self.verticalLayout_6.addWidget(self.textEditwinddir)

        self.textEditwinddirdegree = QTextEdit(self.layoutWidget_2)
        self.textEditwinddirdegree.setObjectName(u"textEditwinddirdegree")
        self.textEditwinddirdegree.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"font: 20pt \"Microsoft YaHei UI\";")

        self.verticalLayout_6.addWidget(self.textEditwinddirdegree)

        self.textEditwindspeed = QTextEdit(self.layoutWidget_2)
        self.textEditwindspeed.setObjectName(u"textEditwindspeed")
        self.textEditwindspeed.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"font: 20pt \"Microsoft YaHei UI\";")

        self.verticalLayout_6.addWidget(self.textEditwindspeed)

        self.textEditwindsca = QTextEdit(self.layoutWidget_2)
        self.textEditwindsca.setObjectName(u"textEditwindsca")
        self.textEditwindsca.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"font: 20pt \"Microsoft YaHei UI\";")

        self.verticalLayout_6.addWidget(self.textEditwindsca)

        self.layoutWidget_3 = QWidget(self.tab)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(320, 130, 135, 301))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(0, 255, 0);\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.label_9)

        self.label_6 = QLabel(self.layoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(85, 170, 127);\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.label_6)

        self.label_7 = QLabel(self.layoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(28, 170, 7);\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.label_7)

        self.label_8 = QLabel(self.layoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(67, 255, 167);\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.label_8)

        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(70, 440, 211, 61))
        self.label_10.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(85, 80, 82);\n"
"\n"
"")
        self.textEdittimeupdate = QTextEdit(self.tab)
        self.textEdittimeupdate.setObjectName(u"textEdittimeupdate")
        self.textEdittimeupdate.setGeometry(QRect(290, 450, 301, 51))
        self.textEdittimeupdate.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"font: 20pt \"Microsoft YaHei UI\";")
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(160, 500, 131, 51))
        self.label_11.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(85, 80, 82);\n"
"")
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 130, 120, 301))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(255, 0, 127);\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(87, 224, 255);\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(170, 0, 255);\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(7, 243, 255);\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.label_5)

        self.layoutWidget_4 = QWidget(self.tab)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(140, 133, 171, 304))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.textEdittemper = QTextEdit(self.layoutWidget_4)
        self.textEdittemper.setObjectName(u"textEdittemper")
        self.textEdittemper.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"font: 20pt \"Microsoft YaHei UI\";")

        self.verticalLayout_8.addWidget(self.textEdittemper)

        self.textEditprcp = QTextEdit(self.layoutWidget_4)
        self.textEditprcp.setObjectName(u"textEditprcp")
        self.textEditprcp.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"font: 20pt \"Microsoft YaHei UI\";")

        self.verticalLayout_8.addWidget(self.textEditprcp)

        self.textEditpresure = QTextEdit(self.layoutWidget_4)
        self.textEditpresure.setObjectName(u"textEditpresure")
        self.textEditpresure.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"font: 20pt \"Microsoft YaHei UI\";")

        self.verticalLayout_8.addWidget(self.textEditpresure)

        self.textEditrh = QTextEdit(self.layoutWidget_4)
        self.textEditrh.setObjectName(u"textEditrh")
        self.textEditrh.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"font: 20pt \"Microsoft YaHei UI\";")

        self.verticalLayout_8.addWidget(self.textEditrh)

        self.fig1 = QTableView(self.tab)
        self.fig1.setObjectName(u"fig1")
        self.fig1.setGeometry(QRect(0, 1, 711, 641))
        self.fig1.setStyleSheet(u"background-image: url(:/jpg/\u98de\u673a\u8dd1\u9053.jpg);")
        self.tabWidget.addTab(self.tab, "")
        self.fig1.raise_()
        self.layoutWidget.raise_()
        self.labelV.raise_()
        self.Filedirectorycity1.raise_()
        self.Helpbut.raise_()
        self.SaveBtnnow.raise_()
        self.lablename1.raise_()
        self.Fig1.raise_()
        self.layoutWidget_2.raise_()
        self.layoutWidget_3.raise_()
        self.textEditNowTime1.raise_()
        self.label.raise_()
        self.label_10.raise_()
        self.textEdittimeupdate.raise_()
        self.label_11.raise_()
        self.layoutWidget_4.raise_()
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableWidget_2 = QTableWidget(self.tab_2)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(0, -20, 771, 651))
        self.tableWidget_2.setStyleSheet(u"background-image: url(:/jpg/\u98de\u673a\u8dd1\u9053.jpg);")
        self.lcdNumber = QLCDNumber(self.tab_2)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(120, 420, 64, 23))
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 0, 381, 31))
        self.label_12.setStyleSheet(u"color: rgb(85, 85, 255);\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 255, 127);")
        self.textEditNowTime2 = QTextEdit(self.tab_2)
        self.textEditNowTime2.setObjectName(u"textEditNowTime2")
        self.textEditNowTime2.setGeometry(QRect(10, 40, 311, 31))
        self.textEditNowTime2.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";\n"
"alternate-background-color: rgb(170, 255, 127);\n"
"font: 700 11pt \"Microsoft YaHei UI\";")
        self.Filedirectorycity2 = QLineEdit(self.tab_2)
        self.Filedirectorycity2.setObjectName(u"Filedirectorycity2")
        self.Filedirectorycity2.setGeometry(QRect(10, 140, 191, 41))
        self.Filedirectorycity2.setFont(font)
        self.Filedirectorycity2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 22pt \"Microsoft YaHei UI\";")
        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 90, 131, 51))
        self.label_14.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(85, 80, 82);\n"
"")
        self.SaveBtnforecast = QPushButton(self.tab_2)
        self.SaveBtnforecast.setObjectName(u"SaveBtnforecast")
        self.SaveBtnforecast.setGeometry(QRect(10, 190, 101, 41))
        sizePolicy.setHeightForWidth(self.SaveBtnforecast.sizePolicy().hasHeightForWidth())
        self.SaveBtnforecast.setSizePolicy(sizePolicy)
        self.SaveBtnforecast.setFont(font1)
        self.SaveBtnforecast.setStyleSheet(u"font: 700 14pt \"Microsoft New Tai Lue\";\n"
"")
        self.labelV_2 = QLabel(self.tab_2)
        self.labelV_2.setObjectName(u"labelV_2")
        self.labelV_2.setGeometry(QRect(-20, 560, 561, 20))
        self.labelV_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.tableWidgetforecast = QTableWidget(self.tab_2)
        self.tableWidgetforecast.setObjectName(u"tableWidgetforecast")
        self.tableWidgetforecast.setGeometry(QRect(30, 250, 641, 301))
        self.labelforecast = QLabel(self.tab_2)
        self.labelforecast.setObjectName(u"labelforecast")
        self.labelforecast.setGeometry(QRect(350, 30, 331, 201))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tableView = QTableView(self.tab_3)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(-380, -340, 1251, 991))
        self.tableView.setStyleSheet(u"background-image: url(:/jpg/\u98ce\u5207\u53d8.jpg);")
        self.calendarWidget = QCalendarWidget(self.tab_3)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(437, 0, 271, 161))
        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 0, 401, 31))
        self.label_13.setStyleSheet(u"color: rgb(85, 85, 255);\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 255, 127);")
        self.Filedirectorycity3 = QLineEdit(self.tab_3)
        self.Filedirectorycity3.setObjectName(u"Filedirectorycity3")
        self.Filedirectorycity3.setGeometry(QRect(10, 130, 171, 41))
        self.Filedirectorycity3.setFont(font)
        self.Filedirectorycity3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 22pt \"Microsoft YaHei UI\";")
        self.label_15 = QLabel(self.tab_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 80, 131, 51))
        self.label_15.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(85, 80, 82);\n"
"")
        self.Filedirectorystarttime = QLineEdit(self.tab_3)
        self.Filedirectorystarttime.setObjectName(u"Filedirectorystarttime")
        self.Filedirectorystarttime.setGeometry(QRect(300, 90, 141, 31))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.Filedirectorystarttime.setFont(font2)
        self.Filedirectorystarttime.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Microsoft YaHei UI\";")
        self.Filedirectoryendtime = QLineEdit(self.tab_3)
        self.Filedirectoryendtime.setObjectName(u"Filedirectoryendtime")
        self.Filedirectoryendtime.setGeometry(QRect(300, 140, 141, 31))
        self.Filedirectoryendtime.setFont(font2)
        self.Filedirectoryendtime.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Microsoft YaHei UI\";")
        self.label_16 = QLabel(self.tab_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(190, 80, 131, 51))
        self.label_16.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(85, 80, 82);\n"
"")
        self.label_17 = QLabel(self.tab_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(190, 120, 131, 51))
        self.label_17.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(85, 80, 82);\n"
"")
        self.labelV_3 = QLabel(self.tab_3)
        self.labelV_3.setObjectName(u"labelV_3")
        self.labelV_3.setGeometry(QRect(-40, 510, 781, 21))
        self.labelV_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.SaveBtnpast = QPushButton(self.tab_3)
        self.SaveBtnpast.setObjectName(u"SaveBtnpast")
        self.SaveBtnpast.setGeometry(QRect(570, 540, 131, 41))
        sizePolicy.setHeightForWidth(self.SaveBtnpast.sizePolicy().hasHeightForWidth())
        self.SaveBtnpast.setSizePolicy(sizePolicy)
        self.SaveBtnpast.setFont(font1)
        self.SaveBtnpast.setStyleSheet(u"font: 700 14pt \"Microsoft New Tai Lue\";\n"
"")
        self.label_18 = QLabel(self.tab_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 50, 118, 26))
        self.label_18.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(85, 80, 82);\n"
"")
        self.Filedirectorylat = QLineEdit(self.tab_3)
        self.Filedirectorylat.setObjectName(u"Filedirectorylat")
        self.Filedirectorylat.setGeometry(QRect(352, 41, 88, 41))
        self.Filedirectorylat.setFont(font2)
        self.Filedirectorylat.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Microsoft YaHei UI\";")
        self.label_19 = QLabel(self.tab_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(220, 50, 118, 26))
        self.label_19.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(85, 80, 82);\n"
"")
        self.Filedirectorylong = QLineEdit(self.tab_3)
        self.Filedirectorylong.setObjectName(u"Filedirectorylong")
        self.Filedirectorylong.setGeometry(QRect(120, 40, 87, 41))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(False)
        self.Filedirectorylong.setFont(font3)
        self.Filedirectorylong.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"Microsoft YaHei UI\";")
        self.labelfig = QLabel(self.tab_3)
        self.labelfig.setObjectName(u"labelfig")
        self.labelfig.setGeometry(QRect(20, 170, 681, 371))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_20 = QLabel(self.tab_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 0, 281, 51))
        self.label_20.setStyleSheet(u"color: rgb(85, 85, 255);\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 255, 127);")
        self.labelV_4 = QLabel(self.tab_4)
        self.labelV_4.setObjectName(u"labelV_4")
        self.labelV_4.setGeometry(QRect(-70, 560, 781, 21))
        self.labelV_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.pushButtonsat = QPushButton(self.tab_4)
        self.pushButtonsat.setObjectName(u"pushButtonsat")
        self.pushButtonsat.setGeometry(QRect(30, 440, 151, 31))
        self.pushButtonsat.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(0, 0, 0);")
        self.Filedirectorysatfile = QLineEdit(self.tab_4)
        self.Filedirectorysatfile.setObjectName(u"Filedirectorysatfile")
        self.Filedirectorysatfile.setGeometry(QRect(180, 440, 371, 31))
        self.Filedirectorysatfile.setFont(font2)
        self.Filedirectorysatfile.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Microsoft YaHei UI\";")
        self.tableView_3 = QTableView(self.tab_4)
        self.tableView_3.setObjectName(u"tableView_3")
        self.tableView_3.setGeometry(QRect(-5, -19, 721, 601))
        self.tableView_3.setStyleSheet(u"background-image: url(:/jpg/\u536b\u661f.jpg);")
        self.pushButtonsatnow = QPushButton(self.tab_4)
        self.pushButtonsatnow.setObjectName(u"pushButtonsatnow")
        self.pushButtonsatnow.setGeometry(QRect(10, 520, 151, 31))
        self.pushButtonsatnow.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(0, 0, 0);")
        self.pushButtonsathis = QPushButton(self.tab_4)
        self.pushButtonsathis.setObjectName(u"pushButtonsathis")
        self.pushButtonsathis.setGeometry(QRect(10, 550, 201, 31))
        self.pushButtonsathis.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(0, 0, 0);")
        self.pushButtonsathis.setAutoDefault(False)
        self.label_21 = QLabel(self.tab_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(210, 530, 181, 31))
        self.label_21.setStyleSheet(u"font: 18pt \"\u5b89\u666f\u81e3\u6bdb\u7b14\u884c\u4e66\";\n"
"color: rgb(85, 80, 82);\n"
"")
        self.Filedirectorysattime = QLineEdit(self.tab_4)
        self.Filedirectorysattime.setObjectName(u"Filedirectorysattime")
        self.Filedirectorysattime.setGeometry(QRect(400, 530, 281, 31))
        self.Filedirectorysattime.setFont(font2)
        self.Filedirectorysattime.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Microsoft YaHei UI\";")
        self.textEditNowTime3 = QTextEdit(self.tab_4)
        self.textEditNowTime3.setObjectName(u"textEditNowTime3")
        self.textEditNowTime3.setGeometry(QRect(330, 10, 311, 31))
        self.textEditNowTime3.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";\n"
"alternate-background-color: rgb(170, 255, 127);\n"
"font: 700 11pt \"Microsoft YaHei UI\";")
        self.labelsatlite = QLabel(self.tab_4)
        self.labelsatlite.setObjectName(u"labelsatlite")
        self.labelsatlite.setGeometry(QRect(20, 50, 681, 381))
        self.Filedirectorysatfiletongdao = QLineEdit(self.tab_4)
        self.Filedirectorysatfiletongdao.setObjectName(u"Filedirectorysatfiletongdao")
        self.Filedirectorysatfiletongdao.setGeometry(QRect(30, 480, 191, 31))
        self.Filedirectorysatfiletongdao.setFont(font2)
        self.Filedirectorysatfiletongdao.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Microsoft YaHei UI\";")
        self.pushButtontongdao2 = QPushButton(self.tab_4)
        self.pushButtontongdao2.setObjectName(u"pushButtontongdao2")
        self.pushButtontongdao2.setGeometry(QRect(390, 480, 191, 31))
        self.pushButtontongdao2.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";")
        self.pushButton_tongdao1 = QPushButton(self.tab_4)
        self.pushButton_tongdao1.setObjectName(u"pushButton_tongdao1")
        self.pushButton_tongdao1.setGeometry(QRect(240, 480, 141, 31))
        self.pushButton_tongdao1.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";")
        self.tabWidget.addTab(self.tab_4, "")
        self.tableView_3.raise_()
        self.label_20.raise_()
        self.labelV_4.raise_()
        self.pushButtonsat.raise_()
        self.Filedirectorysatfile.raise_()
        self.pushButtonsatnow.raise_()
        self.pushButtonsathis.raise_()
        self.label_21.raise_()
        self.Filedirectorysattime.raise_()
        self.textEditNowTime3.raise_()
        self.labelsatlite.raise_()
        self.Filedirectorysatfiletongdao.raise_()
        self.pushButtontongdao2.raise_()
        self.pushButton_tongdao1.raise_()
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tableView_16 = QTableView(self.tab_6)
        self.tableView_16.setObjectName(u"tableView_16")
        self.tableView_16.setGeometry(QRect(-700, -190, 1451, 781))
        self.tableView_16.setStyleSheet(u"background-image: url(:/jpg/\u96f7\u7535.jpg);")
        self.label_leida = QLabel(self.tab_6)
        self.label_leida.setObjectName(u"label_leida")
        self.label_leida.setGeometry(QRect(10, 0, 151, 31))
        self.label_leida.setStyleSheet(u"color: rgb(85, 85, 255);\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 255, 127);")
        self.textEditNowTime4 = QTextEdit(self.tab_6)
        self.textEditNowTime4.setObjectName(u"textEditNowTime4")
        self.textEditNowTime4.setGeometry(QRect(390, 0, 311, 31))
        self.textEditNowTime4.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";\n"
"alternate-background-color: rgb(170, 255, 127);\n"
"font: 700 11pt \"Microsoft YaHei UI\";")
        self.labelV_25 = QLabel(self.tab_6)
        self.labelV_25.setObjectName(u"labelV_25")
        self.labelV_25.setGeometry(QRect(20, 560, 781, 21))
        self.labelV_25.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.labelradar = QLabel(self.tab_6)
        self.labelradar.setObjectName(u"labelradar")
        self.labelradar.setGeometry(QRect(10, 40, 681, 451))
        self.pushButtonsat_ld = QPushButton(self.tab_6)
        self.pushButtonsat_ld.setObjectName(u"pushButtonsat_ld")
        self.pushButtonsat_ld.setGeometry(QRect(10, 500, 151, 31))
        self.pushButtonsat_ld.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(0, 0, 0);")
        self.Filedirectorysatfile_ld2 = QLineEdit(self.tab_6)
        self.Filedirectorysatfile_ld2.setObjectName(u"Filedirectorysatfile_ld2")
        self.Filedirectorysatfile_ld2.setGeometry(QRect(160, 500, 491, 31))
        self.Filedirectorysatfile_ld2.setFont(font2)
        self.Filedirectorysatfile_ld2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Microsoft YaHei UI\";")
        self.pushButtonsat_ld2 = QPushButton(self.tab_6)
        self.pushButtonsat_ld2.setObjectName(u"pushButtonsat_ld2")
        self.pushButtonsat_ld2.setGeometry(QRect(10, 530, 151, 31))
        self.pushButtonsat_ld2.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(0, 0, 0);")
        self.Filedirectorysatfile_ld1 = QLineEdit(self.tab_6)
        self.Filedirectorysatfile_ld1.setObjectName(u"Filedirectorysatfile_ld1")
        self.Filedirectorysatfile_ld1.setGeometry(QRect(160, 530, 491, 31))
        self.Filedirectorysatfile_ld1.setFont(font2)
        self.Filedirectorysatfile_ld1.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Microsoft YaHei UI\";")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tableView_17 = QTableView(self.tab_5)
        self.tableView_17.setObjectName(u"tableView_17")
        self.tableView_17.setGeometry(QRect(-110, -130, 1451, 781))
        self.tableView_17.setStyleSheet(u"background-image: url(:/jpg/\u96f7\u7535.jpg);")
        self.label_sat = QLabel(self.tab_5)
        self.label_sat.setObjectName(u"label_sat")
        self.label_sat.setGeometry(QRect(0, 0, 151, 31))
        self.label_sat.setStyleSheet(u"color: rgb(85, 85, 255);\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 255, 127);")
        self.textEditNowTime5 = QTextEdit(self.tab_5)
        self.textEditNowTime5.setObjectName(u"textEditNowTime5")
        self.textEditNowTime5.setGeometry(QRect(400, 0, 311, 31))
        self.textEditNowTime5.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";\n"
"alternate-background-color: rgb(170, 255, 127);\n"
"font: 700 11pt \"Microsoft YaHei UI\";")
        self.labelV_26 = QLabel(self.tab_5)
        self.labelV_26.setObjectName(u"labelV_26")
        self.labelV_26.setGeometry(QRect(-40, 560, 781, 21))
        self.labelV_26.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.labelsatlight = QLabel(self.tab_5)
        self.labelsatlight.setObjectName(u"labelsatlight")
        self.labelsatlight.setGeometry(QRect(0, 30, 691, 461))
        self.pushButtonsatsat = QPushButton(self.tab_5)
        self.pushButtonsatsat.setObjectName(u"pushButtonsatsat")
        self.pushButtonsatsat.setGeometry(QRect(0, 500, 151, 31))
        self.pushButtonsatsat.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(0, 0, 0);")
        self.pushButtonsatsat2 = QPushButton(self.tab_5)
        self.pushButtonsatsat2.setObjectName(u"pushButtonsatsat2")
        self.pushButtonsatsat2.setGeometry(QRect(0, 530, 151, 31))
        self.pushButtonsatsat2.setStyleSheet(u"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color: rgb(0, 0, 0);")
        self.Filedirectorysatfilesat2 = QLineEdit(self.tab_5)
        self.Filedirectorysatfilesat2.setObjectName(u"Filedirectorysatfilesat2")
        self.Filedirectorysatfilesat2.setGeometry(QRect(150, 530, 491, 31))
        self.Filedirectorysatfilesat2.setFont(font2)
        self.Filedirectorysatfilesat2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Microsoft YaHei UI\";")
        self.Filedirectorysatfilesat1 = QLineEdit(self.tab_5)
        self.Filedirectorysatfilesat1.setObjectName(u"Filedirectorysatfilesat1")
        self.Filedirectorysatfilesat1.setGeometry(QRect(150, 500, 491, 31))
        self.Filedirectorysatfilesat1.setFont(font2)
        self.Filedirectorysatfilesat1.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Microsoft YaHei UI\";")
        self.tabWidget.addTab(self.tab_5, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u94a6\u5929\u4e91-\u536b\u661f\u6570\u636e\u8bfb\u53d6\u4e0e\u5904\u7406\u5e73\u53f0", None))
        self.labelV.setText(QCoreApplication.translate("Form", u"                                                                                \u5730\u533a\u5b9e\u65f6\u6c14\u8c61\u6570\u636e\u663e\u793a\u6a21\u5757  V1.0", None))
        self.label.setText(QCoreApplication.translate("Form", u"   \u5730\u533a\u5b9e\u65f6\u6c14\u8c61\u6570\u636e Real-time forecast", None))
        self.Filedirectorycity1.setText(QCoreApplication.translate("Form", u"\u5357\u4eac", None))
        self.Helpbut.setText(QCoreApplication.translate("Form", u"...", None))
        self.SaveBtnnow.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u6570\u636e", None))
        self.lablename1.setText(QCoreApplication.translate("Form", u"\u94a6\u5929\u4e91-\u673a\u573a\u5929\u6c14\u9884\u62a5\u6570\u636e\u7ba1\u7406\u5e73\u53f0", None))
        self.textEditNowTime1.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5f53\u524d\u65f6\u95f4\uff1a2024\u5e745\u670828\u65e5 11\uff1a20</p></body></html>", None))
        self.textEditwinddir.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u4e1c\u5357\u98ce</span></p></body></html>", None))
        self.textEditwinddirdegree.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">107.0</span></p></body></html>", None))
        self.textEditwindspeed.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">2.7m/s</span></p></body></html>", None))
        self.textEditwindsca.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u5fae\u98ce</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u98ce\u5411\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u98ce\u5411(\u5ea6\u00b0)\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u98ce\u901f\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u98ce\u7ea7\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u53f0\u7ad9\u6570\u636e\u4e0a\u4f20\u65f6\u95f4\uff1a", None))
        self.textEdittimeupdate.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">202406210620</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u57ce\u5e02\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5730\u8868\u6e29\u5ea6\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u964d\u96e8\u91cf\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5927\u6c14\u538b\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u7a7a\u6c14\u6e7f\u5ea6\uff1a", None))
        self.textEdittemper.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u4e1c\u5357\u98ce</span></p></body></html>", None))
        self.textEditprcp.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">10mm</span></p></body></html>", None))
        self.textEditpresure.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">1001hpa</span></p></body></html>", None))
        self.textEditrh.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">90%</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u5b9e\u65f6\u6c14\u8c61\u6570\u636e", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"   \u5730\u533a7\u5929\u5929\u6c14\u9884\u62a5Short-term weather forecasts", None))
        self.textEditNowTime2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5f53\u524d\u65f6\u95f4\uff1a2024\u5e745\u670828\u65e5 11\uff1a20</p></body></html>", None))
        self.Filedirectorycity2.setText(QCoreApplication.translate("Form", u"\u5357\u4eac", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u57ce\u5e02\uff1a", None))
        self.SaveBtnforecast.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u6570\u636e", None))
        self.labelV_2.setText(QCoreApplication.translate("Form", u"                                                                                \u5730\u533a7\u5929\u5929\u6c14\u9884\u62a5\u663e\u793a\u6a21\u5757    V1.0", None))
        self.labelforecast.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"7\u5929\u5929\u6c14\u9884\u62a5", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"   \u5730\u533a\u5386\u53f2\u6c14\u8c61\u6570\u636eHistorical meteorological data", None))
        self.Filedirectorycity3.setText(QCoreApplication.translate("Form", u"\u5357\u4eac", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u9644\u8fd1\u57ce\u5e02\uff1a", None))
        self.Filedirectorystarttime.setText(QCoreApplication.translate("Form", u"2024052005", None))
        self.Filedirectoryendtime.setText(QCoreApplication.translate("Form", u"2024052908", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u65f6\u95f4\uff1a", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u622a\u6b62\u65f6\u95f4\uff1a", None))
        self.labelV_3.setText(QCoreApplication.translate("Form", u"                                                                                \u5730\u533a\u5386\u53f2\u6c14\u8c61\u6570\u636e\u663e\u793a\u6a21\u5757   V1.0", None))
        self.SaveBtnpast.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u6570\u636e", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u5730\u533a\u7ecf\u5ea6\uff1a", None))
        self.Filedirectorylat.setText(QCoreApplication.translate("Form", u"30.30", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u5730\u533a\u7eac\u5ea6\uff1a", None))
        self.Filedirectorylong.setText(QCoreApplication.translate("Form", u"120.20", None))
        self.labelfig.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u5386\u53f2\u6c14\u8c61\u6570\u636e", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u536b\u661f\u4e91\u56fe-\u8bfb\u53d6\u536b\u661f\u6570\u636e\u7ed8\u5236\u536b\u661f\u4e91\u56fe", None))
        self.labelV_4.setText(QCoreApplication.translate("Form", u"                                                                                \u536b\u661f\u4e91\u56fe\u663e\u793a\u6a21\u5757 V1.0", None))
        self.pushButtonsat.setText(QCoreApplication.translate("Form", u"\u98ce\u4e91\u536b\u661f\u6570\u636e\u8def\u5f84\uff1a", None))
        self.Filedirectorysatfile.setText(QCoreApplication.translate("Form", u"*nc\u6216*HDF\u683c\u5f0f\u6570\u636e", None))
        self.pushButtonsatnow.setText(QCoreApplication.translate("Form", u"\u83b7\u53d6\u5b9e\u65f6\u536b\u661f\u4e91\u56fe", None))
        self.pushButtonsathis.setText(QCoreApplication.translate("Form", u"\u83b7\u53d6\u5386\u53f2FY4B\u536b\u661f\u6570\u636e", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u5e74\u6708\u65e5\u5c0f\u65f6\u5206\u949f\uff1a", None))
        self.Filedirectorysattime.setText(QCoreApplication.translate("Form", u"202405280630", None))
        self.textEditNowTime3.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5f53\u524d\u65f6\u95f4\uff1a2024\u5e745\u670828\u65e5 11\uff1a20</p></body></html>", None))
        self.labelsatlite.setText("")
        self.Filedirectorysatfiletongdao.setText(QCoreApplication.translate("Form", u"\u7ed8\u5236\u901a\u9053\u540d* NOM101", None))
        self.pushButtontongdao2.setText(QCoreApplication.translate("Form", u"\u591a\u901a\u9053\u5408\u6210\uff08\u5f69\u8272\u589e\u5f3a\uff09", None))
        self.pushButton_tongdao1.setText(QCoreApplication.translate("Form", u"\u5355\u901a\u9053\u9ed1\u767d\u52a0\u5f3a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u6c14\u8c61\u536b\u661f\u4e91\u56fe", None))
        self.label_leida.setText(QCoreApplication.translate("Form", u"  \u96f7\u8fbe\u56de\u6ce2-\u95ea\u7535\u5b9a\u4f4d ", None))
        self.textEditNowTime4.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5f53\u524d\u65f6\u95f4\uff1a2024\u5e745\u670828\u65e5 11\uff1a20</p></body></html>", None))
        self.labelV_25.setText(QCoreApplication.translate("Form", u"                                                             \u95ea\u7535\u5b9a\u4f4d\u6a21\u5757A V1.0", None))
        self.labelradar.setText("")
        self.pushButtonsat_ld.setText(QCoreApplication.translate("Form", u"\u96f7\u8fbe\u56de\u6ce2\u6587\u4ef6\u5939\uff1a", None))
        self.Filedirectorysatfile_ld2.setText(QCoreApplication.translate("Form", u"*txt json\u683c\u5f0f", None))
        self.pushButtonsat_ld2.setText(QCoreApplication.translate("Form", u"\u95ea\u7535\u5b9a\u4f4d\uff1a", None))
        self.Filedirectorysatfile_ld1.setText(QCoreApplication.translate("Form", u"*txt / *xlsx \u683c\u5f0f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Form", u"\u96f7\u8fbe-\u95ea\u7535\u5b9a\u4f4d", None))
        self.label_sat.setText(QCoreApplication.translate("Form", u"  \u4e91\u9876\u6e29\u5ea6-\u95ea\u7535\u5b9a\u4f4d", None))
        self.textEditNowTime5.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5f53\u524d\u65f6\u95f4\uff1a2024\u5e745\u670828\u65e5 11\uff1a20</p></body></html>", None))
        self.labelV_26.setText(QCoreApplication.translate("Form", u"                                                                                \u95ea\u7535\u5b9a\u4f4d\u6a21\u5757B V1.0", None))
        self.labelsatlight.setText("")
        self.pushButtonsatsat.setText(QCoreApplication.translate("Form", u"\u536b\u661fCTT\u6587\u4ef6\u5939\uff1a", None))
        self.pushButtonsatsat2.setText(QCoreApplication.translate("Form", u"\u95ea\u7535\u5b9a\u4f4d\uff1a", None))
        self.Filedirectorysatfilesat2.setText(QCoreApplication.translate("Form", u"*txt / *xlsx \u683c\u5f0f", None))
        self.Filedirectorysatfilesat1.setText(QCoreApplication.translate("Form", u"*txt json\u683c\u5f0f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\u536b\u661f-\u95ea\u7535\u5b9a\u4f4d", None))
    # retranslateUi

