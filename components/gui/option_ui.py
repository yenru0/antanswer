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

    def setText(self, text: str):
        self.label.setText(text)
        self.colorView.setAutoFillBackground(True)

    def changeColor(self):
        self.m_color.setRgb(*self.color)
        pal: QPalette = self.colorView.palette()
        pal.setColor(QPalette.Window, self.m_color)

        self.colorView.setAutoFillBackground(True)
        self.colorView.setPalette(pal)
        self.colorChanged.emit()

    @property
    def color(self) -> Tuple[int, int, int, int]:
        return self.s_r.value(), self.s_g.value(), self.s_b.value(), 255

class Widget_Option_Font(QWidget, Ui_option_font):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

    def setText(self, text: str):
        self.label.setText(text)
