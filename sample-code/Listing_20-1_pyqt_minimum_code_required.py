# Listing_20-1_pyqt_minimum_code_required.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import sys
from PyQt5 import QtWidgets, uic  # Imports needed PyQt libraries

form_class = uic.loadUiType("MyFirstGui.ui")[0]  # Loads the UI we created in Designer ``❶``

# Defines a class for the main window
class MyFirstWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)  # PyQt object that runs the event loop
myWindow = MyFirstWindow()  # Makes an instance of the window class
# Starts the program and displays the GUI window
myWindow.show()
app.exec_()
