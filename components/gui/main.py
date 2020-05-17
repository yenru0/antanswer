import sys
from functools import partial
from random import randrange, choice
from dataclasses import dataclass  # python 3.7 >=
from PySide2.QtCore import Qt, QObject, QEvent, QAbstractTableModel, QModelIndex, QRect, QAbstractItemModel

from PySide2.QtGui import (QStandardItem, QStandardItemModel, QKeyEvent, QPainter,
                           QScrollEvent)
from PySide2.QtWidgets import (QApplication, QPushButton, QMessageBox, QWidget,
                               QMainWindow, QFileDialog, QCheckBox,
                               QAbstractItemView, QErrorMessage,
                               QListWidgetItem, QListWidget,
                               QAbstractScrollArea, QScrollBar, QScrollArea,
                               QStyle, QTableView, QItemDelegate, QStyledItemDelegate,
                               QStyleOptionViewItem)
from typing import Dict, List, Any


from function.reader.reader import READ_ANW
from function.structure import *
from components.gui.main_ui import Ui_MainWindow


@dataclass
class LoadFileData():
    name: str
    dir: str
    use: int  # 부울 같은 부울 같지 않은 부울 같은 정수
    ads: AntanswerDataStruct = None
    def __getitem__(self, item):
        if isinstance(item, int):
            if item == 0:
                return self.name
            elif item == 1:
                return self.dir
            elif item == 2:
                return self.use
            else:
                raise TypeError
        elif isinstance(item, str):
            if item == "name":
                return self.name
            elif item == "dir":
                return self.dir
            elif item == "use":
                return self.use
            else:
                raise TypeError

    def __setitem__(self, item, value):
        if isinstance(item, int):
            if item == 0:
                self.name = value
            elif item == 1:
                self.dir = value
            elif item == 2:
                self.use = value
            else:
                raise TypeError
        elif isinstance(item, str):
            if item == "name":
                self.name = value
            elif item == "dir":
                self.dir = value
            elif item == "use":
                self.use = value
            else:
                raise TypeError
        return None


class RHScrollBar(QScrollBar):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setProperty("rsign", "false")

        self.setStyleSheet("""
QScrollBar[rsign=\"false\"] {
    background: #f1f1f1;
	height: 5px;
}
QScrollBar[rsign=\"true\"] {
    background: #f1f1f1;
	height: 10px;
}


QScrollBar::handle {
    background: #888;
}



QScrollBar::handle:hover {
	background: #555;
}


        """)

    def enterEvent(self, event: QEvent):
        self.setProperty("rsign", "true")
        self.setStyleSheet(self.styleSheet())

    def leaveEvent(self, event: QEvent):
        self.setProperty("rsign", "false")
        self.setStyleSheet(self.styleSheet())


class RVScrollBar(QScrollBar):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setProperty("rsign", "false")

        self.setStyleSheet("""
QScrollBar[rsign=\"false\"] {
  background: #f1f1f1;
	width: 5px;
}
QScrollBar[rsign=\"true\"] {
  background: #f1f1f1;
	width: 10px;
}


QScrollBar::handle {
  background: #888;
}


QScrollBar::handle:hover {
	background: #555;
}


        """)

    def enterEvent(self, event: QEvent):
        self.setProperty("rsign", "true")
        self.setStyleSheet(self.styleSheet())

    def leaveEvent(self, event: QEvent):
        self.setProperty("rsign", "false")
        self.setStyleSheet(self.styleSheet())


