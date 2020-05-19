# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Tue May 19 21:41:05 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 641)
        MainWindow.setStyleSheet("#MainWindow{\n"
"    background-color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"#centralwidget{\n"
"    background-color: rgb(255,255, 255);\n"
"}\n"
"\n"
"#sideStatus{\n"
"    background-color: rgb(255,255, 255);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(".QLabel#title{\n"
"    font: 25 14pt \"Malgun Gothic\";\n"
"}\n"
"\n"
".QLabel#down_version{\n"
"    font: 100 10pt \"Malgun Gothic\";\n"
"}\n"
"\n"
"#label_resultant{\n"
"    font: 100 bold 25pt \"Malgun Gothic\";\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pages = QtWidgets.QStackedWidget(self.centralwidget)
        self.pages.setStyleSheet("QPushButton{\n"
"    font: 25 bold 12pt \"Malgun Gothic\";\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    frameShape: panel;\n"
"    \n"
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
        self.pages.setObjectName("pages")
        self.page_enter = QtWidgets.QWidget()
        self.page_enter.setStyleSheet("QPushButton{\n"
"    font: 25 bold 18pt \"Malgun Gothic\";\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    frameShape: panel;\n"
"    \n"
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
        self.page_enter.setObjectName("page_enter")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_enter)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.title = QtWidgets.QLabel(self.page_enter)
        self.title.setTextFormat(QtCore.Qt.RichText)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout_4.addWidget(self.title)
        self.titleBtns = QtWidgets.QGridLayout()
        self.titleBtns.setSpacing(10)
        self.titleBtns.setContentsMargins(10, 10, 10, 10)
        self.titleBtns.setObjectName("titleBtns")
        self.titleBtn_exit = QtWidgets.QPushButton(self.page_enter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleBtn_exit.sizePolicy().hasHeightForWidth())
        self.titleBtn_exit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(18)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.titleBtn_exit.setFont(font)
        self.titleBtn_exit.setStyleSheet("")
        self.titleBtn_exit.setObjectName("titleBtn_exit")
        self.titleBtns.addWidget(self.titleBtn_exit, 0, 2, 1, 1)
        self.titleBtn_option = QtWidgets.QPushButton(self.page_enter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleBtn_option.sizePolicy().hasHeightForWidth())
        self.titleBtn_option.setSizePolicy(sizePolicy)
        self.titleBtn_option.setObjectName("titleBtn_option")
        self.titleBtns.addWidget(self.titleBtn_option, 0, 1, 1, 1)
        self.titleBtn_run = QtWidgets.QPushButton(self.page_enter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleBtn_run.sizePolicy().hasHeightForWidth())
        self.titleBtn_run.setSizePolicy(sizePolicy)
        self.titleBtn_run.setObjectName("titleBtn_run")
        self.titleBtns.addWidget(self.titleBtn_run, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.titleBtns)
        self.down_version = QtWidgets.QLabel(self.page_enter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.down_version.sizePolicy().hasHeightForWidth())
        self.down_version.setSizePolicy(sizePolicy)
        self.down_version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.down_version.setObjectName("down_version")
        self.verticalLayout_4.addWidget(self.down_version)
        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 1)
        self.pages.addWidget(self.page_enter)
        self.page_setting = QtWidgets.QWidget()
        self.page_setting.setStyleSheet("QLabel{\n"
"    font: 11pt \"맑은 고딕\";\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton{\n"
"    font: 25 11pt \"Malgun Gothic\";\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    frameShape: panel;\n"
"    \n"
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
"    background-color:rgb(85, 170, 255);\n"
"    border: 1px solid black;\n"
"}\n"
"QPushButton#setting_btn_addfile:pressed{\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 1 rgb(85, 170, 255), stop: 0 rgb(46, 93, 140));\n"
"\n"
"}")
        self.page_setting.setObjectName("page_setting")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_setting)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.setting_stage_table = QtWidgets.QTableView(self.page_setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_stage_table.sizePolicy().hasHeightForWidth())
        self.setting_stage_table.setSizePolicy(sizePolicy)
        self.setting_stage_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setting_stage_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.setting_stage_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.setting_stage_table.setObjectName("setting_stage_table")
        self.gridLayout_2.addWidget(self.setting_stage_table, 2, 0, 1, 1)
        self.setitem_file = QtWidgets.QHBoxLayout()
        self.setitem_file.setObjectName("setitem_file")
        self.setting_layout_btn_addfile = QtWidgets.QVBoxLayout()
        self.setting_layout_btn_addfile.setSpacing(0)
        self.setting_layout_btn_addfile.setObjectName("setting_layout_btn_addfile")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.setting_layout_btn_addfile.addItem(spacerItem)
        self.setting_btn_addfile = QtWidgets.QPushButton(self.page_setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_btn_addfile.sizePolicy().hasHeightForWidth())
        self.setting_btn_addfile.setSizePolicy(sizePolicy)
        self.setting_btn_addfile.setObjectName("setting_btn_addfile")
        self.setting_layout_btn_addfile.addWidget(self.setting_btn_addfile)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.setting_layout_btn_addfile.addItem(spacerItem1)
        self.setitem_file.addLayout(self.setting_layout_btn_addfile)
        self.setting_list_file = QtWidgets.QTableView(self.page_setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_list_file.sizePolicy().hasHeightForWidth())
        self.setting_list_file.setSizePolicy(sizePolicy)
        self.setting_list_file.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setting_list_file.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.setting_list_file.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.setting_list_file.setObjectName("setting_list_file")
        self.setitem_file.addWidget(self.setting_list_file)
        self.gridLayout_2.addLayout(self.setitem_file, 1, 0, 1, 1)
        self.setting_btns_real = QtWidgets.QHBoxLayout()
        self.setting_btns_real.setObjectName("setting_btns_real")
        self.setting_btn_real_run = QtWidgets.QPushButton(self.page_setting)
        self.setting_btn_real_run.setObjectName("setting_btn_real_run")
        self.setting_btns_real.addWidget(self.setting_btn_real_run)
        self.setting_btn_real_gomenu = QtWidgets.QPushButton(self.page_setting)
        self.setting_btn_real_gomenu.setObjectName("setting_btn_real_gomenu")
        self.setting_btns_real.addWidget(self.setting_btn_real_gomenu)
        self.gridLayout_2.addLayout(self.setting_btns_real, 3, 0, 1, 1)
        self.setitem_extend = QtWidgets.QHBoxLayout()
        self.setitem_extend.setObjectName("setitem_extend")
        self.setting_label_extend = QtWidgets.QLabel(self.page_setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_label_extend.sizePolicy().hasHeightForWidth())
        self.setting_label_extend.setSizePolicy(sizePolicy)
        self.setting_label_extend.setObjectName("setting_label_extend")
        self.setitem_extend.addWidget(self.setting_label_extend)
        self.extend_setting = QtWidgets.QStackedWidget(self.page_setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extend_setting.sizePolicy().hasHeightForWidth())
        self.extend_setting.setSizePolicy(sizePolicy)
        self.extend_setting.setObjectName("extend_setting")
        self.extend_normal = QtWidgets.QWidget()
        self.extend_normal.setStyleSheet("QRadioButton{\n"
"    font: 25 10pt \"Malgun Gothic\";\n"
"\n"
"}\n"
"\n"
"QAbstractSpinBox{\n"
"    font: 25 10pt \"Malgun Gothic\";\n"
"}")
        self.extend_normal.setObjectName("extend_normal")
        self.gridLayout = QtWidgets.QGridLayout(self.extend_normal)
        self.gridLayout.setObjectName("gridLayout")
        self.extend_normal_recent = QtWidgets.QSpinBox(self.extend_normal)
        self.extend_normal_recent.setEnabled(False)
        self.extend_normal_recent.setMaximum(314159265)
        self.extend_normal_recent.setObjectName("extend_normal_recent")
        self.gridLayout.addWidget(self.extend_normal_recent, 1, 1, 1, 1)
        self.extend_normal_wil = QtWidgets.QSpinBox(self.extend_normal)
        self.extend_normal_wil.setEnabled(False)
        self.extend_normal_wil.setMaximum(314159265)
        self.extend_normal_wil.setObjectName("extend_normal_wil")
        self.gridLayout.addWidget(self.extend_normal_wil, 1, 0, 1, 1)
        self.extend_normal_button_wil = QtWidgets.QRadioButton(self.extend_normal)
        self.extend_normal_button_wil.setChecked(False)
        self.extend_normal_button_wil.setAutoExclusive(False)
        self.extend_normal_button_wil.setObjectName("extend_normal_button_wil")
        self.gridLayout.addWidget(self.extend_normal_button_wil, 0, 0, 1, 1)
        self.extend_normal_button_recent = QtWidgets.QRadioButton(self.extend_normal)
        self.extend_normal_button_recent.setChecked(False)
        self.extend_normal_button_recent.setAutoExclusive(False)
        self.extend_normal_button_recent.setObjectName("extend_normal_button_recent")
        self.gridLayout.addWidget(self.extend_normal_button_recent, 0, 1, 1, 1)
        self.extend_normal_button_recentValue = QtWidgets.QRadioButton(self.extend_normal)
        self.extend_normal_button_recentValue.setChecked(False)
        self.extend_normal_button_recentValue.setAutoExclusive(False)
        self.extend_normal_button_recentValue.setObjectName("extend_normal_button_recentValue")
        self.gridLayout.addWidget(self.extend_normal_button_recentValue, 0, 2, 1, 1)
        self.extend_normal_recentValue = QtWidgets.QDoubleSpinBox(self.extend_normal)
        self.extend_normal_recentValue.setEnabled(False)
        self.extend_normal_recentValue.setReadOnly(True)
        self.extend_normal_recentValue.setDecimals(4)
        self.extend_normal_recentValue.setMaximum(1.0)
        self.extend_normal_recentValue.setSingleStep(0.01)
        self.extend_normal_recentValue.setObjectName("extend_normal_recentValue")
        self.gridLayout.addWidget(self.extend_normal_recentValue, 1, 2, 1, 1)
        self.extend_setting.addWidget(self.extend_normal)
        self.extend_c2 = QtWidgets.QWidget()
        self.extend_c2.setObjectName("extend_c2")
        self.extend_setting.addWidget(self.extend_c2)
        self.setitem_extend.addWidget(self.extend_setting)
        self.gridLayout_2.addLayout(self.setitem_extend, 0, 0, 1, 1)
        self.pages.addWidget(self.page_setting)
        self.page_do = QtWidgets.QWidget()
        self.page_do.setStyleSheet("#input{\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"}\n"
