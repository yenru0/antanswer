# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_option_color.ui'
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


class Ui_option_color(object):
    def setupUi(self, option_color):
        if option_color.objectName():
            option_color.setObjectName(u"option_color")
        option_color.resize(523, 300)
        self.gridLayout_2 = QGridLayout(option_color)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(option_color)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.cloader = QGridLayout()
        self.cloader.setObjectName(u"cloader")
        self.sli_r = QSlider(option_color)
        self.sli_r.setObjectName(u"sli_r")
        self.sli_r.setMaximum(255)
        self.sli_r.setOrientation(Qt.Horizontal)

        self.cloader.addWidget(self.sli_r, 0, 1, 1, 1)

        self.B = QLabel(option_color)
        self.B.setObjectName(u"B")

        self.cloader.addWidget(self.B, 2, 0, 1, 1)

        self.R = QLabel(option_color)
        self.R.setObjectName(u"R")

        self.cloader.addWidget(self.R, 0, 0, 1, 1)

        self.G = QLabel(option_color)
        self.G.setObjectName(u"G")

        self.cloader.addWidget(self.G, 1, 0, 1, 1)

        self.sli_b = QSlider(option_color)
        self.sli_b.setObjectName(u"sli_b")
        self.sli_b.setMaximum(255)
        self.sli_b.setOrientation(Qt.Horizontal)

        self.cloader.addWidget(self.sli_b, 2, 1, 1, 1)

        self.sli_g = QSlider(option_color)
        self.sli_g.setObjectName(u"sli_g")
        self.sli_g.setMaximum(255)
        self.sli_g.setOrientation(Qt.Horizontal)

        self.cloader.addWidget(self.sli_g, 1, 1, 1, 1)

        self.s_r = QSpinBox(option_color)
        self.s_r.setObjectName(u"s_r")
        self.s_r.setMaximum(255)

        self.cloader.addWidget(self.s_r, 0, 2, 1, 1)

        self.s_g = QSpinBox(option_color)
        self.s_g.setObjectName(u"s_g")
        self.s_g.setMaximum(255)

        self.cloader.addWidget(self.s_g, 1, 2, 1, 1)

        self.s_b = QSpinBox(option_color)
        self.s_b.setObjectName(u"s_b")
        self.s_b.setMaximum(255)

        self.cloader.addWidget(self.s_b, 2, 2, 1, 1)


        self.gridLayout_2.addLayout(self.cloader, 1, 0, 1, 1)

        self.colorView = QWidget(option_color)
        self.colorView.setObjectName(u"colorView")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorView.sizePolicy().hasHeightForWidth())
        self.colorView.setSizePolicy(sizePolicy)
        self.colorView.setMinimumSize(QSize(64, 64))

        self.gridLayout_2.addWidget(self.colorView, 1, 1, 1, 1)


        self.retranslateUi(option_color)
        self.sli_r.valueChanged.connect(self.s_r.setValue)
        self.sli_g.valueChanged.connect(self.s_g.setValue)
        self.sli_b.valueChanged.connect(self.s_b.setValue)
        self.s_r.valueChanged.connect(self.sli_r.setValue)
        self.s_g.valueChanged.connect(self.sli_g.setValue)
        self.s_b.valueChanged.connect(self.sli_b.setValue)

        QMetaObject.connectSlotsByName(option_color)
    # setupUi

    def retranslateUi(self, option_color):
        option_color.setWindowTitle(QCoreApplication.translate("option_color", u"Form", None))
        self.label.setText(QCoreApplication.translate("option_color", u"\uc0c9 \uc124\uc815", None))
        self.B.setText(QCoreApplication.translate("option_color", u"B", None))
        self.R.setText(QCoreApplication.translate("option_color", u"R", None))
        self.G.setText(QCoreApplication.translate("option_color", u"G", None))
    # retranslateUi

