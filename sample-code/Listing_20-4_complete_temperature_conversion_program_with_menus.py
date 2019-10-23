# Listing_20-4_complete_temperature_conversion_program_with_menus.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import sys
from PyQt5 import QtWidgets, uic

form_class = uic.loadUiType("tempconv_menu.ui")[0]  # Loads the UI file that includes the menus

class TemperatureConverterWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # Connects Convert menu item event handlers
        self.btnCtoF.clicked.connect(self.btnCtoF_clicked)
        self.btnFtoC.clicked.connect(self.btnFtoC_clicked)
        self.actionC_to_F.triggered.connect(self.btnCtoF_clicked)
        self.actionF_to_C.triggered.connect(self.btnFtoC_clicked)
        self.actionExit.triggered.connect(self.menuExit_selected)  # Connects Exit menu item event handler

    def btnCtoF_clicked(self):
        cel = float(self.editCel.text())
        fahr = cel * 9 / 5 + 32
        self.spinFahr.setValue(int(fahr + 0.5))

    def btnFtoC_clicked(self):
        fahr = self.spinFahr.value()
        cel = (fahr - 32) * 5 / 9
        self.editCel.setText(str(cel))

    # The new Exit menu item event handler
    def menuExit_selected(self):
        self.close()

app = QtWidgets.QApplication(sys.argv)
myWindow = TemperatureConverterWindow(None)
myWindow.show()
app.exec_()
