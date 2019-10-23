# Listing_24-4_virtualpetpy.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import sys, pickle,datetime
from PyQt5 import QtCore, QtGui, QtWidgets, uic

formclass = uic.loadUiType("virtualpet.ui")[0]

class VirtualPetWindow(QtWidgets.QMainWindow, formclass):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.doctor = False
        # Initializes values
        self.walking = False
        self.sleeping = False
        self.playing = False
        self.eating = False
        self.time_cycle = 0
        self.hunger = 0
        self.happiness  = 8
        self.health = 8
        self.forceAwake = False
        # Lists images for animations
        self.sleepImages = ["sleep1.gif","sleep2.gif","sleep3.gif",
                            "sleep4.gif"]
        self.eatImages = ["eat1.gif", "eat2.gif"]
        self.walkImages = ["walk1.gif", "walk2.gif", "walk3.gif",
                           "walk4.gif"]
        self.playImages = ["play1.gif", "play2.gif"]
        self.doctorImages = ["doc1.gif", "doc2.gif"]
        self.nothingImages  = ["pet1.gif", "pet2.gif", "pet3.gif"]

        self.imageList = self.nothingImages
        self.imageIndex = 0

        # Connects event handlers for toolbar buttons
        self.actionStop.triggered.connect(self.stop_Click)
        self.actionFeed.triggered.connect(self.feed_Click)
        self.actionWalk.triggered.connect(self.walk_Click)
        self.actionPlay.triggered.connect(self.play_Click)
        self.actionDoctor.triggered.connect(self.doctor_Click)

        # Sets up timers
        self.myTimer1 = QtCore.QTimer(self)
        self.myTimer1.start(500)
        self.myTimer1.timeout.connect(self.animation_timer)
        self.myTimer2 = QtCore.QTimer(self)
        self.myTimer2.start(5000)
        self.myTimer2.timeout.connect(self.tick_timer)

        filehandle = True
        # Tries to open pickle file
        try:
            file = open("savedata_vp.pkl", "rb")
        except:
            filehandle = False
        if filehandle:
            save_list = pickle.load(file)  # Reads from pickle file if open
            file.close()
        else:
            save_list = [8, 8, 0, datetime.datetime.now(), 0]  # Uses default values if pickle file not open
        # Pulls individual values out of list
        self.happiness = save_list[0]
        self.health    = save_list[1]
        self.hunger    = save_list[2]
        timestamp_then = save_list[3]
        self.time_cycle = save_list[4]

        # Checks how long since last run
        difference = datetime.datetime.now() - timestamp_then
        ticks = int(difference.seconds / 50)
        for i in range(0, ticks):
            # Simulates all ticks that happened during down time
            self.time_cycle += 1
            if self.time_cycle == 60:
                self.time_cycle = 0
            if self.time_cycle <= 48:  # Awake
                self.sleeping = False
                if self.hunger < 8:
                    self.hunger += 1
            else:  # Sleeping
                self.sleeping = True
                if self.hunger < 8 and self.time_cycle % 3 == 0:
                    self.hunger += 1
            if self.hunger == 7 and (self.time_cycle % 2 ==0) \
                                and self.health > 0:
                self.health -= 1
            if self.hunger == 8 and self.health > 0:
                self.health -=1
        # Uses correct animation—awake or sleeping
        if self.sleeping:
            self.imageList = self.sleepImages
        else:
            self.imageList = self.nothingImages

    def sleep_test(self):
        # Checks if pet is sleeping before doing an action
        if self.sleeping:
            result = (QtWidgets.QMessageBox.warning(self, 'WARNING',  # Type of dialog
"Are you sure you want to wake your pet up?  He'll be unhappy about it!",
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,  # Buttons to show
                    QtWidgets.QMessageBox.No))  # Default button

            if result == QtWidgets.QMessageBox.Yes:
                self.sleeping = False
                self.happiness -= 4
                self.forceAwake = True
                return True
            else:
                return False
        else:
            return True

    # The doctor button event handler
    def doctor_Click(self):
        if self.sleep_test():
            self.imageList = self.doctorImages
            self.doctor = True
            self.walking = False
            self.eating = False
            self.playing = False

    # The feed button event handler
    def feed_Click(self):
        if self.sleep_test():
            self.imageList = self.eatImages
            self.eating = True
            self.walking = False
            self.playing = False
            self.doctor = False

    # The play button event handler
    def play_Click(self):
        if self.sleep_test():
            self.imageList = self.playImages
            self.playing = True
            self.walking = False
            self.eating = False
            self.doctor = False

    # The walk button event handler
    def walk_Click(self):
        if self.sleep_test():
            self.imageList = self.walkImages
            self.walking = True
            self.eating = False
            self.playing = False
            self.doctor = False

    # The stop button event handler
    def stop_Click(self):
        if not self.sleeping:
            self.imageList = self.nothingImages
            self.walking = False
            self.eating = False
            self.playing = False
            self.doctor = False

    def animation_timer(self):
        # The animation timer (every 0.5 sec) event handler
        if self.sleeping and not self.forceAwake:
            self.imageList = self.sleepImages
        self.imageIndex += 1
        if self.imageIndex >= len(self.imageList):
            self.imageIndex = 0
        icon = QtGui.QIcon()
        # Updates pet’s image (animation)
        current_image = self.imageList[self.imageIndex]
        icon.addPixmap(QtGui.QPixmap(current_image),
                       QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.petPic.setIcon(icon)
        self.progressBar_1.setProperty("value", (8-self.hunger)*(100/8.0))
        self.progressBar_2.setProperty("value", self.happiness*(100/8.0))
        self.progressBar_3.setProperty("value", self.health*(100/8.0))

    def tick_timer(self):  # Start of main 5 sec timer event handler
        # Checks if sleeping or awake
        self.time_cycle += 1
        if self.time_cycle == 60:
            self.time_cycle = 0
        if self.time_cycle <= 48 or self.forceAwake:
            self.sleeping = False
        else:
            self.sleeping = True
        if self.time_cycle == 0:
            self.forceAwake = False

        if self.doctor:
            # Adds or subtracts units depending on activity
            self.health += 1
            self.hunger += 1
        elif self.walking and (self.time_cycle % 2 == 0):
            self.happiness += 1
            self.health += 1
            self.hunger += 1
        elif self.playing:
            self.happiness += 1
            self.hunger += 1
        elif self.eating:
            self.hunger -= 2
        elif self.sleeping:
            if self.time_cycle % 3 == 0:
                self.hunger += 1
        else:
            self.hunger += 1
            if self.time_cycle % 2 == 0:
                self.happiness -= 1
        # Makes sure values are not out of range
        if self.hunger > 8:  self.hunger = 8
        if self.hunger < 0:  self.hunger = 0
        if self.hunger == 7 and (self.time_cycle % 2 ==0) :
            self.health -= 1
        if self.hunger == 8:
            self.health -=1
        if self.health > 8:  self.health = 8
        if self.health < 0:  self.health = 0
        if self.happiness > 8:  self.happiness = 8
        if self.happiness < 0:  self.happiness = 0
        # Updates progress bars
        self.progressBar_1.setProperty("value", (8-self.hunger)*(100/8.0))
        self.progressBar_2.setProperty("value", self.happiness*(100/8.0))
        self.progressBar_3.setProperty("value", self.health*(100/8.0))

    def closeEvent(self, event):
        # Saves status and timestamp to pickle file
        file = open("savedata_vp.pkl", "wb")  # Line-continuation character
        save_list = [self.happiness, self.health, self.hunger, \
                     datetime.datetime.now(), self.time_cycle]
        pickle.dump(save_list, file)
        event.accept()

    def menuExit_selected(self):
        self.close()

app = QtWidgets.QApplication(sys.argv)
myapp = VirtualPetWindow()
myapp.show()
app.exec_()