class AnwLoadFileDataModel(QAbstractTableModel):
    def __init__(self, data: List[LoadFileData], loadstagedatamodel):
        QAbstractTableModel.__init__(self)
        self.file_data: List[LoadFileData] = data
        self.column = ["이름", "위치", "사용", "삭제"]

        self.loadStageDataModel = loadstagedatamodel

    def checkData(self):
        """
        isvalid
        :return:
        """
        pass

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        """
        :param index:
        :return:
        """
        if index.column() == 2:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable
        elif index.column() == 3:
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.file_data)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return len(self.column)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.column[section]
        else:
            return None

    def data(self, index: QModelIndex, role: int = ...) -> Any:
        """
        대충 데이터 디스플레이하는 것
        :param index:
        :param role:
        :return
        """

        if index.isValid():

            if role == Qt.DisplayRole:
                if index.column() == 2 or index.column() == 3:
                    # return QPushButton()
                    pass
                else:
                    return self.file_data[index.row()][index.column()]
            elif role == Qt.CheckStateRole:
                if index.column() == 2:
                    return self.file_data[index.row()][2]
            elif role == Qt.DecorationRole:
                if index.column() == 2:

                    pass
                else:
                    return None
        else:
            return None

    def setData(self, index: QModelIndex, value: Any, role: int = ...) -> bool:
        if index.isValid():
            if role == Qt.CheckStateRole:
                if bool(value):
                    for i, t in enumerate(self.file_data):
                        if t[index.column()] is True:
                            t[index.column()] = False
                            break
                    self.file_data[index.row()][index.column()] = bool(value)
                    self.loadStageDataModel.reinit (self.file_data[index.row()].ads)
                else:

                    self.file_data[index.row()][index.column()] = bool(value)
                    self.loadStageDataModel.reinit(None)
            else:
                return False
            return True
        else:
            return False

    def insertRows(self, row: int, count: int, parent: QModelIndex = ...) -> bool:
        self.beginInsertRows(QModelIndex(), row, row + count)
        for i in range(count):
            self.file_data.append(LoadFileData())
        self.endInsertRows()
        return True

    def removeRows(self, row: int, count: int, parent: QModelIndex = ...) -> bool:
        if len(self.file_data) >= count and row - count + 1 >= 0:
            self.beginRemoveRows(QModelIndex(), row - count + 1, row)
            for i in range(count):
                self.file_data.pop(row - count + 1)
            self.endRemoveRows()
            print(self.file_data)

        else:
            return False
        return True

    def append(self, data: LoadFileData):
        self.beginInsertRows(QModelIndex(), len(self.file_data), len(self.file_data))
        self.file_data.append(data)
        self.endInsertRows()
        return True

class AnwLoadFileDataDelegate(QItemDelegate):

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        if True:
            if index.column() == 3:
                self.parent().openPersistentEditor(index)
            elif index.column() == 2:
                v = index.data(Qt.CheckStateRole)
                self.drawCheck(painter, option, option.rect, Qt.Checked if v else Qt.Unchecked)
            else:
                super().paint(painter, option, index)
        else:
            super().paint(painter, option, index)

    def editorEvent(self, event: QEvent, model: QAbstractItemModel, option: QStyleOptionViewItem, index: QModelIndex) -> bool:
        if True:
            if index.column() == 2:
                if event.type() is QEvent.MouseButtonPress:
                    v = bool(model.data(index, Qt.CheckStateRole))
                    model.setData(index, not v, Qt.CheckStateRole)
                    event.accept()

            else:
                pass

        return super().editorEvent(event, model, option, index)

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex) -> QWidget:
        if index.column() == 3:
            btn = QPushButton("X", parent)
            btn.clicked.connect(lambda x: print(index.model().removeRows(index.row(), 1, index)))
            return btn
        else:
            super().createEditor(parent, option, index)


