# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSlider, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(800, 600)
        self.horizontalLayout_2 = QHBoxLayout(MainWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mainVLayout = QVBoxLayout()
        self.mainVLayout.setObjectName(u"mainVLayout")
        self.tabWidget = QTabWidget(MainWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabTextOutput = QWidget()
        self.tabTextOutput.setObjectName(u"tabTextOutput")
        self.verticalLayout_3 = QVBoxLayout(self.tabTextOutput)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textOutputEdit = QTextEdit(self.tabTextOutput)
        self.textOutputEdit.setObjectName(u"textOutputEdit")

        self.verticalLayout_3.addWidget(self.textOutputEdit)

        self.tabWidget.addTab(self.tabTextOutput, "")
        self.tabVisualOutput = QWidget()
        self.tabVisualOutput.setObjectName(u"tabVisualOutput")
        self.verticalLayout_4 = QVBoxLayout(self.tabVisualOutput)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.visualOutputLabel = QLabel(self.tabVisualOutput)
        self.visualOutputLabel.setObjectName(u"visualOutputLabel")
        self.visualOutputLabel.setFrameShape(QFrame.Box)

        self.verticalLayout_4.addWidget(self.visualOutputLabel)

        self.hSliderDrawRange = QSlider(self.tabVisualOutput)
        self.hSliderDrawRange.setObjectName(u"hSliderDrawRange")
        self.hSliderDrawRange.setValue(99)
        self.hSliderDrawRange.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.hSliderDrawRange)

        self.tabWidget.addTab(self.tabVisualOutput, "")

        self.mainVLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pBtnGetCurrent = QPushButton(MainWidget)
        self.pBtnGetCurrent.setObjectName(u"pBtnGetCurrent")

        self.horizontalLayout.addWidget(self.pBtnGetCurrent)

        self.pBtnGetCurrentDetails = QPushButton(MainWidget)
        self.pBtnGetCurrentDetails.setObjectName(u"pBtnGetCurrentDetails")

        self.horizontalLayout.addWidget(self.pBtnGetCurrentDetails)

        self.pBtnTest = QPushButton(MainWidget)
        self.pBtnTest.setObjectName(u"pBtnTest")

        self.horizontalLayout.addWidget(self.pBtnTest)


        self.mainVLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.mainVLayout)


        self.retranslateUi(MainWidget)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"MainWidget", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTextOutput), QCoreApplication.translate("MainWidget", u"Text output", None))
        self.visualOutputLabel.setText(QCoreApplication.translate("MainWidget", u"Das ist ein Test!!!!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVisualOutput), QCoreApplication.translate("MainWidget", u"Visual output", None))
        self.pBtnGetCurrent.setText(QCoreApplication.translate("MainWidget", u"GET Current", None))
        self.pBtnGetCurrentDetails.setText(QCoreApplication.translate("MainWidget", u"GET Current Details", None))
        self.pBtnTest.setText(QCoreApplication.translate("MainWidget", u"Test 2", None))
    # retranslateUi

