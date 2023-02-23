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
        self.ui.pBtnTest.clicked.connect(self.on_pBtnTest_clicked)
        self.ui.hSliderDrawRange.valueChanged.connect(self.on_hSliderDrawRange_valueChanged)

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
        # Get polygon from REST call
        call_result = self.api.analysisResultsDetailsCurrentGet()
        self.currentPolygon = self.api.analysisResultsDetailsToQPolygon(
            call_result=call_result
        )
        
        # Arrange slider and draw polygon
        slider_was_on_max = bool(self.ui.hSliderDrawRange.value() == self.ui.hSliderDrawRange.maximum())
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

    def on_pBtnTest_clicked(self):
        from swagger_client.models import Polygon, Point
        
        for j in range(0,4):
            test_polygon = Polygon(point_list=[])
            print(f'round={j} id of test_polygon={id(test_polygon)}')
            print(f'round={j} id of test_polygon._point_list={id(test_polygon._point_list)}')
            if test_polygon.point_list is None:
                test_polygon.point_list = []
                pass
            
            for i in range(0,100):
                test_polygon.point_list.append(Point(i, i))
                
            # self.ui.textOutputEdit.setText(str(test_polygon))
        
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWidget()
    widget.show()

    sys.exit(app.exec())
