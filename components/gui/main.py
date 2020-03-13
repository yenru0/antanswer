import sys
from PySide2.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QGridLayout,
                               QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, QMainWindow, QFileDialog, QCheckBox,
                               QAbstractItemView, QErrorMessage, QListWidgetItem, QListWidget, QTableView)
from PySide2.QtCore import Qt, Signal, QModelIndex, QAbstractItemModel, QAbstractListModel, QSignalMapper, QObject, SIGNAL, SLOT

from PySide2.QtGui import QStandardItem, QStandardItemModel, QKeyEvent

from functools import partial

from random import randrange, randint, choice

import hashlib

from components.gui.main_ui import Ui_MainWindow
from anwFunctions.anwReaders.reader import READ_ANW


class Main(QMainWindow):
    ok = Signal()

    def __init__(self, opt, debug=0, parent=None):
        QMainWindow.__init__(self, parent)

        ### opt
        self.anw_standard = opt["anw_standard"]
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
        self.bVariables = opt["bVariables"]

        self.aqs = None
        self.cond_used = {}

        self.result = []
        self.samples = None
        self.count = 0
        self.score = 0
        self.detail = [None, None]

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

        self.input_reset()
        self.queston_reset()
        self.log_reset()

        self.ui.enter.clicked.connect(partial(self.next_routine, isFirst=False))

        ### dock
        self.lcptd_reset()

        ### resultant
        self.model_resultant = QStandardItemModel()


        # self.ui.resultant_btn_again.clicked.connect()
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
        if not self.temp_selected_stage:
            tepp = QErrorMessage()
            tepp.showMessage("File wasn't selected")
            tepp.exec_()
            return

        if not any(vv for v in self.temp_selected_stage.values() for vv in v.values()):
            tepp = QErrorMessage()
            tepp.showMessage("Stage wasn't selected")
            tepp.exec_()
            return

        self.init_routine()

        self.ui.pages.setCurrentIndex(2)

    def go_resultant(self):
        self.resultant_set()
        self.ui.pages.setCurrentIndex(3)

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

            self.temp_setting_list_file_checkboxes_select.append(QCheckBox("select" + str(i), self.ui.setting_list_file))
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
            for i in range(len(self.temp_selected_files)):
                self.temp_selected_files[i][2] = False
                if self.temp_selected_files[i][1] in self.temp_selected_stage:
                    del self.temp_selected_stage[self.temp_selected_files[i][1]]

            self.temp_selected_stage[self.temp_selected_files[row][1]] = {}

            for st in self.temp_selected_files[row][3]["stages"]:
                self.temp_selected_stage[self.temp_selected_files[row][1]][st] = True

            self.stage_table_update()

            self.temp_selected_files[row][2] = enable
        else:
            del self.temp_selected_stage[self.temp_selected_files[row][1]]
            self.stage_table_update()

            self.temp_selected_files[row][2] = enable
        self.list_file_update()

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

                c += 1
        self.ui.setting_stage_table.setModel(self.model_stage)

    def stage_table_update_select(self, enable, name, stage):
        if enable:
            self.temp_selected_stage[name][stage] = enable
        else:
            self.temp_selected_stage[name][stage] = enable

    ### routine: do
    def make_aqs(self):
        self.aqs = []

        for n, stdict in self.temp_selected_stage.items():

            for st, v in stdict.items():
                if v:
                    for aq in self.tanw["stages"][st]:
                        self.aqs.append((aq, st, n))

    def init_routine(self):
        # temp
        for n, stdict in self.temp_selected_stage.items():
            for dv in self.temp_selected_files:
                if dv[1] == n:
                    self.tanw = dv[3]
                    break

        self.make_aqs()
        self.cond_used = {}

        for ck, v in self.tanw["cond"].items():
            if v is None:
                self.cond_used[ck] = self.cond_default[ck]
            else:
                self.cond_used[ck] = v

        self.samples = self.sampling()
        self.result = []
        self.score = 0
        self.count = 0

        self.lcptd_reset()
        self.lcptd_set_file(self.temp_selected_stage.keys())

        self.next_routine(False, True)

    def sampling(self):
        """
        get correct wil & recent with checking recent & recentValue
        then, sample answer-question with recent & recentValue
        :return:
        """
        history = []
        # get correct wil & recent
        for k, v in self.tanw["detail_infile"].items():  # priority: recentValue > recent
            if v is None:
                if k == "recentValue":
                    self.detail[1] = int(self.bVariables["bRecentValue"] * len(self.aqs))
                elif k == "wil":
                    self.detail[0] = self.bVariables["bWil"]
                elif k == "recent":
                    if self.detail[1] is not None:
                        pass
                    else:  # recent Check
                        if self.bVariables["bRecent"] > len(self.aqs):
                            self.detail[1] = len(self.aqs)
                        else:
                            self.detail[1] = self.bVariables["bRecent"]
                else:
                    raise Exception("?sampling0r")
            else:
                if k == "recentValue":
                    self.detail[1] = int(v * len(self.aqs))
                elif k == "wil":
                    self.detail[0] = v
                elif k == "recent":
                    if self.detail[1] is not None:
                        pass
                    else:
                        if v > len(self.aqs):
                            self.detail[1] = len(self.aqs)
                        else:
                            self.detail[1] = v
                else:
                    raise Exception("?sampling1r")

        for i in range(self.detail[0]):
            r = randrange(0, len(self.aqs))
            while r in history[-self.detail[1]:]:
                r = randrange(0, len(self.aqs))
            history.append(r)
            yield r

    def next_routine(self, enable=False, isFirst=False):
        if not isFirst:
            emode = self.aqs[self.aqi][0][0]
            answers = self.aqs[self.aqi][0][1]
            questions = tuple(choice(i) for i in self.aqs[self.aqi][0][2])
            scope_stage, scope_name = self.aqs[self.aqi][1], self.aqs[self.aqi][2]
            inputs = [self.ui.input.item(i).text() for i in range(self.ui.input.count())]
            mrs = self.reward_quest(answers, inputs)
            self.result.append([(i, mrs[i], inputs[i]) for i in range(len(inputs))])
            self.result[-1].insert(0, questions)
            self.result[-1].insert(1, answers)
            self.count += 1

        # init
        try:
            self.aqi = next(self.samples)
        except StopIteration as e:
            self.go_resultant()

        self.lcptd_set_property()

        emode = self.aqs[self.aqi][0][0]
        answers = self.aqs[self.aqi][0][1]
        questions = tuple(choice(i) for i in self.aqs[self.aqi][0][2])
        scope_stage, scope_name = self.aqs[self.aqi][1], self.aqs[self.aqi][2]
        t_s = ""
        for i, s in enumerate(questions):
            t_s += "(" + str(i) + ")" + s + "\n"
        self.queston_update(t_s)
        self.input_reset(len(answers))

    def queston_update(self, q: str):
        self.ui.queston.setText(self.queston_template % q)

    def queston_reset(self):
        self.ui.queston.setText(self.queston_template % "")

    def input_reset(self, l=0):
        self.ui.input.clear()

        for i in range(l):
            temp_item = QListWidgetItem("")
            temp_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsDragEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            self.ui.input.addItem(temp_item)

    def log_reset(self):
        self.ui.log.clear()

    def log_update(self, log):
        pass

    def reward_quest(self, ans, inputs):
        """
        check answer is correct
        :param ans: answers list
        :param inputs: input i answered
        :return mrs: 0..1 value list about each
        """
        ans = list(ans)
        # TODO: more simply
        if self.cond_used["COMP_IGNORE_SPACE"] is True:

            for i in range(len(ans)):
                ans[i] = [ans[i][j].replace(" ", "") for j in range(len(ans[i]))]

            for i in range(len(inputs)):
                inputs[i] = inputs[i].replace(" ", "")
        if self.cond_used["COMP_IGNORE_CASE"] is True:
            for i in range(len(ans)):
                ans[i] = [ans[i][j].lower() for j in range(len(ans[i]))]
            for i in range(len(inputs)):
                inputs[i] = inputs[i].lower()

        if self.cond_used["COMP_IGNORE_LAST_PERIOD"] is True:

            for i in range(len(ans)):
                ans[i] = [ans[i][j][:-1] if ans[i][j][-1] == "." else ans[i][j] for j in range(len(ans[i]))]
            for i in range(len(inputs)):
                if inputs[i]:
                    inputs[i] = inputs[i][:-1] if inputs[i][-1] == "." else inputs[i]

        if self.cond_used["COMP_NOT"] is False:
            if self.cond_used["ANSWER_WITHOUT_ORDER"] is True:
                mrs = [max(round(self.compare(s, i), 2) for a in ans
                           for s in a) for i in inputs]
            else:
                mrs = [max(round(self.compare(a, i), 2) for a in als) for i, als in zip(inputs, ans)]
        else:
            if self.cond_used["ANSWER_WITHOUT_ORDER"] is True:
                mrs = []
                t = [list(a) for a in ans]
                for i in inputs:
                    for k in range(len(t)):
                        try:
                            if i in t[k]:
                                del t[k]
                                mrs.append(1)
                                break

                        except ValueError:
                            pass
                    else:
                        mrs.append(0)

            else:
                mrs = tuple(any(i == a for a in als) for i, als in zip(inputs, ans))

        if self.cond_used["COMP_NOT"] is False:
            if min(mrs) > 0.92:
                self.score += 1
            else:
                pass
        else:
            if all(mrs):
                self.score += 1
            else:
                pass
        return mrs

    def lcptd_set_file(self, names):
        self.ui.lcptd_file.setText(";".join(names))

    def lcptd_set_property(self):
        self.ui.lcptd_progress.setValue(self.count)
        self.ui.lcptd_progress.setMaximum(self.detail[0])

        # self.score = exact
        if len(str(self.count)) + 1 != self.ui.di_lcd_count.digitCount():
            self.ui.di_lcd_count.setDigitCount(len(str(self.count)) + 1)
        self.ui.di_lcd_count.display(self.count)

        if len(str(self.score)) + 1 != self.ui.di_lcd_count.digitCount():
            self.ui.di_lcd_count.setDigitCount(len(str(self.score)) + 1)
        self.ui.di_lcd_exact.display(self.score)

        if len(str(self.count - self.score)) + 1 != self.ui.di_lcd_count.digitCount():
            self.ui.di_lcd_wrong.setDigitCount(len(str(self.count - self.score)) + 1)
        self.ui.di_lcd_wrong.display(self.count - self.score)

        if self.count == 0:
            self.ui.di_lcd_rate.display(0)
        else:
            self.ui.di_lcd_rate.display(self.score / self.count * 100)

    def lcptd_reset(self):
        self.ui.lcptd_progress.setValue(0)
        self.ui.lcptd_file.setText("")
        self.ui.di_lcd_count.setDigitCount(2)
        self.ui.di_lcd_exact.setDigitCount(2)
        self.ui.di_lcd_wrong.setDigitCount(2)
        self.ui.di_lcd_count.display(0)
        self.ui.di_lcd_exact.display(0)
        self.ui.di_lcd_wrong.display(0)
        self.ui.di_lcd_rate.display(0)


    def resultant_set(self):

        if self.cond_used["RESULT_MANUAL_POST_CORRECTION"]:
            self.model_resultant.setColumnCount(4)
        else:
            self.model_resultant.setColumnCount(3)
        self.model_resultant.setRowCount(self.detail[0])
        self.ui.resultant_view.setModel(self.model_resultant)
        for i in range(self.detail[0]):
            temp_list1 = QListWidget()
            temp_list2 = QListWidget()
            temp_list3 = QListWidget()
            temp_list1.setMinimumHeight(100)
            temp_list1.setMinimumWidth(400)
            temp_list2.setMinimumHeight(100)
            temp_list2.setMinimumWidth(400)
            temp_list3.setMinimumHeight(100)
            temp_list3.setMinimumWidth(400)
            for rsts in self.result[i][2:]:
                temp_list1.addItem(str(rsts[1]) + "|" + rsts[2])


            for qsts in self.result[i][0]:
                temp_list3.addItem(qsts)

            for asts in self.result[i][1]:
                temp_list2.addItem(str(asts))




            self.ui.resultant_view.setIndexWidget(self.model_resultant.index(i, 0), temp_list1)
            self.ui.resultant_view.setIndexWidget(self.model_resultant.index(i, 1), temp_list2)
            self.ui.resultant_view.setIndexWidget(self.model_resultant.index(i, 2), temp_list3)
            #self.ui.resultant_view.setSizeAdjustPolicy(QTableView.AdjustToContents)

    def keyPressEvent(self, e: QKeyEvent):
        if e.key() == Qt.Key_Return:
            print(e.key())
            if self.ui.pages.currentIndex() == 2:
                self.ui.enter.click()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    debug = 0
    main = Main({}, debug=debug)

    main.show()
    app.exec_()
