#leaderboard.py
'''
Option 1: Derive from QGraphicsProxyWidget and in the mouse functions (mouseMove, ...) you can call 
QGraphicsItem::mouseMove() again, this should bring back again the functionality of moving the Widget.
Option 2: This is more like a workaround, but in most cases the better solution, because it prevents 
you from managing the events as it would be necessary by option 1. Just create a GraphicsRectItem R, i
which is larger than your Widget W. Set R movable etc. Add W to your scene, you will receive a 
QGraphicsProxyWidget P. Call P->setParentItem(R) and finally scene->AddItem(R);
Now your Widget can be moved by moving the parent rectangle. You can also add additional 
GraphicsRectIrems r which have R as parent, e.g. to implement a resizing function. 
You would just have to install an EventFilter for r and react on the mouseMove event in the 
filter function.
'''

import math
from random import randint
import json
from PyQt5.QtCore import(
    Qt,
    QRectF,
    QPointF,
    QPoint,
    pyqtSignal
)
from PyQt5.QtGui import(
    QFont,
    QPainter
)
from PyQt5.QtWidgets import (
    QWidget,
    QGraphicsObject,
    QGraphicsProxyWidget,
    QLCDNumber,
    QPushButton,
    QGridLayout, 
    QLabel,
    QSlider,
    QGraphicsTextItem
    )

    
class Leaderboard(QWidget):
    clickSignal = pyqtSignal(dict)

    #BoundingRect = QRectF(-width/2,-height/2,width,height)
    def __init__(self,players=4,w=500,scale=1.0,parent=None):
        super(Leaderboard, self).__init__()
        self.w = w 
        self.setStyleSheet("background-color : white")
        #self.setAcceptHoverEvents(True)
        grid = QGridLayout()
        self.num_players = players 
        fonttype = "Helvetica"
        title = QLabel("Players",self)
        title.setFont(QFont(fonttype,42))
        title.setAlignment(Qt.AlignCenter)
        grid.addWidget(title,0,0,1,3)
        name = QLabel("Name",self)
        name.setFont(QFont(fonttype,42))
        name.setAlignment(Qt.AlignCenter)
        grid.addWidget(name,1,0)
        answer = QLabel("Answer",self)
        answer.setFont(QFont(fonttype,42))
        answer.setAlignment(Qt.AlignCenter)
        grid.addWidget(answer,1,1)
        score = QLabel("Score",self)
        score.setFont(QFont(fonttype,42))
        score.setAlignment(Qt.AlignCenter)
        grid.addWidget(score,1,2)
        self.scores = [(QLabel(''),QLabel(''),QLabel('0')) for x in range(self.num_players) ]
        # add scores to grid layout
        [(grid.addWidget(n[0],i+2,0),grid.addWidget(n[1],i+2,1),grid.addWidget(n[2],i+2,2)) 
             for i,n in enumerate(self.scores)]
        #set the properties
        [  
            (   [v.setFont(QFont(fonttype,36)) for v in x],
                [v.setAlignment(Qt.AlignCenter) for v in x],
                [v.setStyleSheet("border-bottom : 1px solid black;background-color : {0}".format("white" if i%2 else "Cornsilk")) for v in x]
            ) 
                for i,x in enumerate(self.scores) 
        ]
        self.setLayout(grid)      
        

    def connectFunc(self,fn):
        self.clickSignal.connect(fn)

    def resetScores(self):
        [(n[0].setText(''),n[1].setText(''),n[2].setText('')) for n in self.scores]

    def addUser(self,user):
        for n in self.scores:
            if n[0].text() == user:
                break
            elif n[0].text() == '':
                n[0].setText(user)
                break

    def updateScore(self,v):
        for n in self.scores:
            if n[0].text() == v['name']:
                n[1].setText(v['answer'])
                n[2].setText(v['timestamp'])
                break

    def clearAnswers(self):
        for n in self.scores:
            n[1].setText('')

    def processMessage(self,payload):
        if payload['path'] == '/connect':
            try:
                v = json.loads(payload['message'])
                self.addUser(v['name'])
            except TypeError:
                print('processMessage','Type Error',payload)

        elif payload['path'] == '/user':
            try:
                v = json.loads(payload['message'])
                self.updateScore(v)
            except TypeError:
                print('processMessage','Type Error',payload)

    def questionChanged(self,question):
        self.currentQuestion = question
        self.clearAnswers()

    def valueChanged(self,value):
        self.lcdRadians.display((2*math.pi*value)/self.w)
        self.lcdDegrees.display((180*self.lcdRadians.value()/math.pi))
        self.tickSignal.emit(2*math.pi*value/self.w)

    def onLeftClick(self,f):
        if not hasattr(self,'leftClickF'):
            self.leftClickF = []
        self.leftClickF.append(f)
        return self

    def onRightClick(self,f):
        if not hasattr(self,'rightClickF'):
            self.rightClickF = []
        self.rightClickF.append(f)
        return self

    def setPlayerName(self,index,name):
        self.scores[index][0].setText(name)

    def setPlayerAnswer(self,index,answer):
        self.scores[index][1].setText(answer)

    def setPlayerScore(self,index,score):
        self.scores[index][2].setText(score)

    def hoverMoveEvent(self,event):
        super(Leaderboard,self).hoverMoveEvent(event)
        self.update()

    def mouseMoveEvent(self,event):
        super(Leaderboard,self).mouseMoveEvent(event)
        self.update()

    def mousePressEvent(self,event):
        super(Leaderboard,self).mousePressEvent(event)
        self.update()

    def movable(self,m=True):
        self.setFlag(QGraphicsObject.ItemIsMovable,m)
        return self

    def selectable(self,m=True):
        self.setFlag(QGraphicsObject.ItemIsSelectable,m)
        return self
