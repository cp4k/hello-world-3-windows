# Listing_20-2_adding_an_event_handler_for_the_button_from_listing_201.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import sys
from PyQt5 import QtWidgets, uic

form_class = uic.loadUiType("MyFirstGui.ui")[0]

class MyFirstWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)         ❶ ❷
                                                                     ❷
    def button_clicked(self):                                        ❷
        x = self.pushButton.x()                                      ❷ ❸
        y = self.pushButton.y()                                      ❷ ❸
        x += 50                                                      ❷ ❸
        y += 50                                                      ❷ ❸
        self.pushButton.move(x, y)                                   ❸ ❹

app = QtWidgets.QApplication(sys.argv)
myWindow = MyFirstWindow()
myWindow.show()
app.exec_()
