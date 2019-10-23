# Listing_22-8_the_whole_hangmanpy_program.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import sys
from PyQt5 import QtWidgets, uic
import random

form_class = uic.loadUiType("hangman.ui")[0]

# Finds letters
def find_letters(letter, a_string):
    locations = []
    start = 0
    while a_string.find(letter, start, len(a_string)) != -1:
        location = a_string.find(letter, start, len(a_string))
        locations.append(location)
        start = location + 1
    return locations

# Replaces dashes with letters when the player guesses a letter correctly
def replace_letters(string, locations, letter):
    new_string = ''
    for i in range (0, len(string)):
        if i in locations:
            new_string = new_string + letter
        else:
            new_string = new_string + string[i]
    return new_string

def dashes(word):
    # Replaces letters with dashes at the start of the program
    letters = "abcdefghijklmnopqrstuvwxyz"
    new_string = ''
    for i in word:
        if i in letters:
            new_string += "-"
        else:
            new_string += i
    return new_string

class HangmanGame(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # Connect event handlers
        self.btn_guess.clicked.connect(self.btn_guess_clicked)
        self.actionExit.triggered.connect(self.menuExit_selected)
        # Parts of the man
        self.pieces = [self.head, self.body, self.leftarm, self.leftleg,
                       self.rightarm, self.rightleg]

        self.gallows = [self.line1, self.line2, self.line3, self.line4]  # Parts of the gallows
        self.pieces_shown = 0
        self.currentword = ""
        # Gets word list
        f=open("words.txt", 'r')
        self.lines = f.readlines()
        f.close()
        self.new_game()

    def new_game(self):
        self.guesses.setText("")
        self.currentword = random.choice(self.lines)  # Randomly pick a word from the list
        self.currentword = self.currentword.strip()
        # Hides the man
        for i in self.pieces:
            i.setFrameShadow(QtWidgets.QFrame.Plain)
            i.setHidden(True)
        for i in self.gallows:
            i.setFrameShadow(QtWidgets.QFrame.Plain)
        self.word.setText(dashes(self.currentword))  # Calls the function to replace letters with dashes
        self.pieces_shown = 0

    def btn_guess_clicked(self):
        # Lets the player guess a letter or word
        guess = str(self.guessBox.text())
        if str(self.guesses.text()) != "":
            self.guesses.setText(str(self.guesses.text())+", "+guess)
        else:
            self.guesses.setText(guess)
        # Guess a letter
        if len(guess) == 1:
            if guess in self.currentword:
                locations = find_letters(guess, self.currentword)
                self.word.setText(replace_letters(str(self.word.text()),
                                                  locations,guess))
                if str(self.word.text()) == self.currentword:
                    self.win()
            else:
                self.wrong()
        # Guess a word
        else:
            if guess == self.currentword:
                self.win()
            else:
                self.wrong()
        self.guessBox.setText("")

    # Display a dialog if player wins
    def win(self):
        QtWidgets.QMessageBox.information(self,"Hangman","You win!")
        self.new_game()

    def wrong(self):
        # Wrong guess
        self.pieces_shown += 1
        # Reveal another piece of the man
        for i in range(self.pieces_shown):
            self.pieces[i].setHidden(False)
        if self.pieces_shown == len(self.pieces):
            # Player lost
            message = "You lose.  The word was " + self.currentword
            QtWidgets.QMessageBox.warning(self,"Hangman", message)
            self.new_game()
    def menuExit_selected(self):
        self.close()

app = QtWidgets.QApplication(sys.argv)
myapp = HangmanGame(None)
myapp.show()
app.exec_()
