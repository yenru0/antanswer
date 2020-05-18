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

from components.gui.option_ui import Widget_Option_Color
from components.gui.option_ui import Widget_Option_Font


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(545, 641)
        MainWindow.setStyleSheet(u"#MainWindow{\n"
"	background-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: rgb(255,255, 255);\n"
"}\n"
"\n"
"#sideStatus{\n"
"	background-color: rgb(255,255, 255);\n"
"}\n"
"")
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        self.actionreturn_to_manimenu = QAction(MainWindow)
        self.actionreturn_to_manimenu.setObjectName(u"actionreturn_to_manimenu")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u".QLabel#title{\n"
"	font: 25 14pt \"Malgun Gothic\";\n"
"}\n"
"\n"
".QLabel#down_version{\n"
"	font: 100 10pt \"Malgun Gothic\";\n"
"}\n"
"\n"
"#label_resultant{\n"
"	font: 100 bold 25pt \"Malgun Gothic\";\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"QPushButton{\n"
"	font: 25 bold 12pt \"Malgun Gothic\";\n"
"	background-color: white;\n"
"	border: 1px solid black;\n"
"	frameShape: panel;\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.page_enter = QWidget()
        self.page_enter.setObjectName(u"page_enter")
        self.page_enter.setStyleSheet(u"QPushButton{\n"
"	font: 25 bold 18pt \"Malgun Gothic\";\n"
"	background-color: white;\n"
"	border: 1px solid black;\n"
"	frameShape: panel;\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
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
        self.titleBtn_exit = QPushButton(self.page_enter)
        self.titleBtn_exit.setObjectName(u"titleBtn_exit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleBtn_exit.sizePolicy().hasHeightForWidth())
        self.titleBtn_exit.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Malgun Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.titleBtn_exit.setFont(font)
        self.titleBtn_exit.setStyleSheet(u"")

        self.titleBtns.addWidget(self.titleBtn_exit, 0, 2, 1, 1)

        self.titleBtn_option = QPushButton(self.page_enter)
        self.titleBtn_option.setObjectName(u"titleBtn_option")
        sizePolicy.setHeightForWidth(self.titleBtn_option.sizePolicy().hasHeightForWidth())
        self.titleBtn_option.setSizePolicy(sizePolicy)

        self.titleBtns.addWidget(self.titleBtn_option, 0, 1, 1, 1)

        self.titleBtn_run = QPushButton(self.page_enter)
        self.titleBtn_run.setObjectName(u"titleBtn_run")
        sizePolicy.setHeightForWidth(self.titleBtn_run.sizePolicy().hasHeightForWidth())
        self.titleBtn_run.setSizePolicy(sizePolicy)

        self.titleBtns.addWidget(self.titleBtn_run, 0, 0, 1, 1)


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
        self.page_setting.setStyleSheet(u"QLabel{\n"
"	font: 11pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton{\n"
"	font: 25 11pt \"Malgun Gothic\";\n"
"	background-color: white;\n"
"	border: 1px solid black;\n"
"	frameShape: panel;\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QPushButton#setting_btn_addfile{\n"
"	background-color:rgb(85, 170, 255);\n"
"	border: 1px solid black;\n"
"}\n"
"QPushButton#setting_btn_addfile:pressed{\n"
"	background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 1 rgb(85, 170, 255), stop: 0 rgb(46, 93, 140));\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.page_setting)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.setting_stage_table = QTableView(self.page_setting)
        self.setting_stage_table.setObjectName(u"setting_stage_table")
        sizePolicy1.setHeightForWidth(self.setting_stage_table.sizePolicy().hasHeightForWidth())
        self.setting_stage_table.setSizePolicy(sizePolicy1)
        self.setting_stage_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setting_stage_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setting_stage_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.gridLayout_2.addWidget(self.setting_stage_table, 2, 0, 1, 1)

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
        self.setting_list_file.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setting_list_file.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setting_list_file.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.setitem_file.addWidget(self.setting_list_file)


        self.gridLayout_2.addLayout(self.setitem_file, 1, 0, 1, 1)

        self.setting_btns_real = QHBoxLayout()
        self.setting_btns_real.setObjectName(u"setting_btns_real")
        self.setting_btn_real_run = QPushButton(self.page_setting)
        self.setting_btn_real_run.setObjectName(u"setting_btn_real_run")

        self.setting_btns_real.addWidget(self.setting_btn_real_run)

        self.setting_btn_real_gomenu = QPushButton(self.page_setting)
        self.setting_btn_real_gomenu.setObjectName(u"setting_btn_real_gomenu")

        self.setting_btns_real.addWidget(self.setting_btn_real_gomenu)


        self.gridLayout_2.addLayout(self.setting_btns_real, 3, 0, 1, 1)

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
        self.extend_normal = QWidget()
        self.extend_normal.setObjectName(u"extend_normal")
        self.extend_setting.addWidget(self.extend_normal)
        self.extend_c2 = QWidget()
        self.extend_c2.setObjectName(u"extend_c2")
        self.extend_setting.addWidget(self.extend_c2)

        self.setitem_extend.addWidget(self.extend_setting)


        self.gridLayout_2.addLayout(self.setitem_extend, 0, 0, 1, 1)

        self.pages.addWidget(self.page_setting)
        self.page_do = QWidget()
        self.page_do.setObjectName(u"page_do")
        self.page_do.setStyleSheet(u"#input{\n"
"	font: 25 11pt \"Malgun Gothic\";\n"
"	background-color: white;\n"
"	border: 1px solid black;\n"
"}\n"
"#log {\n"
"	font: 25 9pt \"Malgun Gothic\";\n"
"background-color: white;\n"
"}\n"
"#queston{\n"
"	background-color: white;\n"
"	border: 1px solid black;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.page_do)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.queston = QTextBrowser(self.page_do)
        self.queston.setObjectName(u"queston")
        font1 = QFont()
        font1.setFamily(u"13 Malgun Gothic")
        font1.setPointSize(12)
        font1.setItalic(False)
        self.queston.setFont(font1)
        self.queston.setFocusPolicy(Qt.NoFocus)
        self.queston.setAcceptRichText(False)
        self.queston.setTextInteractionFlags(Qt.NoTextInteraction)
        self.queston.setOpenLinks(False)

        self.verticalLayout_3.addWidget(self.queston)

        self.inputLayout = QHBoxLayout()
        self.inputLayout.setObjectName(u"inputLayout")
        self.input = QListWidget(self.page_do)
        __qlistwidgetitem = QListWidgetItem(self.input)
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.input)
        __qlistwidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem2 = QListWidgetItem(self.input)
        __qlistwidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.input.setObjectName(u"input")
        sizePolicy.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy)
        self.input.setAutoScroll(False)
        self.input.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.input.setTabKeyNavigation(True)
        self.input.setDragEnabled(True)
        self.input.setDragDropOverwriteMode(False)
        self.input.setDragDropMode(QAbstractItemView.DragDrop)
        self.input.setDefaultDropAction(Qt.MoveAction)
        self.input.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.input.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.inputLayout.addWidget(self.input)

        self.enter = QPushButton(self.page_do)
        self.enter.setObjectName(u"enter")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.enter.sizePolicy().hasHeightForWidth())
        self.enter.setSizePolicy(sizePolicy5)
        self.enter.setAutoDefault(True)

        self.inputLayout.addWidget(self.enter)

        self.inputLayout.setStretch(0, 3)
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
        self.log.setFocusPolicy(Qt.NoFocus)
        self.log.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.verticalLayout_3.addWidget(self.log)

        self.verticalLayout_3.setStretch(0, 23)
        self.verticalLayout_3.setStretch(1, 3)
        self.verticalLayout_3.setStretch(2, 3)
        self.pages.addWidget(self.page_do)
        self.page_resultant = QWidget()
        self.page_resultant.setObjectName(u"page_resultant")
        self.page_resultant.setStyleSheet(u"QLabel#label_resultant{\n"
"	font: 100 bold 25pt \"Malgun Gothic\";\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.page_resultant)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_resultant = QLabel(self.page_resultant)
        self.label_resultant.setObjectName(u"label_resultant")
        sizePolicy3.setHeightForWidth(self.label_resultant.sizePolicy().hasHeightForWidth())
        self.label_resultant.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamily(u"Malgun Gothic")
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.label_resultant.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_resultant)

        self.resultant_view = QTableView(self.page_resultant)
        self.resultant_view.setObjectName(u"resultant_view")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.resultant_view.sizePolicy().hasHeightForWidth())
        self.resultant_view.setSizePolicy(sizePolicy7)
        self.resultant_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.resultant_view.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.resultant_view.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_5.addWidget(self.resultant_view)

        self.resultant_btns = QGridLayout()
        self.resultant_btns.setObjectName(u"resultant_btns")
        self.resultant_btn_menu = QPushButton(self.page_resultant)
        self.resultant_btn_menu.setObjectName(u"resultant_btn_menu")

        self.resultant_btns.addWidget(self.resultant_btn_menu, 0, 2, 1, 1)

        self.resultant_btn_again = QPushButton(self.page_resultant)
        self.resultant_btn_again.setObjectName(u"resultant_btn_again")

        self.resultant_btns.addWidget(self.resultant_btn_again, 0, 0, 1, 1)

        self.resultant_btn_setting = QPushButton(self.page_resultant)
        self.resultant_btn_setting.setObjectName(u"resultant_btn_setting")
        font3 = QFont()
        font3.setFamily(u"Malgun Gothic")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.resultant_btn_setting.setFont(font3)

        self.resultant_btns.addWidget(self.resultant_btn_setting, 0, 1, 1, 1)

        self.resultant_btn_save = QPushButton(self.page_resultant)
        self.resultant_btn_save.setObjectName(u"resultant_btn_save")

        self.resultant_btns.addWidget(self.resultant_btn_save, 1, 0, 1, 1)

        self.resultant_btn_preference = QPushButton(self.page_resultant)
        self.resultant_btn_preference.setObjectName(u"resultant_btn_preference")

        self.resultant_btns.addWidget(self.resultant_btn_preference, 1, 1, 1, 1)

        self.resultant_btn_openthis = QPushButton(self.page_resultant)
        self.resultant_btn_openthis.setObjectName(u"resultant_btn_openthis")

        self.resultant_btns.addWidget(self.resultant_btn_openthis, 1, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.resultant_btns)

        self.pages.addWidget(self.page_resultant)
        self.page_option = QWidget()
        self.page_option.setObjectName(u"page_option")
        self.page_option.setStyleSheet(u"QScrollArea{\n"
"	background-color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
".QLabel{\n"
"	font: 25 10pt \"Malgun Gothic\";\n"
"}\n"
"\n"
".QFontComboBox{\n"
"	font: 25 9pt \"Malgun Gothic\";\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
".QSpinBox{\n"
"	font: 25 9pt \"Malgun Gothic\";\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.page_option)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.option_scrollarea = QScrollArea(self.page_option)
        self.option_scrollarea.setObjectName(u"option_scrollarea")
        self.option_scrollarea.setStyleSheet(u"#option_scrollarea_contents{\n"
"	background-color:white;\n"
"}\n"
"\n"
".QWidget{\n"
"	border: 1px solid black;\n"
"}")
        self.option_scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.option_scrollarea.setWidgetResizable(True)
        self.option_scrollarea_contents = QWidget()
        self.option_scrollarea_contents.setObjectName(u"option_scrollarea_contents")
        self.option_scrollarea_contents.setGeometry(QRect(0, 0, 355, 562))
        self.option_scrollarea_contents.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.option_scrollarea_contents)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(4, 4, 4, 4)
        self.option_font_queston = Widget_Option_Font(self.option_scrollarea_contents)
        self.option_font_queston.setObjectName(u"option_font_queston")
        self._3 = QGridLayout(self.option_font_queston)
        self._3.setObjectName(u"_3")

        self.verticalLayout_7.addWidget(self.option_font_queston)

        self.option_font_input = Widget_Option_Font(self.option_scrollarea_contents)
        self.option_font_input.setObjectName(u"option_font_input")
        self._4 = QGridLayout(self.option_font_input)
        self._4.setObjectName(u"_4")

        self.verticalLayout_7.addWidget(self.option_font_input)

        self.option_font_lcptd_file = Widget_Option_Font(self.option_scrollarea_contents)
        self.option_font_lcptd_file.setObjectName(u"option_font_lcptd_file")
        self._2 = QGridLayout(self.option_font_lcptd_file)
        self._2.setObjectName(u"_2")

        self.verticalLayout_7.addWidget(self.option_font_lcptd_file)

        self.option_color_lcptd_progress = Widget_Option_Color(self.option_scrollarea_contents)
        self.option_color_lcptd_progress.setObjectName(u"option_color_lcptd_progress")
        self._5 = QGridLayout(self.option_color_lcptd_progress)
        self._5.setObjectName(u"_5")

        self.verticalLayout_7.addWidget(self.option_color_lcptd_progress)

        self.option_color_lcptd_rategress = Widget_Option_Color(self.option_scrollarea_contents)
        self.option_color_lcptd_rategress.setObjectName(u"option_color_lcptd_rategress")
        self._6 = QGridLayout(self.option_color_lcptd_rategress)
        self._6.setObjectName(u"_6")

        self.verticalLayout_7.addWidget(self.option_color_lcptd_rategress)

        self.option_color_lcptd_cwgress_c = Widget_Option_Color(self.option_scrollarea_contents)
        self.option_color_lcptd_cwgress_c.setObjectName(u"option_color_lcptd_cwgress_c")
        self._7 = QGridLayout(self.option_color_lcptd_cwgress_c)
        self._7.setObjectName(u"_7")

        self.verticalLayout_7.addWidget(self.option_color_lcptd_cwgress_c)

        self.option_color_lcptd_cwgress_w = Widget_Option_Color(self.option_scrollarea_contents)
        self.option_color_lcptd_cwgress_w.setObjectName(u"option_color_lcptd_cwgress_w")
        self._8 = QGridLayout(self.option_color_lcptd_cwgress_w)
        self._8.setObjectName(u"_8")

        self.verticalLayout_7.addWidget(self.option_color_lcptd_cwgress_w)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.option_scrollarea.setWidget(self.option_scrollarea_contents)

        self.verticalLayout_6.addWidget(self.option_scrollarea)

        self.pages.addWidget(self.page_option)

        self.verticalLayout.addWidget(self.pages)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 545, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.sideStatus = QDockWidget(MainWindow)
        self.sideStatus.setObjectName(u"sideStatus")
        self.sideStatus.setStyleSheet(u"#sideStatus::title{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid black;\n"
"	\n"
"}\n"
"\n"
"#sideStatus{\n"
"	font: 11pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"}")
        self.sideStatus.setFloating(False)
        self.lcptd = QWidget()
        self.lcptd.setObjectName(u"lcptd")
        self.lcptd.setStyleSheet(u"#lcptd {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid black;\n"
"	border-top: none;\n"
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
"}\n"
"\n"
"\n"
"#lcptd_progress{\n"
"	\n"
"	font: 25 15pt \"Malgun Gothic\";\n"
"	border: 1.2px solid black;\n"
"	border-radius: 4px;\n"
"	text-align: center;\n"
"}\n"
"#lcptd_progress::chunk{background-color: rgb(0, 170, 255)}\n"
"#lcptd_rategress{\n"
"	\n"
"	font: 25 15pt \"Malgun Gothic\";\n"
"	border: 1.2px solid black;\n"
"	border-radius: 4px;\n"
"	text-align: center;\n"
"}\n"
"#lcptd_rategress::chunk{backgroun"
                        "d-color: rgb(120, 230, 20)}\n"
"\n"
"#lcptd_cwgress{\n"
"	\n"
"	font: 25 15pt \"Malgun Gothic\";\n"
"	border: 1.2px solid black;\n"
"	border-radius: 4px;\n"
"	text-align: center;\n"
"	background-color: rgb(255, 0, 0)\n"
"}\n"
"#lcptd_cwgress::chunk{background-color: rgb(255, 200, 20);}")
        self.verticalLayout_2 = QVBoxLayout(self.lcptd)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lcptd_file = QLineEdit(self.lcptd)
        self.lcptd_file.setObjectName(u"lcptd_file")
        self.lcptd_file.setFocusPolicy(Qt.NoFocus)
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
        self.lcptd_progress.setStyleSheet(u"")
        self.lcptd_progress.setMaximum(100)
        self.lcptd_progress.setValue(10)
        self.lcptd_progress.setTextVisible(True)

        self.verticalLayout_2.addWidget(self.lcptd_progress)

        self.lcptd_rategress = QProgressBar(self.lcptd)
        self.lcptd_rategress.setObjectName(u"lcptd_rategress")
        self.lcptd_rategress.setStyleSheet(u"")
        self.lcptd_rategress.setValue(25)

        self.verticalLayout_2.addWidget(self.lcptd_rategress)

        self.lcptd_cwgress = QProgressBar(self.lcptd)
        self.lcptd_cwgress.setObjectName(u"lcptd_cwgress")
        self.lcptd_cwgress.setMaximum(2)
        self.lcptd_cwgress.setValue(1)

        self.verticalLayout_2.addWidget(self.lcptd_cwgress)

        self.lcptd_voidspacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.lcptd_voidspacer)

        self.sideStatus.setWidget(self.lcptd)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.sideStatus)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionexit)
        self.menu.addAction(self.actionreturn_to_manimenu)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(4)
        self.extend_setting.setCurrentIndex(1)
        self.enter.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"antanswer-python-pyside2", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"\ub098\uac00\uae30", None))
        self.actionreturn_to_manimenu.setText(QCoreApplication.translate("MainWindow", u"\uba54\uc778\uba54\ub274\ub85c \ub3cc\uc544\uac00\uae30", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Antanswer</span><span style=\" font-weight:600; vertical-align:sub;\">(pyside2)</span></p></body></html>", None))
        self.titleBtn_exit.setText(QCoreApplication.translate("MainWindow", u"\ub098\uac00\uae30", None))
        self.titleBtn_option.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.titleBtn_run.setText(QCoreApplication.translate("MainWindow", u"\uc2e4\ud589", None))
        self.down_version.setText(QCoreApplication.translate("MainWindow", u"version: loading", None))
        self.setting_btn_addfile.setText(QCoreApplication.translate("MainWindow", u" \ud30c\uc77c \ucd94\uac00 ", None))
        self.setting_btn_real_run.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.setting_btn_real_gomenu.setText(QCoreApplication.translate("MainWindow", u"\ub3cc\uc544\uac00\uae30", None))
        self.setting_label_extend.setText(QCoreApplication.translate("MainWindow", u" \ud655\uc7a5 \uc124\uc815 ", None))

        __sortingEnabled = self.input.isSortingEnabled()
        self.input.setSortingEnabled(False)
        self.input.setSortingEnabled(__sortingEnabled)

        self.enter.setText(QCoreApplication.translate("MainWindow", u"\uc785\ub825", None))

        __sortingEnabled1 = self.log.isSortingEnabled()
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
        self.log.setSortingEnabled(__sortingEnabled1)

        self.label_resultant.setText(QCoreApplication.translate("MainWindow", u"\uacb0\uacfc:", None))
        self.resultant_btn_menu.setText(QCoreApplication.translate("MainWindow", u"\uba54\ub274\ub85c \ub3cc\uc544\uac00\uae30", None))
        self.resultant_btn_again.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\uc2dc \uc2dc\ub3c4", None))
        self.resultant_btn_setting.setText(QCoreApplication.translate("MainWindow", u"\uc2e4\ud589 \uc124\uc815\uc73c\ub85c", None))
        self.resultant_btn_save.setText(QCoreApplication.translate("MainWindow", u"\uc774 \uacb0\uacfc \uc800\uc7a5", None))
        self.resultant_btn_preference.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud638 \ud30c\uc77c \uc5f4\uae30", None))
        self.resultant_btn_openthis.setText(QCoreApplication.translate("MainWindow", u"\uc774 anw \ud30c\uc77c \uc5f4\uae30", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\uae30\ub2a5", None))
        self.sideStatus.setWindowTitle(QCoreApplication.translate("MainWindow", u"\uc0c1\ud0dc\ucc3d(lcptd)", None))
        self.lcptd_file.setText(QCoreApplication.translate("MainWindow", u"test.dnwouvndowdnbovwdbovwdbowdvnovwdn.zip", None))
        self.lcptd_progress.setFormat(QCoreApplication.translate("MainWindow", u"%p%:%v", None))
        self.lcptd_cwgress.setFormat(QCoreApplication.translate("MainWindow", u"%v:", None))
    # retranslateUi

