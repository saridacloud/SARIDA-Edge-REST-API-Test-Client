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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QSpinBox, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

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
        self.visualOutputLabel.setLineWidth(3)

        self.verticalLayout_4.addWidget(self.visualOutputLabel)

        self.hSliderDrawRange = QSlider(self.tabVisualOutput)
        self.hSliderDrawRange.setObjectName(u"hSliderDrawRange")
        self.hSliderDrawRange.setValue(99)
        self.hSliderDrawRange.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.hSliderDrawRange)

        self.tabWidget.addTab(self.tabVisualOutput, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit_video_player = QTextEdit(self.tab)
        self.textEdit_video_player.setObjectName(u"textEdit_video_player")

        self.verticalLayout.addWidget(self.textEdit_video_player)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pBtn_playback_play = QPushButton(self.groupBox)
        self.pBtn_playback_play.setObjectName(u"pBtn_playback_play")

        self.horizontalLayout_4.addWidget(self.pBtn_playback_play)

        self.pBtn_playback_pause = QPushButton(self.groupBox)
        self.pBtn_playback_pause.setObjectName(u"pBtn_playback_pause")

        self.horizontalLayout_4.addWidget(self.pBtn_playback_pause)

        self.pBtn_playback_get = QPushButton(self.groupBox)
        self.pBtn_playback_get.setObjectName(u"pBtn_playback_get")

        self.horizontalLayout_4.addWidget(self.pBtn_playback_get)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pBtn_frameno_get = QPushButton(self.groupBox_2)
        self.pBtn_frameno_get.setObjectName(u"pBtn_frameno_get")

        self.horizontalLayout_5.addWidget(self.pBtn_frameno_get)

        self.sBox_frameno = QSpinBox(self.groupBox_2)
        self.sBox_frameno.setObjectName(u"sBox_frameno")
        self.sBox_frameno.setMaximum(10000000)

        self.horizontalLayout_5.addWidget(self.sBox_frameno)

        self.pBtn_frameno_set = QPushButton(self.groupBox_2)
        self.pBtn_frameno_set.setObjectName(u"pBtn_frameno_set")

        self.horizontalLayout_5.addWidget(self.pBtn_frameno_set)


        self.horizontalLayout_3.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab, "")

        self.mainVLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pBtnGetCurrent = QPushButton(MainWidget)
        self.pBtnGetCurrent.setObjectName(u"pBtnGetCurrent")

        self.horizontalLayout.addWidget(self.pBtnGetCurrent)

        self.pBtnGetCurrentDetails = QPushButton(MainWidget)
        self.pBtnGetCurrentDetails.setObjectName(u"pBtnGetCurrentDetails")

        self.horizontalLayout.addWidget(self.pBtnGetCurrentDetails)

        self.pBtnTest_set = QPushButton(MainWidget)
        self.pBtnTest_set.setObjectName(u"pBtnTest_set")

        self.horizontalLayout.addWidget(self.pBtnTest_set)

        self.pBtnTest_get = QPushButton(MainWidget)
        self.pBtnTest_get.setObjectName(u"pBtnTest_get")

        self.horizontalLayout.addWidget(self.pBtnTest_get)


        self.mainVLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.mainVLayout)


        self.retranslateUi(MainWidget)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"MainWidget", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTextOutput), QCoreApplication.translate("MainWidget", u"Text output", None))
        self.visualOutputLabel.setText(QCoreApplication.translate("MainWidget", u"Das ist ein Test!!!!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVisualOutput), QCoreApplication.translate("MainWidget", u"Visual output", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWidget", u"Playback", None))
        self.pBtn_playback_play.setText(QCoreApplication.translate("MainWidget", u"Play", None))
        self.pBtn_playback_pause.setText(QCoreApplication.translate("MainWidget", u"Pause", None))
        self.pBtn_playback_get.setText(QCoreApplication.translate("MainWidget", u"Get Status", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWidget", u"Frame number", None))
        self.pBtn_frameno_get.setText(QCoreApplication.translate("MainWidget", u"Get current frame no", None))
        self.pBtn_frameno_set.setText(QCoreApplication.translate("MainWidget", u"Set current frame no", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWidget", u"Video Player", None))
        self.pBtnGetCurrent.setText(QCoreApplication.translate("MainWidget", u"GET Current", None))
        self.pBtnGetCurrentDetails.setText(QCoreApplication.translate("MainWidget", u"GET Current Details", None))
        self.pBtnTest_set.setText(QCoreApplication.translate("MainWidget", u"Test Button PUT", None))
        self.pBtnTest_get.setText(QCoreApplication.translate("MainWidget", u"Test Button GET", None))
    # retranslateUi

