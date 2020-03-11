# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 620)
        MainWindow.setStyleSheet(u"#MainWindow{\n"
"	background-color: rgb(247, 247, 247)\n"
"}")
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        self.actionreturn_to_manimenu = QAction(MainWindow)
        self.actionreturn_to_manimenu.setObjectName(u"actionreturn_to_manimenu")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"	background-color: rgb(247,247, 247);\n"
"}\n"
"\n"
"#page_do{\n"
"	background-color: rgb(247,247, 247);\n"
"}\n"
"\n"
"#queston{\n"
"	background-color: white;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"#log {\n"
"	font: 25 11pt \"Malgun Gothic\";\n"
"background-color: white;\n"
"}\n"
"\n"
"#input{\n"
"	font: 25 11pt \"Malgun Gothic\";\n"
"	background-color: white;\n"
"}\n"
"\n"
"#enter{\n"
"	font: 25 bold 12pt \"Malgun Gothic\";\n"
"	background-color: white;\n"
"}\n"
"\n"
"#titleBtn_exit, #titleBtn_option, #titleBtn_run{\n"
"	font: 25 bold 18pt \"Malgun Gothic\";\n"
"	background-color: white;\n"
"	\n"
"}\n"
"\n"
".QLabel#title{\n"
"	font: 25 14pt \"Malgun Gothic\";\n"
"}\n"
"\n"
".QLabel#down_version{\n"
"	font: 100 10pt \"Malgun Gothic\";\n"
"}\n"
"\n"
"#setting_btn_real_run, #setting_btn_addfile, #setting_label_extend\n"
", #setting_label_run, #setting_runbox, #setting_btn_real_gomenu{\n"
"	font: 100 11pt \"Malgun Gothic\";\n"
"}\n"
"\n"
"#resultant_btn_again, #resultant_btn_setting, #"
                        "resultant_btn_menu{\n"