class AnwLoadStageDataModel(QAbstractTableModel):
    def __init__(self, data: AntanswerDataStruct):
        super().__init__()
        if data is None: # initial create
            self.data_stages = []
            self.column = []
            return
        elif data.isloaded is False:
            self.data_stages = []
            self.column = []
            return
        self.name: str = data.name
        self.data_real = data
        self.data_stages: List[AntanswerStage] = list(data.stages.values())

        self.column = ["파일", "스테이지", "사용"]
        # 방치플레이 하는거임!
        # 생각해보니 아직은 초기 __init__(self)에서 할 짓이 없더라고

    def reinit(self, data: AntanswerDataStruct):
        if data is None:
            self.beginResetModel()
            self.data_stages: List[AntanswerStage] = []
            self.column = []
            self.endResetModel()
            return
        elif data.isloaded is False:
            self.beginResetModel()
            self.data_stages: List[AntanswerStage] = []
            self.column = []
            self.endResetModel()
            return

        self.beginResetModel()
        self.data_stages: List[AntanswerStage] = []
        self.column = ["파일", "스테이지", "사용"]
        self.endResetModel()
        self.name: str = data.name
        self.data_real = data
        self.data_stages: List[AntanswerStage] = list(data.stages.values())
        self.beginResetModel()
        self.endResetModel()

        self.beginInsertRows(QModelIndex(), 0, len(self.data_stages))
        self.endInsertRows()


    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        if index.column() == 2:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable
        else:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def rowCount(self, parent: QModelIndex=...) -> int:
        return len(self.data_stages)

    def columnCount(self, parent: QModelIndex) -> int:
        return len(self.column)

    def headerData(self, section:int, orientation:Qt.Orientation, role:int=...) -> Any:
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.column[section]
        else:
            return None

    def data(self, index: QModelIndex, role: int = ...) -> Any:
        if index.isValid():
            if role == Qt.DisplayRole:
                if index.column() == 2:
                    return None
                elif index.column() == 0:
                    return self.name
                elif index.column() == 1:
                    return self.data_stages[index.row()].stage_name
                else:
                    pass
            elif role == Qt.CheckStateRole:
                if index.column() == 2:
                    return self.data_real.use[self.data_stages[index.row()].stage_name]

        else:
            pass

    def setData(self, index:QModelIndex, value:Any, role:int=...) -> bool:
        if index.isValid():
            if role == Qt.CheckStateRole:
                self.data_real.check(self.data_stages[index.row()].stage_name, bool(value))
            else:
                return False
            return True
        else:
            return False

    def insertRows(self, row:int, count:int, parent:QModelIndex=...) -> bool:
        """
        immutable
        """
        return False

    def removeRows(self):
        """
        immutable
        """
        return False


class AnwLoadStageDataDelegate(QItemDelegate):
    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        if index.column() == 2:
            v = index.data(Qt.CheckStateRole)
            self.drawCheck(painter, option, option.rect, Qt.Checked if v else Qt.Unchecked)
        else:
            super().paint(painter, option, index)

    def editorEvent(self, event: QEvent, model: QAbstractItemModel, option: QStyleOptionViewItem, index: QModelIndex) -> bool:
        if index.column() == 2:
            if event.type() is QEvent.MouseButtonPress:
                v = bool(model.data(index, Qt.CheckStateRole))
                model.setData(index, not v, Qt.CheckStateRole)
                event.accept()
        else:
            pass
        return super().editorEvent(event, model, option, index)

class AnwResultantDataModel(QAbstractTableModel):
    def __init__(self, data: AntanswerResult, cond: Dict[str, bool]):
        super().__init__()
        self.data_result = data
        self.column = ["제출된 답", "답"]
        if cond["RESULT_DISPLAY_QUEST"]:
            self.column.append("문제")
        if cond["RESULT_MANUAL_POST_CORRECTION"]:
            self.column.append("수정")
    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        if index.column() == 3:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable
        elif index.column() == 2:
            if self.cond["RESULT_DISPLAY_QUEST"]:
                return Qt.ItemIsEnabled | Qt.ItemIsSelectable
            else:
                return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
    def rowCount(self, parent:QModelIndex=...) -> int:
        return len(self.data_result)

    def columnCount(self, parent:QModelIndex=...) -> int:
        return len(self.column)

    def headerData(self, section:int, orientation:Qt.Orientation, role:int=...) -> Any:
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.column[section]
        else:
            return None

    def data(self, index:QModelIndex, role:int=...) -> Any:
        if index.isValid():
            if role == Qt.DisplayRole:
                if index.column() == 3:
                    return None
                elif index.column() == 2:
                    if self.cond["RESULT_DISPLAY_QUEST"]:
                        return self.data_result[index.row()][1].getRealQuestion()

                    else:
                        return None
                elif index.column() == 1:
                    return self.data_result[index.row()][1].answers

                elif index.column() == 0:
                    return self.data_result[index.row()][0]

                else:
                    return None
            elif role == Qt.CheckStateRole:
                return self.data_result[index.row()][2]
        else:
            return None

    def setData(self, index:QModelIndex, value:Any, role:int=...) -> bool:
        if index.isValid():
            if role == Qt.CheckStateRole:
                if self.cond["RESULT_MANUAL_POST_CORRECTION"]:
                    self.data_result.check(index.row(), bool(value))
                else:
                    return False
            else:
                return False
            return True
        else:
            return False



