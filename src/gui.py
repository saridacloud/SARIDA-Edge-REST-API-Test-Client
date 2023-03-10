#!/usr/bin/env python3

import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QPolygon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox

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
        self.currentPolygon = QPolygon()

        # Init GUI
        self.ui.setupUi(self)
        self.config = appsettings.loadConfig()
        self.api = SaridaEdgeApiWrapper()
        self.api.setConfig(self.config)

        # Connect ui signals
        self.ui.pBtnGetCurrent.clicked.connect(self.on_pBtnGetCurrent_clicked)
        self.ui.pBtnGetCurrentDetails.clicked.connect(
            self.on_pBtnGetCurrentDetails_clicked
        )
        self.ui.pBtnTest_set.clicked.connect(self.on_pBtnTest_PUT_clicked)
        self.ui.pBtnTest_get.clicked.connect(self.on_pBtnTest_GET_clicked)
        self.ui.hSliderDrawRange.valueChanged.connect(
            self.on_hSliderDrawRange_valueChanged
        )
        # Connect ui signals / video player
        self.ui.pBtn_playback_play.clicked.connect(self.on_pBtn_playback_play_clicked)
        self.ui.pBtn_playback_pause.clicked.connect(self.on_pBtn_playback_pause_clicked)
        self.ui.pBtn_playback_get.clicked.connect(self.on_pBtn_playback_get_clicked)
        self.ui.pBtn_frameno_get.clicked.connect(self.on_pBtn_frameno_get_clicked)
        self.ui.pBtn_frameno_set.clicked.connect(self.on_pBtn_frameno_set_clicked)

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

    def drawPolygon(self, polygon: QPolygon, max_len: int):
        polygon_to_draw = polygon.first(max_len)
        self.clearCanvas()
        canvas = self.ui.visualOutputLabel.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawPolyline(polygon_to_draw)
        # painter.drawPolygon(polygon_to_draw)
        painter.end()
        self.ui.visualOutputLabel.setPixmap(canvas)

    def setCurrentPolygonFromApi(self) -> QPolygon:
        # Get canvas size
        canvas_size = self.api.analysisVideoResolutionGet()
        if not canvas_size:
            QMessageBox.critical(
                self, "API Error", "Failed to call /analysis/video/resolution"
            )
            return
        self.setCanvasSize(width=canvas_size.width, height=canvas_size.height)

        # Get polygon from REST call
        call_result = self.api.analysisResultsDetailsCurrentGet()
        if not call_result:
            QMessageBox.critical(
                self, "API Error", "Failed to call /analysis/results/details/current"
            )
            return
        self.currentPolygon = self.api.analysisResultsDetailsToQPolygon(
            call_result=call_result
        )

        # Arrange slider and draw polygon
        slider_was_on_max = bool(
            self.ui.hSliderDrawRange.value() == self.ui.hSliderDrawRange.maximum()
        )
        self.ui.hSliderDrawRange.setMaximum(len(self.currentPolygon))
        if slider_was_on_max:
            self.ui.hSliderDrawRange.setValue(self.ui.hSliderDrawRange.maximum())
        else:
            self.drawPolygon(self.currentPolygon, self.ui.hSliderDrawRange.value())

        # Text output
        self.ui.textOutputEdit.setText(str(self.currentPolygon))

    def on_pBtnGetCurrent_clicked(self):
        result = self.api.analysisResultsCurrentGet()
        self.ui.textOutputEdit.setText(str(result))

    def on_pBtnGetCurrentDetails_clicked(self):
        self.setCurrentPolygonFromApi()

    def on_hSliderDrawRange_valueChanged(self, value: int):
        if not self.currentPolygon or len(self.currentPolygon) < 1:
            return
        self.drawPolygon(self.currentPolygon, value)

    def on_pBtn_playback_play_clicked(self):
        self.api.videoPlayerRunning = True

    def on_pBtn_playback_pause_clicked(self):
        self.api.videoPlayerRunning = False

    def on_pBtn_playback_get_clicked(self):
        value = self.api.videoPlayerRunning
        self.ui.textEdit_video_player.setPlainText(str(value))

    def on_pBtn_frameno_get_clicked(self):
        value = self.api.videoPlayerCurrentFrame
        self.ui.sBox_frameno.setValue(value)

    def on_pBtn_frameno_set_clicked(self):
        value = self.ui.sBox_frameno.value()
        self.api.videoPlayerCurrentFrame = value

    def on_pBtnTest_PUT_clicked(self):
        self.api.testCallSetCameraState()
    
    def on_pBtnTest_GET_clicked(self):
        camera_state = self.api.testCallGetCameraState()
        self.ui.textEdit_video_player.setPlainText(camera_state)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWidget()
    widget.show()

    sys.exit(app.exec())
