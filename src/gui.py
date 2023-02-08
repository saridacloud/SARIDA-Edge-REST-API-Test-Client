#!/usr/bin/env python3

import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QPolygon
from PySide6.QtCore import Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWidget
from api_client import SaridaEdgeApiWrapper
import appsettings


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)
        self.config = appsettings.loadConfig()
        self.api = SaridaEdgeApiWrapper()
        self.api.setConfig(self.config)

        # Connect ui signals
        self.ui.pBtnGetCurrent.clicked.connect(self.on_pBtnGetCurrent_clicked)
        self.ui.pBtnGetCurrentDetails.clicked.connect(
            self.on_pBtnGetCurrentDetails_clicked
        )
        self.ui.pBtnTest.clicked.connect(self.on_pBtnTest_clicked)

        # Init canvas
        self.setCanvasSize(500, 500)

    def setCanvasSize(self, width: int, height: int):
        canvas = QtGui.QPixmap(QtCore.QSize(width, height))
        canvas.fill(Qt.white)
        self.ui.visualOutputLabel.setPixmap(canvas)
        
    def clearCanvas(self):
        canvas = self.ui.visualOutputLabel.pixmap()
        canvas.fill(Qt.white)
        self.ui.visualOutputLabel.setPixmap(canvas)

    def drawPolygon(self, polygon: QPolygon):
        self.clearCanvas()
        canvas = self.ui.visualOutputLabel.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawPolygon(polygon)
        painter.end()
        self.ui.visualOutputLabel.setPixmap(canvas)

    def on_pBtnGetCurrent_clicked(self):
        result = self.api.analysisResultsCurrentGet()
        self.ui.textOutputEdit.setText(str(result))

    def on_pBtnGetCurrentDetails_clicked(self):
        call_result = self.api.analysisResultsDetailsCurrentGet()
        polygon = self.api.analysisResultsDetailsToQPolygon(
            call_result=call_result
        )
        self.drawPolygon(polygon)

    def on_pBtnTest_clicked(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWidget()
    widget.show()

    sys.exit(app.exec())
