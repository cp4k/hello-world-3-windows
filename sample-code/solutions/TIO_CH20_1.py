# TIO_CH20-1.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# Answer to Try It Out, Question 1, Chapter 20

# Number guess program using PyQt

import sys
from PyQt5 import QtWidgets, uic
import random

form_class = uic.loadUiType("TIO_CH20_1.ui")[0]    # Load the Number Guess UI  

guess = 0
secret = random.randint(1, 100)
tries = 6

class NumberGuess(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btnGuess.clicked.connect(self.btnGuess_clicked)       # Bind the button event handler
        self.actionExit.triggered.connect(self.menuExit_selected)  # Bind Exit menu item event handler
        self.spinBox1.valueChanged.connect(self.spinBox1_valueChanged) # Bind the spinBox event handler
        self.lblMessage.setText("")
        self.lblStatus.setText("You have " + str(tries) + " guesses left.")

    def btnGuess_clicked(self, event):
        global done, guess, tries
        guess = self.spinBox1.value()       # get the player's guess
        if guess != secret and tries > 1:
            if guess < secret:
                self.lblMessage.setText("Too low, ye scurvy dog!")
            elif guess > secret:
                self.lblMessage.setText("Too high, landlubber!")
            tries = tries - 1                         # used up one try    
            self.lblStatus.setText("You have " + str(tries) + " guesses left.")
                
        elif guess == secret:   #Player guessed it
            self.lblMessage.setText("Avast! Ye got it!  Found my secret, ye did!")
            self.lblStatus.setText("")
        else:                  #Player ran out of guesses
            self.lblMessage.setText("No more guesses!  Better luck next time, matey!")
            self.lblStatus.setText("The secret number was " + str(secret))

    def spinBox1_valueChanged(self):               # spinBox changed event handler
        self.lblMessage.setText("")                # clear the Message text
            
    def menuExit_selected(self):               # Flie-Exit Menu event handler
        self.close()                           # 

app = QtWidgets.QApplication(sys.argv)
myWindow = NumberGuess(None)
myWindow.show()
app.exec_() 
    
