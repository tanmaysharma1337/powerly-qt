# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_ui_newKYQgiT.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QFrame,
    QLCDNumber, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 661)
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: white;\n"
"color:black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_application_header = QLabel(self.centralwidget)
        self.main_application_header.setObjectName(u"main_application_header")
        self.main_application_header.setGeometry(QRect(180, 0, 271, 41))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(25)
        font1.setBold(True)
        self.main_application_header.setFont(font1)
        self.main_application_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_input_schedule = QDateTimeEdit(self.centralwidget)
        self.time_input_schedule.setObjectName(u"time_input_schedule")
        self.time_input_schedule.setGeometry(QRect(370, 110, 194, 24))
        self.time_input_schedule.setStyleSheet(u"background-color:#c4c4c4;")
        self.right_panel_label = QLabel(self.centralwidget)
        self.right_panel_label.setObjectName(u"right_panel_label")
        self.right_panel_label.setGeometry(QRect(330, 83, 271, 20))
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(9)
        self.right_panel_label.setFont(font2)
        self.right_panel_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.set_new_schedule_button = QPushButton(self.centralwidget)
        self.set_new_schedule_button.setObjectName(u"set_new_schedule_button")
        self.set_new_schedule_button.setGeometry(QRect(430, 140, 75, 21))
        self.set_new_schedule_button.setFont(font)
        self.set_new_schedule_button.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4A90E2, /* Lighter blue at the top */\n"
"        stop: 1 #357ABD  /* Darker blue at the bottom */\n"
"    );\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    color: white; /* White text */\n"
"    border: 1px solid #357ABD; /* Subtle darker border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: blue;\n"
"}")
        self.bottom_panel_label = QLabel(self.centralwidget)
        self.bottom_panel_label.setObjectName(u"bottom_panel_label")
        self.bottom_panel_label.setGeometry(QRect(190, 387, 251, 20))
        self.bottom_panel_label.setFont(font2)
        self.bottom_panel_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(300, 70, 20, 261))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 60, 611, 16))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 340, 611, 16))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.HH_timer_label = QLCDNumber(self.centralwidget)
        self.HH_timer_label.setObjectName(u"HH_timer_label")
        self.HH_timer_label.setGeometry(QRect(50, 127, 61, 23))
        self.HH_timer_label.setStyleSheet(u"QLCDNumber {\n"
"    color: red; /* Color of the digits */\n"
"    border: 2px solid grey; /* Optional border around the LCD */\n"
"    border-radius: 5px; /* Rounded corners for styling */\n"
"    padding: 5px; /* Padding around the LCD display */\n"
"}")
        self.MM_timer_label = QLCDNumber(self.centralwidget)
        self.MM_timer_label.setObjectName(u"MM_timer_label")
        self.MM_timer_label.setGeometry(QRect(120, 127, 61, 23))
        self.MM_timer_label.setStyleSheet(u"QLCDNumber {\n"
"    color: red; /* Color of the digits */\n"
"    border: 2px solid grey; /* Optional border around the LCD */\n"
"    border-radius: 5px; /* Rounded corners for styling */\n"
"    padding: 5px; /* Padding around the LCD display */\n"
"}")
        self.SS_timer_label = QLCDNumber(self.centralwidget)
        self.SS_timer_label.setObjectName(u"SS_timer_label")
        self.SS_timer_label.setGeometry(QRect(190, 127, 61, 23))
        self.SS_timer_label.setStyleSheet(u"QLCDNumber {\n"
"    color: red; /* Color of the digits */\n"
"    border: 2px solid grey; /* Optional border around the LCD */\n"
"    border-radius: 5px; /* Rounded corners for styling */\n"
"    padding: 5px; /* Padding around the LCD display */\n"
"}")
        self.left_panel_label = QLabel(self.centralwidget)
        self.left_panel_label.setObjectName(u"left_panel_label")
        self.left_panel_label.setGeometry(QRect(60, 97, 191, 20))
        self.left_panel_label.setFont(font2)
        self.left_panel_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hh_label = QLabel(self.centralwidget)
        self.hh_label.setObjectName(u"hh_label")
        self.hh_label.setGeometry(QRect(63, 150, 31, 20))
        self.hh_label.setFont(font2)
        self.hh_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mm_lebl = QLabel(self.centralwidget)
        self.mm_lebl.setObjectName(u"mm_lebl")
        self.mm_lebl.setGeometry(QRect(135, 150, 31, 20))
        self.mm_lebl.setFont(font2)
        self.mm_lebl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ss_label = QLabel(self.centralwidget)
        self.ss_label.setObjectName(u"ss_label")
        self.ss_label.setGeometry(QRect(205, 150, 31, 20))
        self.ss_label.setFont(font2)
        self.ss_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(10, 488, 611, 16))
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.api_label1 = QLabel(self.centralwidget)
        self.api_label1.setObjectName(u"api_label1")
        self.api_label1.setGeometry(QRect(60, 526, 281, 20))
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(13)
        self.api_label1.setFont(font3)
        self.api_label1.setStyleSheet(u"background:transparent;")
        self.api_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scheduled_label_main = QLabel(self.centralwidget)
        self.scheduled_label_main.setObjectName(u"scheduled_label_main")
        self.scheduled_label_main.setGeometry(QRect(47, 417, 531, 31))
        font4 = QFont()
        font4.setBold(True)
        self.scheduled_label_main.setFont(font4)
        self.scheduled_label_main.setStyleSheet(u"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #e8e9eb, /* Lighter blue at the top */\n"
"        stop: 1 #c4c4c4  /* Darker blue at the bottom */\n"
"    ); /* Optional: overall background of the list widget */\n"
"    border-radius: 10px;\n"
"	border:1px solid grey;")
        self.scheduled_label_main.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cancel_shutdown_button = QPushButton(self.centralwidget)
        self.cancel_shutdown_button.setObjectName(u"cancel_shutdown_button")
        self.cancel_shutdown_button.setGeometry(QRect(244, 457, 131, 21))
        self.cancel_shutdown_button.setFont(font)
        self.cancel_shutdown_button.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #ff4040, /* Lighter blue at the top */\n"
