# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_option_font.ui'
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


class Ui_option_font(object):
    def setupUi(self, option_font):
        if option_font.objectName():
            option_font.setObjectName(u"option_font")
        option_font.resize(400, 185)
        self.gridLayout = QGridLayout(option_font)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(option_font)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.fontComboBox = QFontComboBox(option_font)
        self.fontComboBox.setObjectName(u"fontComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
        self.fontComboBox.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.fontComboBox, 1, 0, 1, 1)

        self.spinBox = QSpinBox(option_font)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)


        self.retranslateUi(option_font)

        QMetaObject.connectSlotsByName(option_font)
    # setupUi

    def retranslateUi(self, option_font):
        option_font.setWindowTitle(QCoreApplication.translate("option_font", u"Form", None))
        self.label.setText(QCoreApplication.translate("option_font", u"\ub514\uc2a4\ud50c\ub808\uc774 \ud3f0\ud2b8", None))
    # retranslateUi