"#log {\n"
"    font: 25 9pt \"Malgun Gothic\";\n"
"background-color: white;\n"
"}\n"
"#queston{\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"}")
        self.page_do.setObjectName("page_do")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_do)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.queston = QtWidgets.QTextBrowser(self.page_do)
        font = QtGui.QFont()
        font.setFamily("13 Malgun Gothic")
        font.setPointSize(12)
        font.setItalic(False)
        self.queston.setFont(font)
        self.queston.setFocusPolicy(QtCore.Qt.NoFocus)
        self.queston.setAcceptRichText(False)
        self.queston.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.queston.setOpenLinks(False)
        self.queston.setObjectName("queston")
        self.verticalLayout_3.addWidget(self.queston)
        self.inputLayout = QtWidgets.QHBoxLayout()
        self.inputLayout.setObjectName("inputLayout")
        self.input = QtWidgets.QListWidget(self.page_do)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy)
        self.input.setAutoScroll(False)
        self.input.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.input.setTabKeyNavigation(True)
        self.input.setDragEnabled(True)
        self.input.setDragDropOverwriteMode(False)
        self.input.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.input.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.input.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.input.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.input.setObjectName("input")
        item = QtWidgets.QListWidgetItem(self.input)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item = QtWidgets.QListWidgetItem(self.input)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item = QtWidgets.QListWidgetItem(self.input)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.inputLayout.addWidget(self.input)
        self.enter = QtWidgets.QPushButton(self.page_do)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enter.sizePolicy().hasHeightForWidth())
        self.enter.setSizePolicy(sizePolicy)
        self.enter.setAutoDefault(True)
        self.enter.setDefault(True)
        self.enter.setObjectName("enter")
        self.inputLayout.addWidget(self.enter)
        self.inputLayout.setStretch(0, 3)
        self.inputLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.inputLayout)
        self.log = QtWidgets.QListWidget(self.page_do)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        self.log.setSizePolicy(sizePolicy)
        self.log.setFocusPolicy(QtCore.Qt.NoFocus)
        self.log.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.log.setObjectName("log")
        QtWidgets.QListWidgetItem(self.log)
        QtWidgets.QListWidgetItem(self.log)
        QtWidgets.QListWidgetItem(self.log)
        QtWidgets.QListWidgetItem(self.log)
        QtWidgets.QListWidgetItem(self.log)
        self.verticalLayout_3.addWidget(self.log)
        self.verticalLayout_3.setStretch(0, 23)
        self.verticalLayout_3.setStretch(1, 3)
        self.verticalLayout_3.setStretch(2, 3)
        self.pages.addWidget(self.page_do)
        self.page_resultant = QtWidgets.QWidget()
        self.page_resultant.setStyleSheet("QLabel#label_resultant{\n"
"    font: 100 bold 25pt \"Malgun Gothic\";\n"
"}")
        self.page_resultant.setObjectName("page_resultant")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_resultant)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_resultant = QtWidgets.QLabel(self.page_resultant)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_resultant.sizePolicy().hasHeightForWidth())
        self.label_resultant.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(25)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.label_resultant.setFont(font)
        self.label_resultant.setObjectName("label_resultant")
        self.verticalLayout_5.addWidget(self.label_resultant)
        self.resultant_view = QtWidgets.QTableView(self.page_resultant)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultant_view.sizePolicy().hasHeightForWidth())
        self.resultant_view.setSizePolicy(sizePolicy)
        self.resultant_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.resultant_view.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.resultant_view.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.resultant_view.setObjectName("resultant_view")
        self.verticalLayout_5.addWidget(self.resultant_view)
        self.resultant_btns = QtWidgets.QGridLayout()
        self.resultant_btns.setObjectName("resultant_btns")
        self.resultant_btn_menu = QtWidgets.QPushButton(self.page_resultant)
        self.resultant_btn_menu.setObjectName("resultant_btn_menu")
        self.resultant_btns.addWidget(self.resultant_btn_menu, 0, 2, 1, 1)
        self.resultant_btn_again = QtWidgets.QPushButton(self.page_resultant)
        self.resultant_btn_again.setObjectName("resultant_btn_again")
        self.resultant_btns.addWidget(self.resultant_btn_again, 0, 0, 1, 1)
        self.resultant_btn_setting = QtWidgets.QPushButton(self.page_resultant)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.resultant_btn_setting.setFont(font)
        self.resultant_btn_setting.setObjectName("resultant_btn_setting")
        self.resultant_btns.addWidget(self.resultant_btn_setting, 0, 1, 1, 1)
        self.resultant_btn_save = QtWidgets.QPushButton(self.page_resultant)
        self.resultant_btn_save.setObjectName("resultant_btn_save")
        self.resultant_btns.addWidget(self.resultant_btn_save, 1, 0, 1, 1)
        self.resultant_btn_preference = QtWidgets.QPushButton(self.page_resultant)
        self.resultant_btn_preference.setObjectName("resultant_btn_preference")
        self.resultant_btns.addWidget(self.resultant_btn_preference, 1, 1, 1, 1)
        self.resultant_btn_openthis = QtWidgets.QPushButton(self.page_resultant)
        self.resultant_btn_openthis.setObjectName("resultant_btn_openthis")
        self.resultant_btns.addWidget(self.resultant_btn_openthis, 1, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.resultant_btns)
        self.pages.addWidget(self.page_resultant)
        self.page_option = QtWidgets.QWidget()
        self.page_option.setStyleSheet("QScrollArea{\n"
"    background-color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
".QLabel{\n"
"    font: 25 10pt \"Malgun Gothic\";\n"
"}\n"
"\n"
".QFontComboBox{\n"
"    font: 25 9pt \"Malgun Gothic\";\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
".QSpinBox{\n"
"    font: 25 9pt \"Malgun Gothic\";\n"
"}")
        self.page_option.setObjectName("page_option")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_option)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.option_scrollarea = QtWidgets.QScrollArea(self.page_option)
        self.option_scrollarea.setStyleSheet("#option_scrollarea_contents{\n"
"    background-color:white;\n"
"}\n"
"\n"
".QWidget{\n"
"    border: 1px solid black;\n"
"}")
        self.option_scrollarea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.option_scrollarea.setWidgetResizable(True)
        self.option_scrollarea.setObjectName("option_scrollarea")
        self.option_scrollarea_contents = QtWidgets.QWidget()
        self.option_scrollarea_contents.setGeometry(QtCore.QRect(0, 0, 376, 562))
        self.option_scrollarea_contents.setStyleSheet("")
        self.option_scrollarea_contents.setObjectName("option_scrollarea_contents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.option_scrollarea_contents)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.option_font_queston = Widget_Option_Font(self.option_scrollarea_contents)
        self.option_font_queston.setObjectName("option_font_queston")
        self._3 = QtWidgets.QGridLayout(self.option_font_queston)
        self._3.setObjectName("_3")
        self.verticalLayout_7.addWidget(self.option_font_queston)
        self.option_font_input = Widget_Option_Font(self.option_scrollarea_contents)
        self.option_font_input.setObjectName("option_font_input")
        self._4 = QtWidgets.QGridLayout(self.option_font_input)
        self._4.setObjectName("_4")
        self.verticalLayout_7.addWidget(self.option_font_input)
        self.option_font_lcptd_file = Widget_Option_Font(self.option_scrollarea_contents)
        self.option_font_lcptd_file.setObjectName("option_font_lcptd_file")
        self._2 = QtWidgets.QGridLayout(self.option_font_lcptd_file)
        self._2.setObjectName("_2")
        self.verticalLayout_7.addWidget(self.option_font_lcptd_file)
        self.option_color_lcptd_progress = Widget_Option_Color(self.option_scrollarea_contents)
        self.option_color_lcptd_progress.setObjectName("option_color_lcptd_progress")
        self._5 = QtWidgets.QGridLayout(self.option_color_lcptd_progress)
        self._5.setObjectName("_5")
        self.verticalLayout_7.addWidget(self.option_color_lcptd_progress)
        self.option_color_lcptd_rategress = Widget_Option_Color(self.option_scrollarea_contents)
        self.option_color_lcptd_rategress.setObjectName("option_color_lcptd_rategress")
        self._6 = QtWidgets.QGridLayout(self.option_color_lcptd_rategress)
        self._6.setObjectName("_6")
        self.verticalLayout_7.addWidget(self.option_color_lcptd_rategress)
        self.option_color_lcptd_cwgress_c = Widget_Option_Color(self.option_scrollarea_contents)
        self.option_color_lcptd_cwgress_c.setObjectName("option_color_lcptd_cwgress_c")
        self._7 = QtWidgets.QGridLayout(self.option_color_lcptd_cwgress_c)
        self._7.setObjectName("_7")
        self.verticalLayout_7.addWidget(self.option_color_lcptd_cwgress_c)
        self.option_color_lcptd_cwgress_w = Widget_Option_Color(self.option_scrollarea_contents)
        self.option_color_lcptd_cwgress_w.setObjectName("option_color_lcptd_cwgress_w")
        self._8 = QtWidgets.QGridLayout(self.option_color_lcptd_cwgress_w)
        self._8.setObjectName("_8")
        self.verticalLayout_7.addWidget(self.option_color_lcptd_cwgress_w)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.option_HL = QtWidgets.QHBoxLayout()
        self.option_HL.setObjectName("option_HL")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.option_HL.addItem(spacerItem3)
        self.option_btn_back = QtWidgets.QPushButton(self.option_scrollarea_contents)
        self.option_btn_back.setObjectName("option_btn_back")
        self.option_HL.addWidget(self.option_btn_back)
        self.option_btn_save = QtWidgets.QPushButton(self.option_scrollarea_contents)
        self.option_btn_save.setObjectName("option_btn_save")
        self.option_HL.addWidget(self.option_btn_save)
        self.option_HL.setStretch(0, 5)
        self.option_HL.setStretch(1, 2)
        self.option_HL.setStretch(2, 2)
        self.verticalLayout_7.addLayout(self.option_HL)
        self.option_scrollarea.setWidget(self.option_scrollarea_contents)
        self.verticalLayout_6.addWidget(self.option_scrollarea)
        self.pages.addWidget(self.page_option)
        self.horizontalLayout.addWidget(self.pages)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.sideStatus = QtWidgets.QDockWidget(MainWindow)
        self.sideStatus.setStyleSheet("#sideStatus::title{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid black;\n"
"    \n"
"}\n"
"\n"
"#sideStatus{\n"
"    font: 11pt \"맑은 고딕\";\n"
"}")
        self.sideStatus.setFloating(False)
        self.sideStatus.setObjectName("sideStatus")
        self.lcptd = QtWidgets.QWidget()
        self.lcptd.setStyleSheet("#lcptd {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border: 1px solid black;\n"
"    border-top: none;\n"
"}\n"
"\n"
".QLineEdit#lcptd_file {\n"
"    background-color:rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"}\n"
"\n"
"#correct_layout {\n"
"    background-color: rgba(255, 255, 255, 0)\n"
"}\n"
"\n"
"\n"
"#lcptd_progress{\n"
"    \n"
"    font: 25 15pt \"Malgun Gothic\";\n"
"    border: 1.2px solid black;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"}\n"
"#lcptd_progress::chunk{background-color: rgb(0, 170, 255)}\n"
"#lcptd_rategress{\n"
"    \n"
"    font: 25 15pt \"Malgun Gothic\";\n"
"    border: 1.2px solid black;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"}\n"
"#lcptd_rategress::chunk{background-color: rgb(120, 230, 20)}\n"
"\n"
"#lcptd_cwgress{\n"
"    \n"
"    font: 25 15pt \"Malgun Gothic\";\n"
"    border: 1.2px solid black;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    background-color: rgb(255, 0, 0)\n"
"}\n"
"#lcptd_cwgress::chunk{background-color: rgb(255, 200, 20);}")
        self.lcptd.setObjectName("lcptd")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.lcptd)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcptd_file = QtWidgets.QLineEdit(self.lcptd)
        self.lcptd_file.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lcptd_file.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lcptd_file.setReadOnly(True)
        self.lcptd_file.setObjectName("lcptd_file")
        self.verticalLayout_2.addWidget(self.lcptd_file)
        self.lcptd_progress = QtWidgets.QProgressBar(self.lcptd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcptd_progress.sizePolicy().hasHeightForWidth())
        self.lcptd_progress.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lcptd_progress.setPalette(palette)
        self.lcptd_progress.setStyleSheet("")
        self.lcptd_progress.setMaximum(100)
        self.lcptd_progress.setProperty("value", 10)
        self.lcptd_progress.setTextVisible(True)
        self.lcptd_progress.setObjectName("lcptd_progress")
        self.verticalLayout_2.addWidget(self.lcptd_progress)
        self.lcptd_rategress = QtWidgets.QProgressBar(self.lcptd)
        self.lcptd_rategress.setStyleSheet("")
        self.lcptd_rategress.setProperty("value", 25)
        self.lcptd_rategress.setObjectName("lcptd_rategress")
        self.verticalLayout_2.addWidget(self.lcptd_rategress)
        self.lcptd_cwgress = QtWidgets.QProgressBar(self.lcptd)
        self.lcptd_cwgress.setMaximum(2)
        self.lcptd_cwgress.setProperty("value", 1)
        self.lcptd_cwgress.setObjectName("lcptd_cwgress")
        self.verticalLayout_2.addWidget(self.lcptd_cwgress)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.sideStatus.setWidget(self.lcptd)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.sideStatus)
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionreturn_to_manimenu = QtWidgets.QAction(MainWindow)
        self.actionreturn_to_manimenu.setObjectName("actionreturn_to_manimenu")
        self.actiongotooption = QtWidgets.QAction(MainWindow)
        self.actiongotooption.setObjectName("actiongotooption")
        self.menu.addAction(self.actionexit)
        self.menu.addAction(self.actionreturn_to_manimenu)
        self.menu.addAction(self.actiongotooption)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.pages.setCurrentIndex(0)
        self.extend_setting.setCurrentIndex(0)
        QtCore.QObject.connect(self.extend_normal_button_wil, QtCore.SIGNAL("clicked(bool)"), self.extend_normal_wil.setEnabled)
        QtCore.QObject.connect(self.extend_normal_button_recent, QtCore.SIGNAL("clicked(bool)"), self.extend_normal_recent.setEnabled)
        QtCore.QObject.connect(self.extend_normal_button_recentValue, QtCore.SIGNAL("clicked(bool)"), self.extend_normal_recentValue.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "antanswer-python-pyside2", None, -1))
        self.title.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Antanswer</span><span style=\" font-weight:600; vertical-align:sub;\">(pyside2)</span></p></body></html>", None, -1))
        self.titleBtn_exit.setText(QtWidgets.QApplication.translate("MainWindow", "나가기", None, -1))
        self.titleBtn_option.setText(QtWidgets.QApplication.translate("MainWindow", "설정", None, -1))
        self.titleBtn_run.setText(QtWidgets.QApplication.translate("MainWindow", "실행", None, -1))
        self.down_version.setText(QtWidgets.QApplication.translate("MainWindow", "version: loading", None, -1))
        self.setting_btn_addfile.setText(QtWidgets.QApplication.translate("MainWindow", " 파일 추가 ", None, -1))
        self.setting_btn_real_run.setText(QtWidgets.QApplication.translate("MainWindow", "시작", None, -1))
        self.setting_btn_real_gomenu.setText(QtWidgets.QApplication.translate("MainWindow", "돌아가기", None, -1))
        self.setting_label_extend.setText(QtWidgets.QApplication.translate("MainWindow", " 확장 설정 ", None, -1))
        self.extend_normal_button_wil.setText(QtWidgets.QApplication.translate("MainWindow", "wil", None, -1))
        self.extend_normal_button_recent.setText(QtWidgets.QApplication.translate("MainWindow", "recent", None, -1))
        self.extend_normal_button_recentValue.setText(QtWidgets.QApplication.translate("MainWindow", "recentValue", None, -1))
        __sortingEnabled = self.input.isSortingEnabled()
        self.input.setSortingEnabled(False)
        self.input.setSortingEnabled(__sortingEnabled)
        self.enter.setText(QtWidgets.QApplication.translate("MainWindow", "입력", None, -1))
        __sortingEnabled = self.log.isSortingEnabled()
        self.log.setSortingEnabled(False)
        self.log.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "Test Log is the log.", None, -1))
        self.log.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "TestLog1", None, -1))
        self.log.item(2).setText(QtWidgets.QApplication.translate("MainWindow", "It is made by tree that was made in Korea. But Actually, It is harvested in Chinese.", None, -1))
        self.log.item(3).setText(QtWidgets.QApplication.translate("MainWindow", "Kanobe Empesus decide the warl.", None, -1))
        self.log.item(4).setText(QtWidgets.QApplication.translate("MainWindow", "Laufghart", None, -1))
        self.log.setSortingEnabled(__sortingEnabled)
        self.label_resultant.setText(QtWidgets.QApplication.translate("MainWindow", "결과:", None, -1))
        self.resultant_btn_menu.setText(QtWidgets.QApplication.translate("MainWindow", "메뉴로 돌아가기", None, -1))
        self.resultant_btn_again.setText(QtWidgets.QApplication.translate("MainWindow", "다시 시도", None, -1))
        self.resultant_btn_setting.setText(QtWidgets.QApplication.translate("MainWindow", "실행 설정으로", None, -1))
        self.resultant_btn_save.setText(QtWidgets.QApplication.translate("MainWindow", "이 결과 저장", None, -1))
        self.resultant_btn_preference.setText(QtWidgets.QApplication.translate("MainWindow", "선호 파일 열기", None, -1))
        self.resultant_btn_openthis.setText(QtWidgets.QApplication.translate("MainWindow", "이 anw 파일 열기", None, -1))
        self.option_btn_back.setText(QtWidgets.QApplication.translate("MainWindow", "돌아가기", None, -1))
        self.option_btn_save.setText(QtWidgets.QApplication.translate("MainWindow", "저장하기", None, -1))
        self.menu.setTitle(QtWidgets.QApplication.translate("MainWindow", "기능", None, -1))
        self.sideStatus.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "상태창(lcptd)", None, -1))
        self.lcptd_file.setText(QtWidgets.QApplication.translate("MainWindow", "test.dnwouvndowdnbovwdbovwdbowdvnovwdn.zip", None, -1))
        self.lcptd_progress.setFormat(QtWidgets.QApplication.translate("MainWindow", "%p%:%v", None, -1))
        self.lcptd_cwgress.setFormat(QtWidgets.QApplication.translate("MainWindow", "%v:", None, -1))
        self.actionexit.setText(QtWidgets.QApplication.translate("MainWindow", "나가기", None, -1))
        self.actionreturn_to_manimenu.setText(QtWidgets.QApplication.translate("MainWindow", "메인메뉴로 돌아가기", None, -1))
        self.actiongotooption.setText(QtWidgets.QApplication.translate("MainWindow", "옵션", None, -1))

from components.gui.option_ui import Widget_Option_Font, Widget_Option_Color
