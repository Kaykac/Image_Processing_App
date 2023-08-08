"""
This code is the driver code for the created image processing application to run.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from LabV2 import Ui_MainWindow
from Image import Image 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Image(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
