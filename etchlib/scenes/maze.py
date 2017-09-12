#!/usr/bin/env python3
from threading import Thread
import paho.mqtt.client as mqtt
import time,os,sys,struct
import random
import math
import pigpio
import http.client
import sip
import data

from etchlib.widgets.editor import Widget as EditorWidget
from etchlib.dialogs import QuestionDialog
from etchlib.graphicsitem.maze import Item as Maze
from etchlib.graphicsitem.cheese import Item as Cheese
from etchlib.graphicsitem.mouse import Item as Mouse

from PyQt5.QtCore import *
from PyQt5.QtGui import (
    QPainter, 
    QColor, 
    QPen,
    QIcon,
    QBrush,
    QPixmap,
    QPainterPath,
    QImage,
    QFont,
    QFontMetrics
)
from PyQt5.QtWidgets import (
    QWidget,
    QFrame,
    QMainWindow,
    QLCDNumber, 
    QSlider,
    QPushButton,
    QGridLayout,
    QVBoxLayout, 
    QLabel,
    QSizePolicy,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsTextItem,
    QGraphicsItem,
    QGraphicsObject,
    QGraphicsPixmapItem,
    QGraphicsProxyWidget,
    QMessageBox,
    QLineEdit,
    QFormLayout,
    QGroupBox,
    QRadioButton,
    QButtonGroup,
    QComboBox,
    QSizePolicy,
    QDialog
)

from PyQt5.QtSvg import QGraphicsSvgItem,QSvgRenderer


def getPin(pin):
    pi = pigpio.pi()
    pi.set_mode(pin,pigpio.INPUT) 
    pi.set_pull_up_down(pin,pigpio.PUD_UP)
    return pi

GPIOS = [18,23,24,25] 
pinDefs = [getPin(pin) for pin in GPIOS]

buttonStart = False


#Todo -- get the mqtt service working
#broker_address = "172.17.1.21"
#mqttClient = mqtt.Client("P1")
#try:
#    mqttClient.connect(broker_address)
#    mqttClient.publish("topic/state","Hey from RPI")
#except ConnectionRefusedError:
#    print('Cannot connect to the mqtt server')

def buttonPressed(button):
   global buttonStart
   if not pinDefs[button].read(GPIOS[button]):
       buttonStart = True
    # since we are using pull up resistor, logic goes to 0 when button is
    # pressed
   return not pinDefs[button].read(GPIOS[button])