"        stop: 1 #e63737  /* Darker blue at the bottom */\n"
"    );\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    color: white; /* White text */\n"
"    border: 1px solid #357ABD; /* Subtle darker border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #ad1717;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #A0A0A0, /* Light grey */\n"
"        stop: 1 #808080  /* Darker grey */\n"
"    );\n"
"    border: 1px solid #808080; /* Grey border */\n"
"    color: #C0C0C0; /* Muted text */\n"
"}")
        self.api_server_link_button = QPushButton(self.centralwidget)
        self.api_server_link_button.setObjectName(u"api_server_link_button")
        self.api_server_link_button.setGeometry(QRect(300, 524, 191, 24))
        self.api_server_link_button.setFont(font3)
        self.api_server_link_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.api_server_link_button.setStyleSheet(u"color:red;")
        self.creator_label_main = QPushButton(self.centralwidget)
        self.creator_label_main.setObjectName(u"creator_label_main")
        self.creator_label_main.setGeometry(QRect(130, 580, 371, 31))
        font5 = QFont()
        font5.setFamilies([u"Consolas"])
        font5.setPointSize(13)
        font5.setBold(True)
        self.creator_label_main.setFont(font5)
        self.creator_label_main.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.creator_label_main.setStyleSheet(u"")
        self.predefined_minute_combo = QComboBox(self.centralwidget)
        self.predefined_minute_combo.addItem("")
        self.predefined_minute_combo.addItem("")
        self.predefined_minute_combo.addItem("")
        self.predefined_minute_combo.addItem("")
        self.predefined_minute_combo.addItem("")
        self.predefined_minute_combo.addItem("")
        self.predefined_minute_combo.setObjectName(u"predefined_minute_combo")
        self.predefined_minute_combo.setGeometry(QRect(393, 237, 69, 22))
        self.predefined_minute_combo.setStyleSheet(u"    QComboBox {\n"
"        background: qlineargradient(\n"
"            x1: 0, y1: 0, x2: 0, y2: 1,\n"
"            stop: 0 #e8e9eb, /* Lighter blue at the top */\n"
"            stop: 1 #c4c4c4  /* Darker blue at the bottom */\n"
"        );\n"
"        border-radius: 10px;\n"
"        border: 1px solid grey;\n"
"        padding: 5px;\n"
"    }\n"
"\n"
"    QComboBox::drop-down {\n"
"        subcontrol-origin: padding;\n"
"        subcontrol-position: top right;\n"
"        width: 15px;\n"
"        border-left: 1px solid grey;\n"
"    }\n"
"\n"
"    QComboBox::down-arrow {\n"
"        width: 8px;\n"
"        height: 8px;\n"
"		image:url(:/icons/down.png);\n"
"    }\n"
"\n"
"    QComboBox QAbstractItemView {\n"
"        background: qlineargradient(\n"
"            x1: 0, y1: 0, x2: 0, y2: 1,\n"
"            stop: 0 #e8e9eb,\n"
"            stop: 1 #c4c4c4\n"
"        );\n"
"        border-radius: 10px;\n"
"        border: 1px solid grey;\n"
"    }\n"
"\n"
"    QComboBox QAbstractItemView::item {\n"
"        b"
                        "ackground: transparent;\n"
"        padding: 5px;\n"
"		border-radius: 10px;\n"
"    }\n"
"\n"
"    QComboBox QAbstractItemView::item:hover {\n"
"        background: #a6a6a6; /* Highlighted item's background on hover */\n"
"        color: white; /* Change text color on hover */\n"
"		border-radius: 10px;\n"
"    }\n"
"\n"
"    QComboBox QAbstractItemView::item:selected {\n"
"        background: #808080; /* Selected item's background */\n"
"        color: white; /* Selected item's text color */\n"
"    }")
        self.predefined_hours_combo = QComboBox(self.centralwidget)
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.addItem("")
        self.predefined_hours_combo.setObjectName(u"predefined_hours_combo")
        self.predefined_hours_combo.setGeometry(QRect(393, 268, 69, 22))
        self.predefined_hours_combo.setStyleSheet(u"    QComboBox {\n"
"        background: qlineargradient(\n"
"            x1: 0, y1: 0, x2: 0, y2: 1,\n"
"            stop: 0 #e8e9eb, /* Lighter blue at the top */\n"
"            stop: 1 #c4c4c4  /* Darker blue at the bottom */\n"
"        );\n"
"        border-radius: 10px;\n"
"        border: 1px solid grey;\n"
"        padding: 5px;\n"
"    }\n"
"\n"
"    QComboBox::drop-down {\n"
"        subcontrol-origin: padding;\n"
"        subcontrol-position: top right;\n"
"        width: 15px;\n"
"        border-left: 1px solid grey;\n"
"    }\n"
"\n"
"    QComboBox::down-arrow {\n"
"        width: 8px;\n"
"        height: 8px;\n"
"		image:url(:/icons/down.png);\n"
"    }\n"
"\n"
"    QComboBox QAbstractItemView {\n"
"        background: qlineargradient(\n"
"            x1: 0, y1: 0, x2: 0, y2: 1,\n"
"            stop: 0 #e8e9eb,\n"
"            stop: 1 #c4c4c4\n"
"        );\n"
"        border-radius: 10px;\n"
"        border: 1px solid grey;\n"
"    }\n"
"\n"
"    QComboBox QAbstractItemView::item {\n"
"        b"
                        "ackground: transparent;\n"
"        padding: 5px;\n"
"		border-radius: 10px;\n"
"    }\n"
"\n"
"    QComboBox QAbstractItemView::item:hover {\n"
"        background: #a6a6a6; /* Highlighted item's background on hover */\n"
"        color: white; /* Change text color on hover */\n"
"		border-radius: 10px;\n"
"    }\n"
"\n"
"    QComboBox QAbstractItemView::item:selected {\n"
"        background: #808080; /* Selected item's background */\n"
"        color: white; /* Selected item's text color */\n"
"    }")
        self.predefined_days_combo = QComboBox(self.centralwidget)
        self.predefined_days_combo.addItem("")
        self.predefined_days_combo.addItem("")
        self.predefined_days_combo.addItem("")
        self.predefined_days_combo.addItem("")
        self.predefined_days_combo.addItem("")
        self.predefined_days_combo.addItem("")
        self.predefined_days_combo.setObjectName(u"predefined_days_combo")
        self.predefined_days_combo.setGeometry(QRect(393, 300, 69, 22))
        self.predefined_days_combo.setStyleSheet(u"    QComboBox {\n"
"        background: qlineargradient(\n"
"            x1: 0, y1: 0, x2: 0, y2: 1,\n"
"            stop: 0 #e8e9eb, /* Lighter blue at the top */\n"
"            stop: 1 #c4c4c4  /* Darker blue at the bottom */\n"
"        );\n"
"        border-radius: 10px;\n"
"        border: 1px solid grey;\n"
"        padding: 5px;\n"
"    }\n"
"\n"
"    QComboBox::drop-down {\n"
"        subcontrol-origin: padding;\n"
"        subcontrol-position: top right;\n"
"        width: 15px;\n"
"        border-left: 1px solid grey;\n"
"    }\n"
"\n"
"    QComboBox::down-arrow {\n"
"        width: 8px;\n"
"        height: 8px;\n"
"		image:url(:/icons/down.png);\n"
"    }\n"
"\n"
"    QComboBox QAbstractItemView {\n"
"        background: qlineargradient(\n"
"            x1: 0, y1: 0, x2: 0, y2: 1,\n"
"            stop: 0 #e8e9eb,\n"
"            stop: 1 #c4c4c4\n"
"        );\n"
"        border-radius: 10px;\n"
"        border: 1px solid grey;\n"
"    }\n"
"\n"
"    QComboBox QAbstractItemView::item {\n"
"        b"
                        "ackground: transparent;\n"
"        padding: 5px;\n"
"		border-radius: 10px;\n"
"    }\n"
"\n"
"    QComboBox QAbstractItemView::item:hover {\n"
"        background: #a6a6a6; /* Highlighted item's background on hover */\n"
"        color: white; /* Change text color on hover */\n"
"		border-radius: 10px;\n"
"    }\n"
"\n"
"    QComboBox QAbstractItemView::item:selected {\n"
"        background: #808080; /* Selected item's background */\n"
"        color: white; /* Selected item's text color */\n"
"    }")
        self.predefined_minute_button = QPushButton(self.centralwidget)
        self.predefined_minute_button.setObjectName(u"predefined_minute_button")
        self.predefined_minute_button.setGeometry(QRect(480, 237, 51, 21))
        self.predefined_minute_button.setFont(font)
        self.predefined_minute_button.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4A90E2, /* Lighter blue at the top */\n"