"	font: 100 14pt \"Malgun Gothic\";\n"
"}\n"
"\n"
"#label_resultant{\n"
"	font: 100 bold 24pt \"Malgun Gothic\";\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.page_enter = QWidget()
        self.page_enter.setObjectName(u"page_enter")
        self.verticalLayout_4 = QVBoxLayout(self.page_enter)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.title = QLabel(self.page_enter)
        self.title.setObjectName(u"title")
        self.title.setTextFormat(Qt.RichText)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.title)

        self.titleBtns = QGridLayout()
        self.titleBtns.setSpacing(10)
        self.titleBtns.setObjectName(u"titleBtns")
        self.titleBtns.setContentsMargins(10, 10, 10, 10)
        self.titleBtn_run = QPushButton(self.page_enter)
        self.titleBtn_run.setObjectName(u"titleBtn_run")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleBtn_run.sizePolicy().hasHeightForWidth())
        self.titleBtn_run.setSizePolicy(sizePolicy)

        self.titleBtns.addWidget(self.titleBtn_run, 0, 0, 1, 1)

        self.titleBtn_option = QPushButton(self.page_enter)
        self.titleBtn_option.setObjectName(u"titleBtn_option")
        sizePolicy.setHeightForWidth(self.titleBtn_option.sizePolicy().hasHeightForWidth())
        self.titleBtn_option.setSizePolicy(sizePolicy)

        self.titleBtns.addWidget(self.titleBtn_option, 0, 1, 1, 1)

        self.titleBtn_exit = QPushButton(self.page_enter)
        self.titleBtn_exit.setObjectName(u"titleBtn_exit")
        sizePolicy.setHeightForWidth(self.titleBtn_exit.sizePolicy().hasHeightForWidth())
        self.titleBtn_exit.setSizePolicy(sizePolicy)

        self.titleBtns.addWidget(self.titleBtn_exit, 0, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.titleBtns)

        self.down_version = QLabel(self.page_enter)
        self.down_version.setObjectName(u"down_version")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.down_version.sizePolicy().hasHeightForWidth())
        self.down_version.setSizePolicy(sizePolicy1)
        self.down_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.down_version)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 1)
        self.pages.addWidget(self.page_enter)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.gridLayout_2 = QGridLayout(self.page_setting)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.setitem_file = QHBoxLayout()
        self.setitem_file.setObjectName(u"setitem_file")
        self.setting_layout_btn_addfile = QVBoxLayout()
        self.setting_layout_btn_addfile.setSpacing(0)
        self.setting_layout_btn_addfile.setObjectName(u"setting_layout_btn_addfile")
        self.setting_btn_addfile_vSpacer1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.setting_layout_btn_addfile.addItem(self.setting_btn_addfile_vSpacer1)

        self.setting_btn_addfile = QPushButton(self.page_setting)
        self.setting_btn_addfile.setObjectName(u"setting_btn_addfile")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.setting_btn_addfile.sizePolicy().hasHeightForWidth())
        self.setting_btn_addfile.setSizePolicy(sizePolicy2)

        self.setting_layout_btn_addfile.addWidget(self.setting_btn_addfile)

        self.setting_btn_addfile_vSpacer2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.setting_layout_btn_addfile.addItem(self.setting_btn_addfile_vSpacer2)


        self.setitem_file.addLayout(self.setting_layout_btn_addfile)

        self.setting_list_file = QTableView(self.page_setting)
        self.setting_list_file.setObjectName(u"setting_list_file")
        sizePolicy1.setHeightForWidth(self.setting_list_file.sizePolicy().hasHeightForWidth())
        self.setting_list_file.setSizePolicy(sizePolicy1)

        self.setitem_file.addWidget(self.setting_list_file)


        self.gridLayout_2.addLayout(self.setitem_file, 2, 0, 1, 1)

        self.setitem_extend = QHBoxLayout()
        self.setitem_extend.setObjectName(u"setitem_extend")
        self.setting_label_extend = QLabel(self.page_setting)
        self.setting_label_extend.setObjectName(u"setting_label_extend")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.setting_label_extend.sizePolicy().hasHeightForWidth())
        self.setting_label_extend.setSizePolicy(sizePolicy3)

        self.setitem_extend.addWidget(self.setting_label_extend)

        self.extend_setting = QStackedWidget(self.page_setting)
        self.extend_setting.setObjectName(u"extend_setting")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.extend_setting.sizePolicy().hasHeightForWidth())
        self.extend_setting.setSizePolicy(sizePolicy4)
        self.extend_compiled = QWidget()
        self.extend_compiled.setObjectName(u"extend_compiled")
        self.extend_setting.addWidget(self.extend_compiled)
        self.extend_direct = QWidget()
        self.extend_direct.setObjectName(u"extend_direct")
        self.extend_setting.addWidget(self.extend_direct)

        self.setitem_extend.addWidget(self.extend_setting)


        self.gridLayout_2.addLayout(self.setitem_extend, 1, 0, 1, 1)

        self.setitem_runmode = QHBoxLayout()
        self.setitem_runmode.setObjectName(u"setitem_runmode")
        self.setting_label_run = QLabel(self.page_setting)
        self.setting_label_run.setObjectName(u"setting_label_run")
        sizePolicy3.setHeightForWidth(self.setting_label_run.sizePolicy().hasHeightForWidth())
        self.setting_label_run.setSizePolicy(sizePolicy3)

        self.setitem_runmode.addWidget(self.setting_label_run)

        self.setting_runbox = QComboBox(self.page_setting)
        self.setting_runbox.addItem("")
        self.setting_runbox.addItem("")
        self.setting_runbox.setObjectName(u"setting_runbox")
        self.setting_runbox.setMaxVisibleItems(12)

        self.setitem_runmode.addWidget(self.setting_runbox)


        self.gridLayout_2.addLayout(self.setitem_runmode, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.setting_btn_real_run = QPushButton(self.page_setting)
        self.setting_btn_real_run.setObjectName(u"setting_btn_real_run")

        self.horizontalLayout.addWidget(self.setting_btn_real_run)

        self.setting_btn_real_gomenu = QPushButton(self.page_setting)
        self.setting_btn_real_gomenu.setObjectName(u"setting_btn_real_gomenu")

        self.horizontalLayout.addWidget(self.setting_btn_real_gomenu)


        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.setting_stage_table = QTableView(self.page_setting)
        self.setting_stage_table.setObjectName(u"setting_stage_table")
        sizePolicy1.setHeightForWidth(self.setting_stage_table.sizePolicy().hasHeightForWidth())
        self.setting_stage_table.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.setting_stage_table, 3, 0, 1, 1)

        self.gridLayout_2.setRowMinimumHeight(0, 1)
        self.gridLayout_2.setRowMinimumHeight(1, 1)
        self.gridLayout_2.setRowMinimumHeight(2, 1)
        self.gridLayout_2.setRowMinimumHeight(3, 1)
        self.gridLayout_2.setRowMinimumHeight(4, 1)
        self.pages.addWidget(self.page_setting)
        self.page_do = QWidget()
        self.page_do.setObjectName(u"page_do")
        self.verticalLayout_3 = QVBoxLayout(self.page_do)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.queston = QTextBrowser(self.page_do)
        self.queston.setObjectName(u"queston")
        font = QFont()
        font.setFamily(u"13 Malgun Gothic")
        font.setPointSize(12)
        font.setItalic(False)
        self.queston.setFont(font)
        self.queston.setAcceptRichText(False)
        self.queston.setOpenLinks(False)

        self.verticalLayout_3.addWidget(self.queston)

        self.inputLayout = QHBoxLayout()
        self.inputLayout.setObjectName(u"inputLayout")
        self.input = QLineEdit(self.page_do)
        self.input.setObjectName(u"input")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy5)

        self.inputLayout.addWidget(self.input)

        self.enter = QPushButton(self.page_do)
        self.enter.setObjectName(u"enter")
        sizePolicy5.setHeightForWidth(self.enter.sizePolicy().hasHeightForWidth())
        self.enter.setSizePolicy(sizePolicy5)

        self.inputLayout.addWidget(self.enter)

        self.inputLayout.setStretch(0, 4)
        self.inputLayout.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.inputLayout)

        self.log = QListWidget(self.page_do)
        QListWidgetItem(self.log)
        QListWidgetItem(self.log)
        QListWidgetItem(self.log)
        QListWidgetItem(self.log)
        QListWidgetItem(self.log)
        self.log.setObjectName(u"log")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        self.log.setSizePolicy(sizePolicy6)

        self.verticalLayout_3.addWidget(self.log)

        self.verticalLayout_3.setStretch(0, 23)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 5)
        self.pages.addWidget(self.page_do)
        self.page_resultant = QWidget()
        self.page_resultant.setObjectName(u"page_resultant")
        self.verticalLayout_5 = QVBoxLayout(self.page_resultant)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_resultant = QLabel(self.page_resultant)
        self.label_resultant.setObjectName(u"label_resultant")
        sizePolicy3.setHeightForWidth(self.label_resultant.sizePolicy().hasHeightForWidth())
        self.label_resultant.setSizePolicy(sizePolicy3)

        self.verticalLayout_5.addWidget(self.label_resultant)

        self.resultant_view = QTableView(self.page_resultant)
        self.resultant_view.setObjectName(u"resultant_view")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.resultant_view.sizePolicy().hasHeightForWidth())
        self.resultant_view.setSizePolicy(sizePolicy7)

        self.verticalLayout_5.addWidget(self.resultant_view)

        self.resultant_gobtns = QHBoxLayout()
        self.resultant_gobtns.setObjectName(u"resultant_gobtns")
        self.resultant_btn_again = QPushButton(self.page_resultant)
        self.resultant_btn_again.setObjectName(u"resultant_btn_again")

        self.resultant_gobtns.addWidget(self.resultant_btn_again)

        self.resultant_btn_setting = QPushButton(self.page_resultant)
        self.resultant_btn_setting.setObjectName(u"resultant_btn_setting")
        font1 = QFont()
        font1.setFamily(u"Malgun Gothic")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(12)
        self.resultant_btn_setting.setFont(font1)

        self.resultant_gobtns.addWidget(self.resultant_btn_setting)

        self.resultant_btn_menu = QPushButton(self.page_resultant)
        self.resultant_btn_menu.setObjectName(u"resultant_btn_menu")

        self.resultant_gobtns.addWidget(self.resultant_btn_menu)


        self.verticalLayout_5.addLayout(self.resultant_gobtns)

        self.pages.addWidget(self.page_resultant)
        self.page_option = QWidget()
        self.page_option.setObjectName(u"page_option")
        self.verticalLayout_6 = QVBoxLayout(self.page_option)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.option_scrollarea = QScrollArea(self.page_option)
        self.option_scrollarea.setObjectName(u"option_scrollarea")
        self.option_scrollarea.setWidgetResizable(True)
        self.option_scrollarea_contents = QWidget()
        self.option_scrollarea_contents.setObjectName(u"option_scrollarea_contents")
        self.option_scrollarea_contents.setGeometry(QRect(0, 0, 495, 559))
        self.gridLayout_3 = QGridLayout(self.option_scrollarea_contents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.templeft = QLabel(self.option_scrollarea_contents)
        self.templeft.setObjectName(u"templeft")

        self.gridLayout_3.addWidget(self.templeft, 0, 0, 1, 1)

        self.tempright = QLabel(self.option_scrollarea_contents)
        self.tempright.setObjectName(u"tempright")

        self.gridLayout_3.addWidget(self.tempright, 0, 1, 1, 1)

        self.option_scrollarea.setWidget(self.option_scrollarea_contents)

        self.verticalLayout_6.addWidget(self.option_scrollarea)

        self.pages.addWidget(self.page_option)

        self.gridLayout.addWidget(self.pages, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 680, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.sideStatus = QDockWidget(MainWindow)
        self.sideStatus.setObjectName(u"sideStatus")
        self.sideStatus.setFloating(False)
        self.lcptd = QWidget()
        self.lcptd.setObjectName(u"lcptd")
        self.lcptd.setStyleSheet(u"#lcptd {\n"
"	background-color: rgb(247, 247, 247);\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QLabel {\n"
"	font: 25 18pt \"Malgun Gothic\";\n"
"	font-weight: bold;\n"
"}\n"
"\n"
".QLabel#percent {\n"
"	font: 25 28pt \"Malgun Gothic\";\n"
"	font-weight: bold;\n"
"}\n"
".QLineEdit#lcptd_file {\n"
"	font: 25 12pt \"Malgun Gothic\";\n"
"	background-color:rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"}\n"
"\n"
"#correct_layout {\n"
"	background-color: rgba(255, 255, 255, 0)\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.lcptd)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lcptd_file = QLineEdit(self.lcptd)
        self.lcptd_file.setObjectName(u"lcptd_file")
        self.lcptd_file.setEchoMode(QLineEdit.Normal)
        self.lcptd_file.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.lcptd_file)

        self.lcptd_progress = QProgressBar(self.lcptd)
        self.lcptd_progress.setObjectName(u"lcptd_progress")
        sizePolicy1.setHeightForWidth(self.lcptd_progress.sizePolicy().hasHeightForWidth())
        self.lcptd_progress.setSizePolicy(sizePolicy1)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(170, 0, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(213, 127, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(191, 63, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(85, 0, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(113, 0, 170, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush7 = QBrush(QColor(212, 127, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.lcptd_progress.setPalette(palette)
        self.lcptd_progress.setStyleSheet(u"#lcptd_progress{\n"
"	\n"
"	font: 25 bold 11pt \"Malgun Gothic\";\n"
"}")
        self.lcptd_progress.setMaximum(1000)
        self.lcptd_progress.setValue(111)
        self.lcptd_progress.setTextVisible(True)

        self.verticalLayout_2.addWidget(self.lcptd_progress)

        self.lcptd_count = QHBoxLayout()
        self.lcptd_count.setObjectName(u"lcptd_count")
        self.di_label_count = QLabel(self.lcptd)
        self.di_label_count.setObjectName(u"di_label_count")
        sizePolicy5.setHeightForWidth(self.di_label_count.sizePolicy().hasHeightForWidth())
        self.di_label_count.setSizePolicy(sizePolicy5)

        self.lcptd_count.addWidget(self.di_label_count)

        self.di_lcd_count = QLCDNumber(self.lcptd)
        self.di_lcd_count.setObjectName(u"di_lcd_count")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.di_lcd_count.sizePolicy().hasHeightForWidth())
        self.di_lcd_count.setSizePolicy(sizePolicy8)
        self.di_lcd_count.setFrameShape(QFrame.NoFrame)
        self.di_lcd_count.setSmallDecimalPoint(True)
        self.di_lcd_count.setDigitCount(2)
        self.di_lcd_count.setSegmentStyle(QLCDNumber.Flat)

        self.lcptd_count.addWidget(self.di_lcd_count)

        self.lcptd_count.setStretch(0, 1)
        self.lcptd_count.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.lcptd_count)

        self.lcptd_exact = QHBoxLayout()
        self.lcptd_exact.setObjectName(u"lcptd_exact")
        self.di_label_exact = QLabel(self.lcptd)
        self.di_label_exact.setObjectName(u"di_label_exact")
        sizePolicy5.setHeightForWidth(self.di_label_exact.sizePolicy().hasHeightForWidth())
        self.di_label_exact.setSizePolicy(sizePolicy5)

        self.lcptd_exact.addWidget(self.di_label_exact)

        self.di_lcd_exact = QLCDNumber(self.lcptd)
        self.di_lcd_exact.setObjectName(u"di_lcd_exact")
        sizePolicy8.setHeightForWidth(self.di_lcd_exact.sizePolicy().hasHeightForWidth())
        self.di_lcd_exact.setSizePolicy(sizePolicy8)
        font2 = QFont()
        font2.setPointSize(20)
        self.di_lcd_exact.setFont(font2)
        self.di_lcd_exact.setStyleSheet(u"font-size: 12")
        self.di_lcd_exact.setFrameShape(QFrame.NoFrame)
        self.di_lcd_exact.setSmallDecimalPoint(True)
        self.di_lcd_exact.setDigitCount(2)
        self.di_lcd_exact.setSegmentStyle(QLCDNumber.Flat)

        self.lcptd_exact.addWidget(self.di_lcd_exact)

        self.lcptd_exact.setStretch(0, 1)
        self.lcptd_exact.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.lcptd_exact)

        self.lcptd_wrong = QHBoxLayout()
        self.lcptd_wrong.setObjectName(u"lcptd_wrong")
        self.di_label_wrong = QLabel(self.lcptd)
        self.di_label_wrong.setObjectName(u"di_label_wrong")
        sizePolicy5.setHeightForWidth(self.di_label_wrong.sizePolicy().hasHeightForWidth())
        self.di_label_wrong.setSizePolicy(sizePolicy5)

        self.lcptd_wrong.addWidget(self.di_label_wrong)

        self.di_lcd_wrong = QLCDNumber(self.lcptd)
        self.di_lcd_wrong.setObjectName(u"di_lcd_wrong")
        sizePolicy8.setHeightForWidth(self.di_lcd_wrong.sizePolicy().hasHeightForWidth())
        self.di_lcd_wrong.setSizePolicy(sizePolicy8)
        self.di_lcd_wrong.setFrameShape(QFrame.NoFrame)
        self.di_lcd_wrong.setSmallDecimalPoint(True)
        self.di_lcd_wrong.setDigitCount(2)
        self.di_lcd_wrong.setSegmentStyle(QLCDNumber.Flat)

        self.lcptd_wrong.addWidget(self.di_lcd_wrong)

        self.lcptd_wrong.setStretch(0, 1)
        self.lcptd_wrong.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.lcptd_wrong)

        self.lcptd_rate = QHBoxLayout()
        self.lcptd_rate.setObjectName(u"lcptd_rate")
        self.di_label_rate = QLabel(self.lcptd)
        self.di_label_rate.setObjectName(u"di_label_rate")
        sizePolicy5.setHeightForWidth(self.di_label_rate.sizePolicy().hasHeightForWidth())
        self.di_label_rate.setSizePolicy(sizePolicy5)

        self.lcptd_rate.addWidget(self.di_label_rate)

        self.di_lcd_rate = QLCDNumber(self.lcptd)
        self.di_lcd_rate.setObjectName(u"di_lcd_rate")
        sizePolicy8.setHeightForWidth(self.di_lcd_rate.sizePolicy().hasHeightForWidth())
        self.di_lcd_rate.setSizePolicy(sizePolicy8)
        self.di_lcd_rate.setFrameShape(QFrame.NoFrame)
        self.di_lcd_rate.setSmallDecimalPoint(True)
        self.di_lcd_rate.setDigitCount(4)
        self.di_lcd_rate.setSegmentStyle(QLCDNumber.Flat)
        self.di_lcd_rate.setProperty("value", 83.579999999999998)

        self.lcptd_rate.addWidget(self.di_lcd_rate)

        self.percent = QLabel(self.lcptd)
        self.percent.setObjectName(u"percent")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.percent.sizePolicy().hasHeightForWidth())
        self.percent.setSizePolicy(sizePolicy9)

        self.lcptd_rate.addWidget(self.percent)

        self.lcptd_rate.setStretch(0, 2)
        self.lcptd_rate.setStretch(1, 3)
        self.lcptd_rate.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.lcptd_rate)

        self.sideStatus.setWidget(self.lcptd)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.sideStatus)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionexit)
        self.menu.addAction(self.actionreturn_to_manimenu)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)
        self.extend_setting.setCurrentIndex(0)
        self.setting_runbox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"antanswer-python-pyside2", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.actionreturn_to_manimenu.setText(QCoreApplication.translate("MainWindow", u"return to mainmenu", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Antanswer Python</span><span style=\" font-size:14pt; font-weight:600; vertical-align:sub;\">(pyside2)</span></p></body></html>", None))
        self.titleBtn_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.titleBtn_option.setText(QCoreApplication.translate("MainWindow", u"Option", None))
        self.titleBtn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.down_version.setText(QCoreApplication.translate("MainWindow", u"version: loading", None))
        self.setting_btn_addfile.setText(QCoreApplication.translate("MainWindow", u"add file", None))
        self.setting_label_extend.setText(QCoreApplication.translate("MainWindow", u"extend setting", None))
        self.setting_label_run.setText(QCoreApplication.translate("MainWindow", u"run mode", None))
        self.setting_runbox.setItemText(0, QCoreApplication.translate("MainWindow", u"compiled", None))
        self.setting_runbox.setItemText(1, QCoreApplication.translate("MainWindow", u"direct", None))

        self.setting_btn_real_run.setText(QCoreApplication.translate("MainWindow", u"run", None))
        self.setting_btn_real_gomenu.setText(QCoreApplication.translate("MainWindow", u"return to mainmenu", None))
        self.queston.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'13 Malgun Gothic'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Malgun Gothic'; font-size:14pt; font-weight:600;\">Test Grap is the tools that I test this antanswer gui, Test Grab consists of HTML text, but it is UNSTABLE</span></p></body></html>", None))
        self.input.setText(QCoreApplication.translate("MainWindow", u"TestInput Is test dragon. Imagine the Text Dragon. This is Very Terrific Land Dragon", None))
        self.enter.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))

        __sortingEnabled = self.log.isSortingEnabled()
        self.log.setSortingEnabled(False)
        ___qlistwidgetitem = self.log.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Test Log is the log.", None));
        ___qlistwidgetitem1 = self.log.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"TestLog1", None));
        ___qlistwidgetitem2 = self.log.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"It is made by tree that was made in Korea. But Actually, It is harvested in Chinese.", None));
        ___qlistwidgetitem3 = self.log.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Kanobe Empesus decide the warl.", None));
        ___qlistwidgetitem4 = self.log.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Laufghart", None));
        self.log.setSortingEnabled(__sortingEnabled)

        self.label_resultant.setText(QCoreApplication.translate("MainWindow", u"Result:", None))
        self.resultant_btn_again.setText(QCoreApplication.translate("MainWindow", u"try again", None))
        self.resultant_btn_setting.setText(QCoreApplication.translate("MainWindow", u"back to setting", None))
        self.resultant_btn_menu.setText(QCoreApplication.translate("MainWindow", u"return to menu", None))
        self.templeft.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.tempright.setText(QCoreApplication.translate("MainWindow", u"yenru0", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"actions", None))
        self.sideStatus.setWindowTitle(QCoreApplication.translate("MainWindow", u"status", None))
        self.lcptd_file.setText(QCoreApplication.translate("MainWindow", u"test.dnwouvndowdnbovwdbovwdbowdvnovwdn.zip", None))
        self.di_label_count.setText(QCoreApplication.translate("MainWindow", u"Count", None))
        self.di_label_exact.setText(QCoreApplication.translate("MainWindow", u"Exact", None))
        self.di_label_wrong.setText(QCoreApplication.translate("MainWindow", u"Wrong", None))
        self.di_label_rate.setText(QCoreApplication.translate("MainWindow", u"Rate", None))
        self.percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
    # retranslateUi

