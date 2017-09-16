#!/usr/bin/env python3

import math
import random
import textwrap
from etchlib.graphicsitem import svg
from PyQt5.QtCore import(
    Qt,
    QRectF,
    QPointF,
    pyqtSignal
)
from PyQt5.QtGui import(
    QFont
)
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QGraphicsObject,
    QGraphicsWidget,
    QGraphicsTextItem,
    QGraphicsLinearLayout,
    QVBoxLayout
    )
class Button(QGraphicsWidget):
    def __init__(self,text="Button",parent=None):
        super(Button,self).__init__(parent)

class Bubble(QGraphicsObject):

    def __init__(self,questions,scale=1.0,parent=None):
        super(Bubble, self).__init__()
        self.bubble = svg.Item(":/images/speech_bubble2.svg",scale,self)
        self.bubble.setPos(QPointF(self.boundingRect().left(),self.boundingRect().top()))
        self.bubble.onLeftClick(self.showAnswer)
        self.bubble.onRightClick(self.resetQuestion)
        self.questions = questions
        self.question = QGraphicsTextItem(self)
        self.answer = QGraphicsTextItem(self)
        #self.display("Arrr!!!<br>On September 19th,<br>we be pirates.<br>Talk Like a Pi-Rate")
        self.displayRandom()
        self.question.setPos(-85,-70)
        self.answer.setPos(-85,-70)
        self.answer.hide()
        #self.button.setToolTip('This is an example button')
        #self.button.move(100,70)

    def showAnswer(self,event):
        self.question.hide()
        self.answer.show()

    def resetQuestion(self,event):
        self.displayRandom()
        self.question.show()
        self.answer.hide()

    def makeHtml(self,value,width=30):

        # Wrap this text.
        wrapper = textwrap.TextWrapper(width=width)
        word_list = wrapper.wrap(text=value)
        # Print each line.
        text = ''
        for element in word_list:
            text += element+'<br>'
        return text

    def display(self,obj,text):
        obj.setHtml('<div style="font-family:Comic Sans MS;display:block;width:200px;word-wrap:break-word;">'+self.makeHtml(text)+'</div>')

    def displayRandom(self):
        q = self.questions[random.randint(0,len(self.questions)-1)]
        self.display(self.answer,q['answer'])
        self.display(self.question,q['question'])

    def boundingRect(self):
        r = self.bubble.boundingRect()
        return QRectF(-r.width()/2,-r.height()/2,r.width()*(self.bubble.scale),r.height()*(self.bubble.scale))

    def movable(self,m=True):
        self.setFlag(QGraphicsObject.ItemIsMovable,m)
        return self

    def paint(self, painter, option, widget):
        pass
        #painter.setBrush(Qt.blue)
        #painter.drawRect(self.boundingRect())
        #painter.drawText(self.boundingRect().bottomRight(),"Hello")