"        stop: 1 #357ABD  /* Darker blue at the bottom */\n"
"    );\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    color: white; /* White text */\n"
"    border: 1px solid #357ABD; /* Subtle darker border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: blue;\n"
"}")
        self.right_panel_label_2 = QLabel(self.centralwidget)
        self.right_panel_label_2.setObjectName(u"right_panel_label_2")
        self.right_panel_label_2.setGeometry(QRect(370, 200, 191, 20))
        self.right_panel_label_2.setFont(font2)
        self.right_panel_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.predefined_hours_button = QPushButton(self.centralwidget)
        self.predefined_hours_button.setObjectName(u"predefined_hours_button")
        self.predefined_hours_button.setGeometry(QRect(480, 270, 51, 21))
        self.predefined_hours_button.setFont(font)
        self.predefined_hours_button.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4A90E2, /* Lighter blue at the top */\n"
"        stop: 1 #357ABD  /* Darker blue at the bottom */\n"
"    );\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    color: white; /* White text */\n"
"    border: 1px solid #357ABD; /* Subtle darker border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: blue;\n"
"}")
        self.predefined_days_button = QPushButton(self.centralwidget)
        self.predefined_days_button.setObjectName(u"predefined_days_button")
        self.predefined_days_button.setGeometry(QRect(480, 300, 51, 21))
        self.predefined_days_button.setFont(font)
        self.predefined_days_button.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #4A90E2, /* Lighter blue at the top */\n"
