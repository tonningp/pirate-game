#!/usr/bin/env python3
import random
from PyQt5.QtCore import *
from PyQt5.QtGui import (QPainter, QColor,
QPen,QIcon,QBrush,QPixmap,QPainterPath,QImage,QFont,QFontMetrics)
from PyQt5.QtWidgets import (
        QWidget,
        QFrame,
        QPushButton,
        QGridLayout,
        QVBoxLayout, 
        QLabel,
        QSizePolicy,
        QMessageBox,
        QLineEdit,
        QFormLayout,
        QGroupBox,
        QRadioButton,
        QButtonGroup,
        QComboBox,
        QSizePolicy,
        QDialog)


class QuestionDialog(QDialog):

    def __init__(self,question=None,parent=None):
        super(QuestionDialog,self).__init__(parent)
        frameStyle = QFrame.Sunken | QFrame.Panel
        self.correct = False
        self.question = question
        self.textLabel = QLabel() 
        self.textLabel.setFrameStyle(frameStyle)
        if question:
            self.textLabel.setText(question['text'])
        layout = QGridLayout()
        layout.setColumnStretch(1,1)
        layout.setColumnMinimumWidth(1,250)
        layout.addWidget(self.textLabel,0,0)
        self.answerBox = QGroupBox("Answers")

        self.vlayout = QVBoxLayout()
        self.bgroup = QButtonGroup(self)
        count = 0
        self.radios = []
        keys = list(question['answers'].keys())
        random.shuffle(keys)
        for answer in keys:
            radio = QRadioButton(question['answers'][answer])
            radio.label = answer
            radio.clicked.connect(self.checkAnswer)
            radio.setChecked(False)
            self.radios.append(radio)
            self.bgroup.addButton(radio)
            self.vlayout.addWidget(radio)
        self.bgroup.buttonClicked.connect(self.checkAnswer)
        self.vlayout.addStretch(1)
        self.answerBox.setLayout(self.vlayout)
        layout.addWidget(self.answerBox,1,0)
        
        self.correctLabel = QLabel()
        self.correctLabel.setText('')
        layout.addWidget(self.correctLabel,3,0)
        self.closeButton = QPushButton('&Close')
        layout.addWidget(self.closeButton,4,1)
        self.closeButton.clicked.connect(self.close)
        self.setLayout(layout)
        self.setWindowTitle("Question")
        self.show()

    def checkAnswer(self,radio):
        if hasattr(radio,'label'):
            if radio.label in self.question['correct']:
                self.correctLabel.setText(self.question['feedback'][radio.label])
                self.correct = True
                self.correctlabel = radio.label
            else:
                self.correctLabel.setText('Sorry, that is not correct')
                self.correct = False

    def reset(self):
        self.correct = False
        for radio in self.radios:
            radio.setAutoExclusive(False)
            radio.setChecked(False)
            radio.setAutoExclusive(True)
            radio.setCheckable(False)
            radio.update()
            radio.setCheckable(True)
            self.vlayout.removeWidget(radio)
        random.shuffle(self.radios)
        for radio in self.radios:
            self.vlayout.addWidget(radio)
        self.correctLabel.setText('')


