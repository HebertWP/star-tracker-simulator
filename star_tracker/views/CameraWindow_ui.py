# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CameraWindows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CameraWindow(object):
    def setupUi(self, CameraWindow):
        if not CameraWindow.objectName():
            CameraWindow.setObjectName(u"CameraWindow")
        CameraWindow.resize(400, 300)

        self.retranslateUi(CameraWindow)

        QMetaObject.connectSlotsByName(CameraWindow)
    # setupUi

    def retranslateUi(self, CameraWindow):
        CameraWindow.setWindowTitle(QCoreApplication.translate("CameraWindow", u"Camera Window", None))
    # retranslateUi