class AnwResultantDataDeligate(QItemDelegate):
    pass




class Main(QMainWindow):

    def __init__(self, opt, parent=None):
        QMainWindow.__init__(self, parent)

        ### opt
        self.anw_standard = opt["anw_standard"]
        self.cond_default = {  # string: bool
            # Anw ReaderMain
            "COMP_IGNORE_SPACE": True,  # ignoring space, blank like '\t' won't be replaced
            "COMP_IGNORE_CASE": True,  # ignoring case, replace upper to lower
            "ANSWER_WITHOUT_ORDER": True,  # when answering quest, order don't interrupt you
            "COMP_NOT": True,  # ignoring sequence matcher(compare) method
            "RESULT_DISPLAY_QUEST": True,  # not displaying Quest
            "COMP_IGNORE_LAST_PERIOD": True,  # ignoring the last period
            "RESULT_MANUAL_POST_CORRECTION": True,  # post correction at result time GUI main cond
            "REVERSE_AQ": False  # reverse AQ in element
        }
        self.cond_used = {}

        self.selected: AntanswerDataStruct

        self.samples = None


        self.q_si_beforhead = list()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pages.setCurrentIndex(0)

        ### menubar: action
        self.ui.actionexit.triggered.connect(self.go_exit)
        self.ui.actionreturn_to_manimenu.triggered.connect(self.go_enter)

        ### enter
        self.ui.titleBtn_run.clicked.connect(self.go_setting)
        self.ui.titleBtn_option.clicked.connect(self.go_option)
        self.ui.titleBtn_exit.clicked.connect(self.go_exit)
        self.ui.down_version.setText("version: {}".format(opt["version"]))
        ### setting

        ### setting:파일 추가 및 add 파일 버튼
        # 그리고 model_stage의 선정의
        self.ui.setting_btn_addfile.clicked.connect(self.add_file)

        self.model_stage = AnwLoadStageDataModel(None) # 미리 정의 해놔야됨

        self.model_file = AnwLoadFileDataModel([], self.model_stage)
        self.model_file_delegate = AnwLoadFileDataDelegate(self.ui.setting_list_file)

        self.ui.setting_list_file.setModel(self.model_file)
        self.ui.setting_list_file.setItemDelegate(self.model_file_delegate)

        self.ui.setting_list_file.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.setting_list_file.setHorizontalScrollBar(RHScrollBar())
        self.ui.setting_list_file.setVerticalScrollBar(RVScrollBar())

        ### setting:stage_table

        #self.model_stage = AnwLoadStageDataModel(None) predef
        self.model_stage_delegate = AnwLoadStageDataDelegate(self.ui.setting_stage_table)

        self.ui.setting_stage_table.setModel(self.model_stage)
        self.ui.setting_stage_table.setItemDelegate(self.model_stage_delegate)

        self.ui.setting_stage_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.setting_stage_table.setHorizontalScrollBar(RHScrollBar())
        self.ui.setting_stage_table.setVerticalScrollBar(RVScrollBar())

        ### setting:btn_real_run & btn_real_gomenu
        self.ui.setting_btn_real_run.clicked.connect(self.go_run)
        self.ui.setting_btn_real_gomenu.clicked.connect(self.go_enter)

        ### do

        self.queston_template = """<!DOCTYPE html><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style=" font-family:'13 Malgun Gothic'; font-size:12pt; font-weight:400; font-style:normal;"><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Malgun Gothic'; font-size:14pt; font-weight:600;">%s</span></p></body></html>"""

        self.input_reset()
        self.queston_reset()
        self.log_reset()

        self.ui.input.setHorizontalScrollBar(RHScrollBar())
        self.ui.log.setHorizontalScrollBar(RHScrollBar())
        self.ui.input.setVerticalScrollBar(RVScrollBar())
        self.ui.log.setVerticalScrollBar(RVScrollBar())

        self.ui.enter.clicked.connect(partial(self.next_routine, isFirst=False))

        ### dock
        self.lcptd_reset()

        ### resultant
        self.model_resultant = QStandardItemModel()
        self.ui.resultant_view.setHorizontalScrollBar(RHScrollBar())
        self.ui.resultant_view.setVerticalScrollBar(RVScrollBar())
        # self.ui.resultant_btn_again.clicked.connect()
        self.ui.resultant_btn_setting.clicked.connect(self.go_setting)
        self.ui.resultant_btn_menu.clicked.connect(self.go_enter)
        self.ui.resultant_btn_again.clicked.connect(self.go_run)

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

    def add_file(self):
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

                ads = AntanswerDataStruct()
                print("O")
                ads.load(f)

            except Exception as e:
                print(e)
                tepp = QErrorMessage()
                tepp.showMessage("wrong anw file:", str(e))
                tepp.exec_()
                f.close()
                continue
            finally:
                f.close()

            for j in self.model_file.file_data:
                if j.name == ads.name:
                    tepp = QErrorMessage()
                    tepp.showMessage("duplicate named file:", ads.name)
                    tepp.exec_()
                    break
            else:
                self.model_file.append(LoadFileData(ads.name, i, False, ads))


    ### routine: do

    def init_routine(self):
        for lfd in self.model_file.file_data:
            self.samples = lfd.ads.sampling()
            self.selected = lfd.ads
            break

        self.cond_used = {}

        for ck, v in self.selected.cond.items():
            if v is None:
                self.cond_used[ck] = self.cond_default[ck]
            else:
                self.cond_used[ck] = v

        self.lcptd_reset()
        self.lcptd_set_file(self.temp_selected_stage.keys())

        self.next_routine(False, True)

    def next_routine(self, enable=False, isFirst=False):
        # process before head
        if not isFirst:
            inputs = [self.ui.input.item(i).text() for i in range(self.ui.input.count())]
            self.selected.result.answer(inputs)
            self.selected.result.check()


        # init
        try:
            aq: AntanswerElement = next(self.samples)
        except StopIteration as e:
            self.go_resultant()
            return

        self.lcptd_set_property()

        t_s = ""

        for i, q in enumerate(aq.getRealQuestion(self.cond_used["REVERSE_AQ"])):
            t_s += "(" + str(i) + ")" + q + "\n"

        self.queston_update(t_s)
        self.input_reset(len(aq.answers))

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


    def lcptd_set_file(self, names):
        self.ui.lcptd_file.setText(";".join(names))

    def lcptd_set_property(self):
        self.ui.lcptd_progress.setValue(self.count)
        self.ui.lcptd_progress.setMaximum(self.detail[0])
        if self.count == 0:
            self.ui.lcptd_rategress.setMaximum(1)
            self.ui.lcptd_cwgress.setMaximum(1)
        else:
            self.ui.lcptd_rategress.setMaximum(self.count)
            self.ui.lcptd_cwgress.setMaximum(self.count)
        self.ui.lcptd_rategress.setValue(self.score)
        self.ui.lcptd_cwgress.setValue(self.score)
        self.ui.lcptd_cwgress.setFormat("%s:%s" % (self.score, self.count - self.score))

    def lcptd_reset(self):
        self.ui.lcptd_file.setText("")
        self.ui.lcptd_progress.setMaximum(0)
        self.ui.lcptd_rategress.setMaximum(0)
        self.ui.lcptd_cwgress.setMaximum(0)

    def resultant_set(self):
        if self.cond_used["RESULT_DISPLAY_QUEST"]:
            self.model_resultant.setColumnCount(4)
        else:
            self.model_resultant.setColumnCount(3)
        self.model_resultant.setRowCount(self.detail[0])
        self.ui.resultant_view.setModel(self.model_resultant)
        for i, sts in self.correct.items():
            temp_list1 = QListWidget()
            temp_list2 = QListWidget()
            temp_list3 = QListWidget()
            temp_list1.setMinimumHeight(100)
            temp_list1.setMinimumWidth(400)
            temp_list2.setMinimumHeight(100)
            temp_list2.setMinimumWidth(400)
            temp_list3.setMinimumHeight(100)
            temp_list3.setMinimumWidth(400)
            temp_list1.setHorizontalScrollBar(RHScrollBar())
            temp_list1.setVerticalScrollBar(RVScrollBar())
            temp_list2.setHorizontalScrollBar(RHScrollBar())
            temp_list2.setVerticalScrollBar(RVScrollBar())
            temp_list3.setHorizontalScrollBar(RHScrollBar())
            temp_list3.setVerticalScrollBar(RVScrollBar())
            temp_list1.setEditTriggers(QAbstractItemView.NoEditTriggers)
            temp_list2.setEditTriggers(QAbstractItemView.NoEditTriggers)
            temp_list3.setEditTriggers(QAbstractItemView.NoEditTriggers)
            # correct (isCorrect, mrs, scope_stage, scope_name, elem_ci, inputs, q_si)
            if self.cond_used["REVERSE_AQ"]:
                qcol, acol = 1, 2
            else:
                qcol, acol = 2, 1
            # asts and rtst
            for j, rsts in enumerate(sts[5]):
                temp_list1.addItem(rsts)
                temp_list2.addItem(str(self.temp_selected_files[sts[3]][2]["stages"][sts[2]][sts[4]][acol][j]))

            for j, q_si in enumerate(sts[6]):
                temp_list3.addItem(self.temp_selected_files[sts[3]][2]["stages"][sts[2]][sts[4]][qcol][j][q_si])

            temp_manual_checkbox = QCheckBox()
            temp_manual_checkbox.setChecked(self.correct[i][0])
            temp_manual_checkbox.clicked[bool].connect(partial(self.resultant_manual_crr,
                                                               stage_name=self.correct[i][2],
                                                               file_name=self.correct[i][3],
                                                               ci=self.correct[i][4]
                                                               ))
            if self.cond_used["RESULT_MANUAL_POST_CORRECTION"]:
                temp_manual_checkbox.setCheckable(True)
            else:
                temp_manual_checkbox.setCheckable(False)

            self.ui.resultant_view.setIndexWidget(self.model_resultant.index(i, 0), temp_list1)
            self.ui.resultant_view.setIndexWidget(self.model_resultant.index(i, 1), temp_list2)
            if self.cond_used["RESULT_DISPLAY_QUEST"]:
                self.ui.resultant_view.setIndexWidget(self.model_resultant.index(i, 2), temp_list3)
                self.ui.resultant_view.setIndexWidget(self.model_resultant.index(i, 3), temp_manual_checkbox)
            else:
                self.ui.resultant_view.setIndexWidget(self.model_resultant.index(i, 2), temp_manual_checkbox)
            # self.ui.resultant_view.setSizeAdjustPolicy(QTableView.AdjustToContents)

    def resultant_manual_crr(self, enable, stage_name, file_name, ci):
        if enable:
            self.score += 1
        else:
            self.score -= 1
        self.lcptd_set_property()

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