"        stop: 1 #357ABD  /* Darker blue at the bottom */\n"
"    );\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    color: white; /* White text */\n"
"    border: 1px solid #357ABD; /* Subtle darker border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: blue;\n"
"}")
        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(320, 174, 301, 20))
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.left_panel_label_2 = QLabel(self.centralwidget)
        self.left_panel_label_2.setObjectName(u"left_panel_label_2")
        self.left_panel_label_2.setGeometry(QRect(60, 201, 191, 20))
        self.left_panel_label_2.setFont(font2)
        self.left_panel_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(0, 174, 301, 20))
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.ss_label_2 = QLabel(self.centralwidget)
        self.ss_label_2.setObjectName(u"ss_label_2")
        self.ss_label_2.setGeometry(QRect(207, 253, 31, 20))
        self.ss_label_2.setFont(font2)
        self.ss_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boot_HH_timer_label = QLCDNumber(self.centralwidget)
        self.boot_HH_timer_label.setObjectName(u"boot_HH_timer_label")
        self.boot_HH_timer_label.setGeometry(QRect(52, 230, 61, 23))
        self.boot_HH_timer_label.setStyleSheet(u"QLCDNumber {\n"
"    color: red; /* Color of the digits */\n"
"    border: 2px solid grey; /* Optional border around the LCD */\n"
"    border-radius: 5px; /* Rounded corners for styling */\n"
"    padding: 5px; /* Padding around the LCD display */\n"
"}")
        self.boot_SS_timer_label = QLCDNumber(self.centralwidget)
        self.boot_SS_timer_label.setObjectName(u"boot_SS_timer_label")
        self.boot_SS_timer_label.setGeometry(QRect(192, 230, 61, 23))
        self.boot_SS_timer_label.setStyleSheet(u"QLCDNumber {\n"
"    color: red; /* Color of the digits */\n"
"    border: 2px solid grey; /* Optional border around the LCD */\n"
"    border-radius: 5px; /* Rounded corners for styling */\n"
"    padding: 5px; /* Padding around the LCD display */\n"
"}")
        self.hh_label_2 = QLabel(self.centralwidget)
        self.hh_label_2.setObjectName(u"hh_label_2")
        self.hh_label_2.setGeometry(QRect(65, 253, 31, 20))
        self.hh_label_2.setFont(font2)
        self.hh_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mm_lebl_2 = QLabel(self.centralwidget)
        self.mm_lebl_2.setObjectName(u"mm_lebl_2")
        self.mm_lebl_2.setGeometry(QRect(137, 253, 31, 20))
        self.mm_lebl_2.setFont(font2)
        self.mm_lebl_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boot_MM_timer_label = QLCDNumber(self.centralwidget)
        self.boot_MM_timer_label.setObjectName(u"boot_MM_timer_label")
        self.boot_MM_timer_label.setGeometry(QRect(122, 230, 61, 23))
        self.boot_MM_timer_label.setStyleSheet(u"QLCDNumber {\n"
"    color: red; /* Color of the digits */\n"
"    border: 2px solid grey; /* Optional border around the LCD */\n"
"    border-radius: 5px; /* Rounded corners for styling */\n"
"    padding: 5px; /* Padding around the LCD display */\n"
"}")
        self.boot_time_label_main = QLabel(self.centralwidget)
        self.boot_time_label_main.setObjectName(u"boot_time_label_main")
        self.boot_time_label_main.setGeometry(QRect(14, 300, 271, 20))
        self.boot_time_label_main.setFont(font2)
        self.boot_time_label_main.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 630, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u26a1\ufe0fPowerly\u26a1\ufe0f", None))
        self.main_application_header.setText(QCoreApplication.translate("MainWindow", u"\u26a1\ufe0fPowerly\u26a1\ufe0f", None))
        self.right_panel_label.setText(QCoreApplication.translate("MainWindow", u"Pick Date & Time for Shutdown", None))
        self.set_new_schedule_button.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.bottom_panel_label.setText(QCoreApplication.translate("MainWindow", u"Next Scheduled Shutdown", None))
        self.left_panel_label.setText(QCoreApplication.translate("MainWindow", u"Time until next shutdown", None))
        self.hh_label.setText(QCoreApplication.translate("MainWindow", u"HH", None))
        self.mm_lebl.setText(QCoreApplication.translate("MainWindow", u"MM", None))
        self.ss_label.setText(QCoreApplication.translate("MainWindow", u"SS", None))
        self.api_label1.setText(QCoreApplication.translate("MainWindow", u"Serving web server at : ", None))
        self.scheduled_label_main.setText(QCoreApplication.translate("MainWindow", u"NO SHUTDOWN SCHEDULED", None))
        self.cancel_shutdown_button.setText(QCoreApplication.translate("MainWindow", u"Cancel Shutdown", None))
        self.api_server_link_button.setText(QCoreApplication.translate("MainWindow", u"http://0.0.0.0:5000", None))
        self.creator_label_main.setText(QCoreApplication.translate("MainWindow", u"Made with \u2764\ufe0f by tanmay sharma", None))
        self.predefined_minute_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"10m", None))
        self.predefined_minute_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"20m", None))
        self.predefined_minute_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"30m", None))
        self.predefined_minute_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"40m", None))
        self.predefined_minute_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"50m", None))
        self.predefined_minute_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"60m", None))

        self.predefined_hours_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"1h", None))
        self.predefined_hours_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"2h", None))
        self.predefined_hours_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"3h", None))
        self.predefined_hours_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"4h", None))
        self.predefined_hours_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"5h", None))
        self.predefined_hours_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"6h", None))
        self.predefined_hours_combo.setItemText(6, QCoreApplication.translate("MainWindow", u"7h", None))
        self.predefined_hours_combo.setItemText(7, QCoreApplication.translate("MainWindow", u"8h", None))
        self.predefined_hours_combo.setItemText(8, QCoreApplication.translate("MainWindow", u"9h", None))
        self.predefined_hours_combo.setItemText(9, QCoreApplication.translate("MainWindow", u"10h", None))
        self.predefined_hours_combo.setItemText(10, QCoreApplication.translate("MainWindow", u"11h", None))
        self.predefined_hours_combo.setItemText(11, QCoreApplication.translate("MainWindow", u"12h", None))
        self.predefined_hours_combo.setItemText(12, QCoreApplication.translate("MainWindow", u"13h", None))
        self.predefined_hours_combo.setItemText(13, QCoreApplication.translate("MainWindow", u"14h", None))
        self.predefined_hours_combo.setItemText(14, QCoreApplication.translate("MainWindow", u"15h", None))
        self.predefined_hours_combo.setItemText(15, QCoreApplication.translate("MainWindow", u"16h", None))
        self.predefined_hours_combo.setItemText(16, QCoreApplication.translate("MainWindow", u"17h", None))
        self.predefined_hours_combo.setItemText(17, QCoreApplication.translate("MainWindow", u"18h", None))
        self.predefined_hours_combo.setItemText(18, QCoreApplication.translate("MainWindow", u"19h", None))
        self.predefined_hours_combo.setItemText(19, QCoreApplication.translate("MainWindow", u"20h", None))
        self.predefined_hours_combo.setItemText(20, QCoreApplication.translate("MainWindow", u"21h", None))
        self.predefined_hours_combo.setItemText(21, QCoreApplication.translate("MainWindow", u"22h", None))
        self.predefined_hours_combo.setItemText(22, QCoreApplication.translate("MainWindow", u"23h", None))

        self.predefined_days_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"1d", None))
        self.predefined_days_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"2d", None))
        self.predefined_days_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"3d", None))
        self.predefined_days_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"4d", None))
        self.predefined_days_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"5d", None))
        self.predefined_days_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"6d", None))

        self.predefined_minute_button.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.right_panel_label_2.setText(QCoreApplication.translate("MainWindow", u"Select a Preset ", None))
        self.predefined_hours_button.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.predefined_days_button.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.left_panel_label_2.setText(QCoreApplication.translate("MainWindow", u"Your computer is up since", None))
        self.ss_label_2.setText(QCoreApplication.translate("MainWindow", u"SS", None))
        self.hh_label_2.setText(QCoreApplication.translate("MainWindow", u"HH", None))
        self.mm_lebl_2.setText(QCoreApplication.translate("MainWindow", u"MM", None))
        self.boot_time_label_main.setText(QCoreApplication.translate("MainWindow", u"Boot time : 11/27/2024, 12:49:45 PM", None))
    # retranslateUi

