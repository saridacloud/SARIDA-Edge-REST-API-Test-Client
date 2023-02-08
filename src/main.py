#!/usr/bin/env python3
import sys
from PySide6 import QtWidgets
from gui import MainWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWidget()
    widget.show()

    sys.exit(app.exec())


# # Prints PySide6 version
# print(PySide6.__version__)

# # Prints the Qt version used to compile PySide6
# print(PySide6.QtCore.__version__)