import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QGridLayout,
                               QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, QMainWindow, QFileDialog, QCheckBox,
                               QAbstractItemView, QErrorMessage)
from PySide2.QtCore import Qt, Signal, QModelIndex, QAbstractItemModel, QAbstractListModel, QSignalMapper, QObject, SIGNAL, SLOT

from PySide2.QtGui import QStandardItem, QStandardItemModel

from functools import partial

import hashlib

from components.gui.main_ui import Ui_MainWindow
from anwFunctions.anwReaders.reader import READ_ANW

class Main(QMainWindow):
    ok = Signal()
    def __init__(self, opt, debug=0,parent=None):
        QMainWindow.__init__(self, parent)

        ### opt
        #self.anw_standard = opt["anw_standard"]
        self.cond_default = {
            "COMP_IGNORE_SPACE": True,  # ignoring space, blank like '\t' won't be replaced
            "COMP_IGNORE_CASE": True,  # ignoring case, replace upper to lower
            "ANSWER_WITHOUT_ORDER": True,  # when answering quest, order don't interrupt you
            "COMP_NOT": True,  # ignoring sequence matcher(compare) method # in now deprecated sorry
            "RESULT_DISPLAY_QUEST": True,  # displaying Quest
            "COMP_IGNORE_LAST_PERIOD": True,  # ignoring the last period
            # support CLI, but main is GUI.
            "RESULT_MANUAL_POST_CORRECTION": True  # post correction at result time GUI main cond
        }  # default preferences
        #self.bVariables = opt["bVariables"]



        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pages.setCurrentIndex(debug)
        ### menubar: action
        self.ui.actionexit.triggered.connect(self.go_exit)
        self.ui.actionreturn_to_manimenu.triggered.connect(self.go_enter)

        ### enter
        self.ui.titleBtn_run.clicked.connect(self.go_setting)
        self.ui.titleBtn_option.clicked.connect(self.go_option)
        self.ui.titleBtn_exit.clicked.connect(self.go_exit)

        ### setting

        ### setting:list_file & btn_addfile
        self.ui.setting_btn_addfile.clicked.connect(self.add_filetemp)

        self.temp_setting_list_file_btns_delete = list()
        self.temp_setting_list_file_checkboxes_select = list()

        self.temp_selected_files = list()


        self.model_file = QStandardItemModel(None)
        self.model_file.setColumnCount(4)
        self.model_file.setHorizontalHeaderLabels(("name", "dir", "use", "delete"))
        self.ui.setting_list_file.setEditTriggers(QAbstractItemView.NoEditTriggers)

        ### setting:stage_table
        self.temp_selected_stage = dict()


        self.model_stage = QStandardItemModel(None)
        self.model_stage.setColumnCount(3)
        self.model_stage.setHorizontalHeaderLabels(("name", "stage", "check"))
        self.ui.setting_stage_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        ### setting:btn_real_run & btn_real_gomenu
        self.ui.setting_btn_real_run.clicked.connect(self.go_run)
        self.ui.setting_btn_real_gomenu.clicked.connect(self.go_enter)



        ### do
        self.queston_template = """<!DOCTYPE html><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style=" font-family:'13 Malgun Gothic'; font-size:12pt; font-weight:400; font-style:normal;"><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Malgun Gothic'; font-size:14pt; font-weight:600;">%s</span></p></body></html>"""

        self.ui.input.setText("")
        self.ui.queston.setText(self.queston_template%"")

        self.ui.log.clear()


        ### resultant
        #self.ui.resultant_btn_again.clicked.connect()
        self.ui.resultant_btn_setting.clicked.connect(self.go_setting)
        self.ui.resultant_btn_menu.clicked.connect(self.go_enter)






    def go_setting(self):
        self.ui.pages.setCurrentIndex(1)

    def go_option(self):
        self.ui.pages.setCurrentIndex(4)

    def go_exit(self):
        cMessage = QMessageBox(self)
        c = cMessage.question(self, 'really_exit?', 'do you really exit?', QMessageBox.Yes | QMessageBox.No)
        if c == QMessageBox.No:
            pass
        else:
            self.close()

    def go_enter(self):
        # pause all
        self.ui.pages.setCurrentIndex(0)

    def go_run(self):
        self.ui.pages.setCurrentIndex(2)



    def add_filetemp(self):
        fnames = QFileDialog.getOpenFileNames(self, "open anw runfiles", "", "All Files(*)", "/anwdatapack")

        for i in fnames[0]:
            try:
                f = open(i, "r", encoding="utf-8")
            except FileNotFoundError as e:
                tepp = QErrorMessage()
                tepp.showMessage("File Not Found")
                tepp.exec_()
                continue
            except Exception as e:
                tepp = QErrorMessage()
                tepp.showMessage("Wrongthing some while select file")
                tepp.exec_()
                continue
            try:
                wbr = READ_ANW(f)

            except Exception as e:
                tepp = QErrorMessage()
                tepp.showMessage("wrong anw file:", str(e))
                tepp.exec_()
                f.close()
                continue
            finally:
                f.close()

            for i in self.temp_selected_files:
                if i[1] == wbr["name"]:
                    tepp = QErrorMessage()
                    tepp.showMessage("duplicate named file:", wbr["name"])
                    tepp.exec_()
                    break
            else:
                self.temp_selected_files.append([i, wbr["name"], False, wbr])

        self.list_file_update()


    def list_file_update(self):
        self.model_file = QStandardItemModel(None)
        self.model_file.setColumnCount(3)
        self.model_file.setHorizontalHeaderLabels(("name", "use", "delete"))

        self.temp_setting_list_file_btns_delete = []
        self.temp_setting_list_file_checkboxes_select = []

        for i, sf in enumerate(self.temp_selected_files):
            temp_item_name = QStandardItem()
            temp_item_name.setData(sf[1], Qt.DisplayRole)
            self.model_file.appendRow(temp_item_name)
            self.ui.setting_list_file.setModel(self.model_file)

            self.temp_setting_list_file_btns_delete.append(QPushButton(str(i), self.ui.setting_list_file))
            self.temp_setting_list_file_btns_delete[i].setObjectName(
                "temp_setting_list_file_btn_delete_{}".format(str(i))
            )
            self.temp_setting_list_file_btns_delete[i].clicked.connect(lambda ch=False, row=i: self.list_file_delete_element(row))

            self.temp_setting_list_file_checkboxes_select.append(QCheckBox("select" + str(i) , self.ui.setting_list_file))
            self.temp_setting_list_file_checkboxes_select[i].setObjectName(
                "temp_setting_list_file_checkbox_select_{}".format(str(i))
            )
            self.temp_setting_list_file_checkboxes_select[i].setChecked(sf[2])
            self.temp_setting_list_file_checkboxes_select[i].clicked[bool].connect(partial(self.list_file_update_select, row=i))
            self.ui.setting_list_file.setIndexWidget(self.model_file.index(i, 2), self.temp_setting_list_file_btns_delete[i])
            self.ui.setting_list_file.setIndexWidget(self.model_file.index(i, 1), self.temp_setting_list_file_checkboxes_select[i])

        self.ui.setting_list_file.setModel(self.model_file)

    def list_file_delete_element(self, row):
        t_name = self.temp_selected_files[row][1]
        del self.temp_selected_files[row]

        if t_name in self.temp_selected_stage:
            del self.temp_selected_stage[t_name]

        self.stage_table_update()
        self.list_file_update()


    def list_file_update_select(self, enable, row=0):
        """
        update list_file when checking checkbox
        :param enable: is checkbox enable?
        :param row: row index
        :return: void
        """
        if enable:

            self.temp_selected_stage[self.temp_selected_files[row][1]] = {}


            for st in self.temp_selected_files[row][3]["stages"]:
                self.temp_selected_stage[self.temp_selected_files[row][1]][st] = True

            self.stage_table_update()


            self.temp_selected_files[row][2] = enable
        else:
            del self.temp_selected_stage[self.temp_selected_files[row][1]]
            self.stage_table_update()

            self.temp_selected_files[row][2] = enable

    def stage_table_update(self):
        self.model_stage = QStandardItemModel(None)
        self.model_stage.setColumnCount(3)
        self.model_stage.setHorizontalHeaderLabels(("name", "stage", "check"))
        c = 0
        print(self.temp_selected_stage)
        for n, stdict in self.temp_selected_stage.items():
            for st, v in stdict.items():
                temp_item_name = QStandardItem()
                temp_item_name.setData(n, Qt.DisplayRole)
                temp_item_stage = QStandardItem()
                temp_item_stage.setData(st, Qt.DisplayRole)
                self.model_stage.appendRow((temp_item_name, temp_item_stage))
                self.ui.setting_stage_table.setModel(self.model_stage)

                temp_setting_stage_table_checkbox_select = QCheckBox("select", self.ui.setting_stage_table)
                temp_setting_stage_table_checkbox_select.setChecked(v)
                temp_setting_stage_table_checkbox_select.clicked[bool].connect(partial(self.stage_table_update_select, name=n, stage=st))
                self.ui.setting_stage_table.setIndexWidget(self.model_stage.index(c, 2), temp_setting_stage_table_checkbox_select)

                c+= 1
        self.ui.setting_stage_table.setModel(self.model_stage)


    def stage_table_update_select(self, enable, name, stage):
        if enable:
            self.temp_selected_stage[name][stage] = enable
        else:
            self.temp_selected_stage[name][stage] = enable





if __name__ == '__main__':
    app = QApplication(sys.argv)
    debug = 0
    main = Main({}, debug=debug)

    main.show()
    app.exec_()