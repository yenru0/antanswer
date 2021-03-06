import sys
from functools import partial
from random import randrange, choice
from threading import Thread, Timer
from time import sleep
from datetime import datetime, time
from dataclasses import dataclass  # python 3.7 >=
from PySide2.QtCore import Qt, QObject, QEvent, QAbstractTableModel, QModelIndex, QRect, QAbstractItemModel, QUrl

from PySide2.QtGui import (QKeyEvent, QPainter,
                           QScrollEvent, QFont, QDesktopServices)
from PySide2.QtWidgets import (QApplication, QPushButton, QMessageBox, QWidget,
                               QMainWindow, QFileDialog, QCheckBox,
                               QAbstractItemView, QErrorMessage,
                               QListWidgetItem, QListWidget,
                               QAbstractScrollArea, QScrollBar, QScrollArea,
                               QStyle, QTableView, QItemDelegate, QStyledItemDelegate,
                               QStyleOptionViewItem)
from typing import Dict, List, Tuple, Any
import json

from function.reader import __anw_std__, __anw_compatibles__, __anw_supports__
from function.structure import *
from components.gui.main_ui import Ui_MainWindow
from main import __version__


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
                    self.loadStageDataModel.reinit(self.file_data[index.row()].ads)
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
        if data is None:  # initial create
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

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.data_stages)

    def columnCount(self, parent: QModelIndex) -> int:
        return len(self.column)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
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

    def setData(self, index: QModelIndex, value: Any, role: int = ...) -> bool:
        if index.isValid():
            if role == Qt.CheckStateRole:
                self.data_real.check(self.data_stages[index.row()].stage_name, bool(value))
            else:
                return False
            return True
        else:
            return False

    def insertRows(self, row: int, count: int, parent: QModelIndex = ...) -> bool:
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
    def __init__(self, data: AntanswerResult, cond: Dict[str, bool], runner):
        super().__init__()
        self.data_result = data
        self.column = ["제출된 답", "답"]
        self.cond = cond
        self.runner = runner
        if self.cond["RESULT_DISPLAY_QUEST"]:
            self.column.append("문제")
        if self.cond["RESULT_MANUAL_POST_CORRECTION"]:
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

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.data_result)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return len(self.column)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.column[section]
        else:
            return None

    def data(self, index: QModelIndex, role: int = ...) -> Any:
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

                    return ";".join(map(str, self.data_result[index.row()][1].answers))

                elif index.column() == 0:
                    return self.data_result[index.row()][0]

                else:
                    return None
            elif role == Qt.CheckStateRole:
                if index.column() == 2:
                    if self.cond["RESULT_DISPLAY_QUEST"]:
                        return None
                    else:
                        return all(self.data_result[index.row()][2])
                elif index.column() == 3:
                    return all(self.data_result[index.row()][2])
        else:
            return None

    def setData(self, index: QModelIndex, value: Any, role: int = ...) -> bool:
        if index.isValid():
            if role == Qt.CheckStateRole:
                if self.cond["RESULT_MANUAL_POST_CORRECTION"]:
                    self.data_result.correct(self.cond, index.row(), bool(value))
                    self.runner.lcptd_set_property()
                else:
                    return False
            else:
                return False
            return True
        else:
            return False


class AnwResultantDataDeligate(QItemDelegate):
    def __init__(self, parent, cond):
        super().__init__(parent)
        self.cond = cond

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        if index.column() == 3:
            v = index.data(Qt.CheckStateRole)
            self.drawCheck(painter, option, option.rect, Qt.Checked if v else Qt.Unchecked)
        elif index.column() == 2:
            if self.cond["RESULT_DISPLAY_QUEST"]:
                super().paint(painter, option, index)
            else:
                v = index.data(Qt.CheckStateRole)
                self.drawCheck(painter, option, option.rect, Qt.Checked if v else Qt.Unchecked)
        else:
            super().paint(painter, option, index)

    def editorEvent(self, event: QEvent, model: QAbstractItemModel, option: QStyleOptionViewItem, index: QModelIndex) -> bool:
        if index.column() == 3:
            if event.type() is QEvent.MouseButtonPress:
                v = bool(model.data(index, Qt.CheckStateRole))
                model.setData(index, not v, Qt.CheckStateRole)
                event.accept()
        elif index.column() == 2:
            if not self.cond["RESULT_DISPLAY_QUEST"]:
                if event.type() is QEvent.MouseButtonPress:
                    v = bool(model.data(index, Qt.CheckStateRole))
                    model.setData(index, not v, Qt.CheckStateRole)
                    event.accept()
        else:
            pass
        return super().editorEvent(event, model, option, index)


