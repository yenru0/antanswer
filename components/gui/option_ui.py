from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QColor, QPalette
from PySide2.QtCore import Qt, Signal
from components.gui.widget_option_color_ui import Ui_option_color
from components.gui.widget_option_font_ui import Ui_option_font

from typing import Tuple


class Widget_Option_Color(QWidget, Ui_option_color):
    colorChanged = Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.m_color: QColor = QColor(*self.color)
        self.s_r.valueChanged.connect(self.changeColor)
        self.s_g.valueChanged.connect(self.changeColor)
        self.s_b.valueChanged.connect(self.changeColor)
        self.changeColor()
        self.key = ""

    def setText(self, text: str):
        self.label.setText(text)
        self.colorView.setAutoFillBackground(True)

    def setKey(self, key: str):
        self.key = "color:{0}".format(key)

    def getOValue(self):
        return dict(zip(("r", "g", "b"), self.color))

    def setColors(self, r: int, g: int, b: int):
        self.s_r.setValue(r)
        self.s_g.setValue(g)
        self.s_b.setValue(b)
        self.changeColor()

    def changeColor(self):
        self.m_color.setRgb(*self.color)
        pal: QPalette = self.colorView.palette()
        pal.setColor(QPalette.Window, self.m_color)

        self.colorView.setAutoFillBackground(True)
        self.colorView.setPalette(pal)
        self.colorChanged.emit()

    @property
    def color(self) -> Tuple[int, int, int]:
        return self.s_r.value(), self.s_g.value(), self.s_b.value()


class Widget_Option_Font(QWidget, Ui_option_font):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.key = ""

    def setText(self, text: str):
        self.label.setText(text)

    def setKey(self, key: str):
        self.key = "font:{0}".format(key)

    def getOValue(self):
        return {"font-family": str(self.fontComboBox.currentFont().family()), "font-size": self.spinBox.value()}

    def setComboFont(self, font: str):
        self.fontComboBox.setCurrentFont(font)

    def setSize(self, size: int):
        self.spinBox.setValue(int(size))


