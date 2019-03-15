#!/usr/bin/python3

import sys
import wrapper
import pandas
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QTextEdit, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore 
from PyQt5 import QtWidgets
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Secrets-Autoposter'
        self.left = 200
        self.top = 200
        self.width = 640
        self.height = 440
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create textbox
        self.textbox = QTextEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(600,300)

        self.textbox1 = QTextEdit(self)
        self.textbox1.move(205,325)
        self.textbox1.resize(230,25)
        #set Text puts the initial text on text editor as parsed from the gsheet. "Say your name friend" and School are
        #titles of the Columns on my spreadsheet that I needed to parse
        self.textbox.setText('#' + cur_hash + str(henum+1) + ": " + data['Say your name friend'].iat[entry] + "\n \n" + data['School'].iat[entry])
        self.textbox1.setText(cur_hash)
 
        # Create a button in the window
        self.button1 = QPushButton('Post Secret', self)
        self.button1.move(20,355)
        self.button1.resize(150,75)

        self.button2 = QPushButton('Move to Archive', self)
        self.button2.move(470,355)
        self.button2.resize(150,75)

        self.button3 = QPushButton('Change Hashtag', self)
        self.button3.move(245,355)
        self.button3.resize(150,75)

        l1 = QtWidgets.QLabel(self)
        l1.setText("#")
        l1.move(195,320)
        # connect button to function on_click
        self.button1.clicked.connect(self.post_anom)
        self.button2.clicked.connect(self.move_to_archive)
        self.button3.clicked.connect(self.change_hashtag)
        self.show()


    # admin edit shortcut
    def keyPressEvent(self, event):
    # Did the user press the Alt key?
        if event.key() == QtCore.Qt.Key_F1: 
        # Yes: do stuffs
            answer = self.textbox.toPlainText()
            answer_piece = answer.rsplit('(', 1)[1]
            answer = answer.rsplit('(', 1)[0]
            answer = answer + "\n" + "[αδμιν εδιτ]:" + "\n\n" + "(" + answer_piece
            self.textbox.setText(answer)

        # No:  Do nothing.
    
    def post_anom(self):
        global entry
        global henum
        answer = self.textbox.toPlainText()
        wrapper.fb_autoposter.post_msg(answer, api)
        print("Posted!")
        wrapper.sheet.mark_uploaded(entry+2, 1, worksheet)
        wrapper.sheet.mark_timestamp(entry+2, worksheet)
        answer = answer.split(None, 1)[1]
        wrapper.sheet.save_posted(entry+2, answer, worksheet)
        wrapper.sheet.write_hashtag(entry+2, cur_hash, worksheet)
        entry += 1
        henum += 1
        self.textbox.setText("")
        try:
            self.textbox.setText('#' + cur_hash + str(henum+1) + ": " + data['Say your name friend'].iat[entry] + "\n \n" + data['School'].iat[entry])
        except(IndexError):
            #happens when gsheet has no data left for the given entry
            self.textbox.setText("Entries over, you can close program")
        
    def move_to_archive(self):
        global entry
        wrapper.sheet.mark_uploaded(entry+2, 0, worksheet)
        wrapper.sheet.mark_timestamp(entry+2, worksheet)
        entry += 1
        print("Moved to archive :(")
        try:
            self.textbox.setText('#' + cur_hash + str(henum+1) + ": " + data['Say your name friend'].iat[entry] + "\n \n" + data['School'].iat[entry])
        except(IndexError):
            self.textbox.setText("Entries over, you can close program")

    def change_hashtag(self):
        cur_hash = self.textbox1.toPlainText()
        print("Setting hashtag to: "+ cur_hash)
        print("New hashtag typed!")
        henum = 0  
        self.textbox.setText('#' + cur_hash + str(henum+1) + ": " + data['Say your name friend'].iat[entry] + "\n \n" + data['School'].iat[entry])
        self.textbox1.setText(cur_hash)  
######################################################################3
         
data, entry, api, worksheet = wrapper.initialize()
if (entry!=0):
    cur_hash = wrapper.sheet.show_hashtag(data, entry)
elif(entry==0):
    cur_hash = input('Input your new hashtag: ')
    print("Since it is the first time you are using the code with the given form, don't forget to post at least one secret!")
try:
    print("Current Hashtag enumeration is: ",data['Hashtag'].value_counts()[cur_hash])
    henum = data['Hashtag'].value_counts()[cur_hash]
except(KeyError):
    print("New hashtag typed!")
    henum = 0                           #current hashtag number
app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