class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

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
        self.selected_path: str

        self.samples = None

        self.q_si_beforhead = list()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pages.setCurrentIndex(0)

        ### menubar: action
        self.ui.actionexit.triggered.connect(self.go_exit)
        self.ui.actionreturn_to_manimenu.triggered.connect(self.go_enter)
        self.ui.actiongotooption.triggered.connect(self.go_option)

        ### enter
        self.ui.titleBtn_run.clicked.connect(self.go_setting)
        self.ui.titleBtn_option.clicked.connect(self.go_option)
        self.ui.titleBtn_exit.clicked.connect(self.go_exit)
        self.ui.down_version.setText("version: {}".format(__version__))
        ### setting

        ### setting:파일 추가 및 add 파일 버튼
        # 그리고 model_stage의 선정의
        self.ui.setting_btn_addfile.clicked.connect(self.add_file)

        self.model_stage = AnwLoadStageDataModel(None)  # 미리 정의 해놔야됨

        self.model_file = AnwLoadFileDataModel([], self.model_stage)
        self.model_file_delegate = AnwLoadFileDataDelegate(self.ui.setting_list_file)

        self.ui.setting_list_file.setModel(self.model_file)
        self.ui.setting_list_file.setItemDelegate(self.model_file_delegate)

        self.ui.setting_list_file.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.setting_list_file.setHorizontalScrollBar(RHScrollBar())
        self.ui.setting_list_file.setVerticalScrollBar(RVScrollBar())

        ### setting:stage_table

        # self.model_stage = AnwLoadStageDataModel(None) predef
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
        # time
        self.ui.lcptd_timerate.clicked[bool].connect(self.lcptd_set_timerate)
        self.isRuntime: bool = False
        self.isCounting: bool = False
        self.runtime: float = 0
        self.lastStartingTime: datetime = datetime.now()
        self.th_clock = None

        ### resultant
        self.model_resultant: AnwResultantDataModel
        self.model_resultant_delegate: AnwResultantDataDeligate

        self.ui.resultant_view.setHorizontalScrollBar(RHScrollBar())
        self.ui.resultant_view.setVerticalScrollBar(RVScrollBar())
        # self.ui.resultant_btn_again.clicked.connect()
        self.ui.resultant_btn_setting.clicked.connect(self.go_setting)
        self.ui.resultant_btn_menu.clicked.connect(self.go_enter)
        self.ui.resultant_btn_again.clicked.connect(self.go_run)
        self.ui.resultant_btn_save.clicked.connect(self.resultant_save_result)
        self.ui.resultant_btn_preference.clicked.connect(self.resultant_open_pref)
        self.ui.resultant_btn_openthis.clicked.connect(self.resultant_open_this)

        ### option
        self.ui.option_btn_save.clicked.connect(self.saveOption)
        self.ui.option_btn_back.clicked.connect(self.go_enter)

        self.ui.option_scrollarea.setVerticalScrollBar(RVScrollBar(self.ui.option_scrollarea))

        self.ui.option_font_queston.setText("문제 출력 글꼴")
        self.ui.option_font_input.setText("정답 입력 글꼴")
        self.ui.option_font_lcptd_file.setText("상태창 파일 이름 글꼴")
        self.ui.option_font_queston.setKey("queston")
        self.ui.option_font_input.setKey("input")
        self.ui.option_font_lcptd_file.setKey("lcptd_file")

        self.ui.option_color_lcptd_progress.setText("상태창 진행도 색 설정")
        self.ui.option_color_lcptd_rategress.setText("상태창 정답률 색 설정")
        self.ui.option_color_lcptd_cwgress_c.setText("상태창 맞은 개수 색 설정")
        self.ui.option_color_lcptd_cwgress_w.setText("상태창 틀린 개수 색 설정")
        self.ui.option_color_lcptd_progress.setKey("lcptd_progress")
        self.ui.option_color_lcptd_rategress.setKey("lcptd_rategress")
        self.ui.option_color_lcptd_cwgress_c.setKey("lcptd_cwgress_c")
        self.ui.option_color_lcptd_cwgress_w.setKey("lcptd_cwgress_w")

        self.loadOption()

    def go_setting(self):
        self.ui.pages.setCurrentIndex(1)

    def go_option(self):
        self.loadOption()
        self.ui.pages.setCurrentIndex(4)

    def go_exit(self):
        cMessage = QMessageBox(self)
        c = cMessage.question(self, '나가는 중', '진짜로 나갈건가요?', QMessageBox.Yes | QMessageBox.No)
        if c == QMessageBox.No:
            pass
        else:
            self.beforeEnd()
            self.close()


    def go_enter(self):
        # pause all
        self.ui.pages.setCurrentIndex(0)

    def go_run(self):
        if not any([i.use for i in self.model_file.file_data]):
            tepp = QErrorMessage()
            tepp.showMessage("File wasn't selected")
            tepp.exec_()
            return

        if not any(v for v in self.model_stage.data_real.use.values()):
            tepp = QErrorMessage()
            tepp.showMessage("Stage wasn't selected")
            tepp.exec_()
            return

        if self.init_routine():
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
        T = AntanswerDetail()
        T.set(
            self.ui.extend_normal_wil.value() if self.ui.extend_normal_wil.isEnabled() else 0,
            self.ui.extend_normal_recent if self.ui.extend_normal_recent.isEnabled() else 0,
            self.ui.extend_normal_recentValue if self.ui.extend_normal_recentValue.isEnabled() else 0.0
        )
        for lfd in self.model_file.file_data:
            if lfd.use:
                try:
                    f = open("preference/{}.prefer".format(lfd.name), "r", encoding="utf-8")
                    pref = json.load(f)
                    weights = pref["weights"]
                    f.close()
                except FileNotFoundError as e:
                    with open("preference/{}.prefer".format(lfd.name), "w", encoding="utf-8") as f:
                        weights = {}
                        for stn, stg in lfd.ads.stages.items():
                            weights[stn] = []
                            for e in stg:
                                weights[stn].append(0)
                        json.dump({"weights": weights}, f, indent=2)
                except json.JSONDecodeError as e:
                    cMessage = QMessageBox(self)
                    c = cMessage.question(self, '부서지다.', "'preference/{}.prefer'가 부서진것 같습니다.\n초기화하겠습니까?".format(lfd.name),
                                          QMessageBox.Yes | QMessageBox.No)
                    if c == QMessageBox.No:
                        weights = {}
                        for stn, stg in lfd.ads.stages.items():
                            weights[stn] = []
                            for e in stg:
                                weights[stn].append(0)
                    else:
                        with open("preference/{}.prefer".format(lfd.name), "w", encoding="utf-8") as f:
                            weights = {}
                            for stn, stg in lfd.ads.stages.items():
                                weights[stn] = []
                                for e in stg:
                                    weights[stn].append(0)
                            json.dump({"weights": weights}, f, indent=2)

                self.samples = lfd.ads.sampling(T, weights, weightAddAlt=self.ui.extend_normal_weightAlg.currentIndex(),
                                                weightMult=self.ui.extend_normal_weightMult.value())
                next(self.samples)
                self.selected_path = lfd.dir
                self.selected = lfd.ads
                self.selected.clearResult()
                break
        if self.selected.detail_used.wil == 0:
            tepp = QErrorMessage()
            tepp.showMessage("wil 변수가 0입니다 이는 용납할 수 없습니다.")
            tepp.exec_()
            return False
        self.runtime = 0.0
        self.isRuntime = True
        self.isCounting = False
        self.lcptd_set_timerate()
        self.th_clock = Thread(target=self.lcptd_timerate_live, daemon=True)
        self.th_clock.start()
        self.cond_used = {}

        for ck, v in self.selected.cond.items():
            if v is None:
                self.cond_used[ck] = self.cond_default[ck]
            else:
                self.cond_used[ck] = v

        self.lcptd_reset()
        self.lcptd_set_file(self.selected.name)

        self.next_routine(True)
        return True

    def next_routine(self, isFirst: bool = False):
        if not isFirst:
            # get inputs from input
            inputs = [self.ui.input.item(i).text() for i in range(self.ui.input.count())]
            self.selected.result.answer(inputs)
            self.selected.result.check(self.cond_used)

        # init
        try:
            aq: AntanswerElement = next(self.samples)

        except StopIteration as e:
            self.lcptd_set_property()
            self.go_resultant()

            return

        self.lcptd_set_property()
        t_s = ""

        for i, q in enumerate(aq.getRealQuestion(self.cond_used["REVERSE_AQ"])):
            t_s += "(" + str(i) + ")" + q + "\n"

        self.queston_update(t_s)
        self.input_reset(len(aq.answers))

    def queston_reset(self):
        self.ui.queston.setText("")

    def input_reset(self, l: int = 0):
        self.ui.input.clear()
        for i in range(l):
            temp_item = QListWidgetItem("")
            temp_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsDragEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            self.ui.input.addItem(temp_item)

    def log_reset(self):
        self.ui.log.clear()

    def queston_update(self, q: str):
        self.ui.queston.setText(q)

    def log_update(self, log):
        pass

    def lcptd_set_file(self, name: str):
        self.ui.lcptd_file.setText(name)

    def lcptd_set_property(self):
        self.ui.lcptd_progress.setValue(self.selected.result.count)
        self.ui.lcptd_progress.setMaximum(self.selected.detail_used.wil)
        if self.selected.result.count == 0:
            self.ui.lcptd_rategress.setMaximum(1)
            self.ui.lcptd_cwgress.setMaximum(1)
        else:
            self.ui.lcptd_rategress.setMaximum(self.selected.result.count)
            self.ui.lcptd_cwgress.setMaximum(self.selected.result.count)
        self.ui.lcptd_rategress.setValue(self.selected.result.score)
        self.ui.lcptd_cwgress.setValue(self.selected.result.score)
        self.ui.lcptd_cwgress.setFormat("%s:%s" % (
            self.selected.result.score,
            self.selected.result.count - self.selected.result.score
        )
                                        )

    def lcptd_reset(self):
        self.ui.lcptd_file.setText("")
        self.ui.lcptd_progress.setMaximum(0)
        self.ui.lcptd_rategress.setMaximum(0)
        self.ui.lcptd_cwgress.setMaximum(0)
        self.ui.lcptd_timerate.setText("")

    def lcptd_set_timerate(self):
        if self.isRuntime:
            if self.isCounting:
                self.isCounting = False
                self.runtime += (datetime.now() - self.lastStartingTime).total_seconds()
            else:
                self.isCounting = True
                self.lastStartingTime = datetime.now()
        else:
            pass

    def lcptd_fin_timerate(self):
        pass

    def lcptd_timerate_live(self):
        if self.isRuntime:
            if self.isCounting:
                self.ui.lcptd_timerate.setText(str(int(
                    (datetime.now()-self.lastStartingTime).total_seconds()
                                                   + self.runtime)) + "초")
            else:
                pass
            Timer(0.8, self.lcptd_timerate_live).start()
        else:
            pass

    def resultant_set(self):
        self.isRuntime = False
        self.isCounting = False

        self.ui.resultant_btn_save.setEnabled(True)
        self.model_resultant = AnwResultantDataModel(self.selected.result,
                                                     self.cond_used,
                                                     self
                                                     )

        self.model_resultant_delegate = AnwResultantDataDeligate(self.ui.resultant_view,
                                                                 self.cond_used,
                                                                 )
        self.ui.resultant_view.setModel(self.model_resultant)
        self.ui.resultant_view.setItemDelegate(self.model_resultant_delegate)

    def resultant_save_result(self):
        self.ui.resultant_btn_save.setEnabled(False)
        for r in self.selected.result:
            if not all(r[2]):
                self.selected.weights[r[1].stage_name][r[1].id] += self.selected.weightMult
            print(self.selected.weightMult)
        with open("preference/{}.prefer".format(self.selected.name), "w", encoding='utf-8') as f:
            json.dump({"weights": self.selected.weights}, f, indent=2)

    def resultant_open_this(self):
        QDesktopServices.openUrl(QUrl(self.selected_path))

    def resultant_open_pref(self):
        cMessage = QMessageBox(self)
        c = cMessage.about(None, "존재하지 않는 기능", "이 기능은 아직 존재하지 않습니다.")

    def keyPressEvent(self, e: QKeyEvent):
        if e.key() == Qt.Key_Return:
            print(e.key())
            if self.ui.pages.currentIndex() == 2:
                self.ui.enter.click()

    def loadOption(self):
        """
        load option from option.json
        :return:
        """

        # TODO: 예외처리 세게 좀 필요할 듯
        with open("option.json", "r", encoding="utf-8") as f:
            v = json.load(f)

            font = v[self.ui.option_font_queston.key]["font-family"]
            size = v[self.ui.option_font_queston.key]["font-size"]
            self.ui.queston.setFontFamily(font)
            self.ui.queston.setFontPointSize(int(size))
            self.ui.option_font_queston.setComboFont(font)
            self.ui.option_font_queston.setSize(int(size))

            font = v[self.ui.option_font_input.key]["font-family"]
            size = v[self.ui.option_font_input.key]["font-size"]
            self.ui.input.setStyleSheet(f"""font: {size}pt {font}""")
            self.ui.option_font_input.setComboFont(font)
            self.ui.option_font_input.setSize(int(size))

            font = v[self.ui.option_font_lcptd_file.key]["font-family"]
            size = v[self.ui.option_font_lcptd_file.key]["font-size"]
            ft = QFont(font, pointSize=int(size))
            self.ui.lcptd_file.setFont(ft)
            self.ui.option_font_lcptd_file.setComboFont(font)
            self.ui.option_font_lcptd_file.setSize(int(size))

            t = v[self.ui.option_color_lcptd_progress.key]
            self.ui.lcptd_progress.setStyleSheet("""
            QProgressBar::chunk{
                background-color: rgb(%s, %s, %s)
            }
            """ % (t["r"], t["g"], t["b"]))
            self.ui.option_color_lcptd_progress.setColors(t["r"], t["g"], t["b"])

            t = v[self.ui.option_color_lcptd_progress.key]
            self.ui.lcptd_progress.setStyleSheet("""
                        QProgressBar::chunk{
                            background-color: rgb(%s, %s, %s);
                        }
                        """ % (t["r"], t["g"], t["b"]))
            self.ui.option_color_lcptd_progress.setColors(t["r"], t["g"], t["b"])

            t = v[self.ui.option_color_lcptd_rategress.key]
            self.ui.lcptd_rategress.setStyleSheet("""
                        QProgressBar::chunk{
                            background-color: rgb(%s, %s, %s);
                        }
                        """ % (t["r"], t["g"], t["b"]))
            self.ui.option_color_lcptd_rategress.setColors(t["r"], t["g"], t["b"])

            t_c = v[self.ui.option_color_lcptd_cwgress_c.key]
            t_w = v[self.ui.option_color_lcptd_cwgress_w.key]
            self.ui.lcptd_cwgress.setStyleSheet("""
                        QProgressBar{
                            background-color: rgb(%s, %s, %s);
                        }
                        QProgressBar::chunk{
                            background-color: rgb(%s, %s, %s);
                        }
                        """ % (t_w["r"], t_w["g"], t_w["b"], t_c["r"], t_c["g"], t_c["b"]))
            self.ui.option_color_lcptd_cwgress_c.setColors(t_c["r"], t_c["g"], t_c["b"])
            self.ui.option_color_lcptd_cwgress_w.setColors(t_w["r"], t_w["g"], t_w["b"])

    def saveOption(self):
        with open("option.json", "w", encoding="utf-8") as f:
            T = {}
            T[self.ui.option_font_queston.key] = \
                self.ui.option_font_queston.getOValue()

            T[self.ui.option_font_input.key] = \
                self.ui.option_font_input.getOValue()

            T[self.ui.option_font_lcptd_file.key] = \
                self.ui.option_font_lcptd_file.getOValue()

            T[self.ui.option_color_lcptd_progress.key] = \
                self.ui.option_color_lcptd_progress.getOValue()

            T[self.ui.option_color_lcptd_rategress.key] = \
                self.ui.option_color_lcptd_rategress.getOValue()

            T[self.ui.option_color_lcptd_cwgress_c.key] = \
                self.ui.option_color_lcptd_cwgress_c.getOValue()

            T[self.ui.option_color_lcptd_cwgress_w.key] = \
                self.ui.option_color_lcptd_cwgress_w.getOValue()

            json.dump(T, f, indent=2)

        self.loadOption()

    def beforeEnd(self):
        self.isRuntime = False