class Scene(QGraphicsScene):

    SCALE = 4.0
    offset = 2

    display_template = '<strong style="color:{2};font-size:{1}px;">{0}</strong>'

    questions = [
            {
            'text' : 'The raspberry pi 3 is which of the following:',
            'answers' : {
                'a1':'a single board computer',
                'a2':'a desktop computer',
                'a3':'a mainframe computer',
                'a4':'a super computer'
              },
              'correct' : ['a1'],
'feedback' : 
{'a1': 'That is correct, The raspberry pi is a single board computer (SBC).'
}
             },
            {
            'text' : 'This computer game is written using which language :',
            'answers' : {
                'a1':'English',
                'a2':'Python',
                'a3':'Java',
                'a4':'C++'
              },
              'correct' : ['a2'],
'feedback' : 
{'a2': 'That is correct, this game was written using the Python programming\
 language.'
}
             },
            {
            'text' : 
            'The amount of memory on the guidance computer used on the lunar \
module was around:',
            'answers' : {
                'a1':'2 Gigabytes',
                'a2':'1 Megabyte',
                'a3':'640 Kilobytes',
                'a4':'4 Kilobytes'
              },
              'correct' : ['a4'],
'feedback' : 
{'a4': 'That is correct, the Apollo Guidance Computer had less than 4 kilobytes \
of memory. '
}
             },
            {
            'text' : 
            'Do you want to become a computer programmer?',
            'answers' : {
                'a1':'Yes',
                'a2':'No'
              },
              'correct' : ['a1','a2'],
'feedback' : 
{'a1': 'That is great, pay attention in your math and science classes',
 'a2' : 'You will do well whatever you decide to do.'
}
             }
    ]
    def initUI(self):
        w = QWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)

        w.setAttribute(Qt.WA_NoSystemBackground, True)
        w.setAttribute(Qt.WA_TranslucentBackground, True)
        layout = QFormLayout()
        self.m_nameEdit = QLineEdit()
        layout.addRow(QLabel("Your Name:"), self.m_nameEdit)
        self.namewidget = QGraphicsProxyWidget()
        self.school = QComboBox()
        for school in data.schools:
            self.school.addItem(school)

        layout.addRow(QLabel("Your School:"), self.school)
        w.setLayout(layout)
        self.namewidget.setWidget(w)
        self.addItem(self.namewidget)
        self.namewidget.setPos(-630,-440)
    
    @pyqtSlot()
    def showEditor(self):
        self.editor.show();

    @pyqtSlot()
    def hideEditor(self):
        self.editor.hide();

    def initCheeseList(self):
        self.cheesePositions = [
                QPoint(-230,165),
                QPoint(-100,-30),
                QPoint(156,-220),
                QPoint(0,-400)
                
                ]
        self.cheeseList = [
                Cheese(self.currentView,self.questions[x],self.cheesePositions[x]) for x in range(4) ]
        self.cheeseList[len(self.cheeseList)-1].final = True

    def __init__(self,currentView=None):
        super(Scene,self).__init__()
        self.currentView = currentView
        self.mouseUpdates = [
                { 'rotation' : 0, 'offset' : QPoint(0,-1*self.offset)}, #up
                { 'rotation' : 180, 'offset' : QPoint(0,self.offset)}, #down
                { 'rotation' : -90, 'offset' : QPoint(-1*self.offset,0)}, #left
                { 'rotation' : 90, 'offset' : QPoint(self.offset,0)} #right
        ]
        self.initUI()
        self.initCheeseList()
        self.mouse = Mouse()
        self.mouse.move(QPoint(0,400))
        self.mouse.showBoundingRect = False
        self.addItem(self.mouse)
        self.mouse.setZValue(100)
        for cheese in self.cheeseList:
            self.mouse.moved.connect(cheese.checkCollision)
            self.addItem(cheese)
        self.maze = Maze(':/images/10x10maze.v1.svg',self.SCALE)
        br = self.maze.boundingRect()
        self.maze.setPos(-300,-300)
        self.addItem(self.maze);
        self.cheese = self.cheeseList[3]
        self.setSceneRect(-300, -300, 600, 600)
        self.setItemIndexMethod(QGraphicsScene.NoIndex)
        self.timer = QTimer()
        self.timer.timeout.connect(self.readButtons)
        self.timer.start(10)
        self.gametimer = QTimer()
        self.gametimer.timeout.connect(self.updateGameTime)
        self.mazeimage = QImage(br.width()*self.SCALE,br.height()*self.SCALE,QImage.Format_ARGB32)
        painter = QPainter(self.mazeimage)
        self.maze.renderer.render(painter)
        self.mouse.mazeEntered = False
        self.winner = QGraphicsTextItem()
        self.winner.setHtml(self.display_template.format('You Won!',72,'blue'))
        self.winner.setZValue(100)
        self.gotcheese = QGraphicsTextItem()
        self.gotcheese.setHtml('<div style="background-color:white;">'+self.display_template.format('You got the cheese, but did you really \
win?',48,'blue')+'</div>')
        self.addItem(self.winner)
        self.addItem(self.gotcheese)
        self.winner.setPos(-300,0)
        #self.winner.setPos(-300,-485)
        self.gotcheese.setPos(-400,0)
        self.gotcheese.setZValue(100)
        self.gametimertext = QGraphicsTextItem()
        self.gametimertext.setHtml(self.display_template.format(0,48,'blue'))
        self.addItem(self.gametimertext)
        self.gametimertext.setPos(350,-400)
        self.gametimerCount = 0

        self.winner.hide()
        self.gotcheese.hide()

        button = QPushButton("Reset")
        self.reset = QGraphicsProxyWidget()
        self.reset.setWidget(button)
        self.addItem(self.reset)
        self.reset.setPos(-300,-330)
        button.clicked.connect(self.on_reset_click)
        self.editor = EditorWidget()
        self.addItem(self.editor)
        self.editor.hide()
        self.editor.setPos(-300,-330)
        

    
    @pyqtSlot()
    def on_reset_click(self):
        global buttonStart
        self.mouse.mazeEntered = False
        self.mouse.move(QPoint(0,400))
        self.mouse.resetColor()
        self.mouse.update()
        self.winner.hide()
        self.gotcheese.hide()
        buttonStart = False
        self.mouse.mazeEntered = False
        self.gametimer.stop()
        self.gametimertext.setHtml(self.display_template.format(0,48,'blue'))
        self.gametimerCount = 0
        self.m_nameEdit.setText('')
        for p in range(4):
            self.cheeseList[p].setPos(self.cheesePositions[p])
            self.cheeseList[p].show()

    def updateGameTime(self):
        self.gametimerCount += 1
        self.gametimertext.setHtml(self.display_template.format(self.gametimerCount,48,'blue'))

    def keyPressEvent(self,e):
        global buttonStart
        offset = 10;
        mouseUpdates = [
                { 'rotation' : 0, 'offset' : QPoint(0,-1*offset)}, #up
                { 'rotation' : 180, 'offset' : QPoint(0,offset)}, #down
                { 'rotation' : -90, 'offset' : QPoint(-1*offset,0)}, #left
                { 'rotation' : 90, 'offset' : QPoint(offset,0)} #right
        ]
        keys = \
        [   
            #Qt.Key_K,Qt.Key_J,Qt.Key_H,Qt.Key_L,
            #Qt.Key_Up,Qt.Key_Down,Qt.Key_Left,Qt.Key_Right,
            #Qt.Key_W,Qt.Key_S,Qt.Key_A,Qt.Key_D
            Qt.Key_Up,Qt.Key_Down,Qt.Key_Left,Qt.Key_Right
        ]
        index = 0
        for key in keys:
            if key == e.key(): 
                buttonStart = True
                self.updateMousePosition(mouseUpdates[index%4]['rotation'],mouseUpdates[index%4]['offset'])
                break
            index += 1
        return super(Scene,self).keyPressEvent(e)

    def updateMousePosition(self,rot,offset):
            global buttonStart
            if not self.mouse.mazeEntered and \
                self.mouse.collidesWith(self.maze):
                self.mouse.mazeEntered = True            
            self.mouse.setRotation(rot);
            newPos = self.mouse.pos() + offset
            if self.collidingItems(self.mouse):
                if not self.mouse.hitsWall(self):
                    self.mouse.move(newPos)
            else:
                self.mouse.move(newPos)
            if not self.mouse.mazeEntered and self.mouse.collidesWith(self.cheese):
                self.gotcheese.show()
                self.gametimer.stop()
                buttonStart = False
            elif self.mouse.mazeEntered and \
            self.mouse.collidesWith(self.cheeseList[3]):
                self.winner.setHtml('<div '
                        'style="background-color:white;text-align:center;'
                        'border:1px solid black;">'+self.display_template.format('Hey\
                    {} '.format(self.m_nameEdit.text()) + ' from ' + 
                    self.school.currentText()+'<br>You answered the questions '
                    'and your time was '+str(self.gametimerCount)+' seconds.',24,'blue')+'</div>')
                self.winner.show()
                self.gametimer.stop()
                buttonStart = False
                programmer='No'
                if self.cheeseList[3].correctlabel and\
                self.cheeseList[3].correctlabel == 'a1':
                    programmer='Yes'

                connection = http.client\
                                 .HTTPConnection('207.233.102.195',timeout=2)
                connection.request('GET','/mousegame?name='+\
                        self.m_nameEdit.text().replace(' ','%20')\
                        +'&school='\
                        +self.school.currentText().replace(' ','%20')+'&time='\
                        +str(self.gametimerCount)\
                        +'&programmer='+programmer)

                print(self.cheeseList[3].correctlabel)
                response = connection.getresponse()
                print('{} {} - a response on a GET request by using "http.client"'.format(response.status, response.reason))
                content = response.read().decode('utf-8')
                print(content[:100], '...')
                #hmm... do something with the response?


    def readButtons(self):
        global buttonStart
        if not self.gametimer.isActive() and buttonStart:
            if self.m_nameEdit.text() != '':
                self.gametimer.start(1000)
            else:
                buttonStart = False
                QMessageBox.information(None,'Enter Name', 
                        "Please enter your name.", 
                        QMessageBox.Ok, QMessageBox.Ok)
                

        for b in range(4):
            if buttonPressed(b):
                self.updateMousePosition(self.mouseUpdates[b]['rotation'],self.mouseUpdates[b]['offset'])



