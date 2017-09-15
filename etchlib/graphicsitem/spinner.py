import math
import random
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
    QGraphicsObject,
    QGraphicsTextItem
    )

class Spinner(QGraphicsObject):
    tickSignal = pyqtSignal(int)
    prizes = {
        '0' : ''
    }
    points = [
        'Bankrupt',
        100,
        200,
    ]

    def __init__(self,file,scale=1.0,parent=None):
        super(Spinner, self).__init__()
        self.compass = svg.Item(":/images/compass.svg",1.0,self)
        self.compass.setTransform(self.compass.transform().scale(6.25,7.25).translate(-5.3,-16.0))
        self.spinner = svg.Item(file,scale,self)
        self.spinner.setPos(self.spinner.pos().x(),-self.boundingRect().width()/4)
        self.rect = self.boundingRect()
        self.center = self.rect.center()
        self.radius = self.rect.width()/2
        self.numbers = []
        self.spinCount = 48 # run for 2 periods for a longer wave
        self.currentSpin = 0
        self.div = 15
        for a in range(self.spinCount//2):
            theta = self.toRad(a*self.div + 5) 
            textPoint = QPointF(self.center.x() + self.radius*math.cos(theta)-20,self.center.y() + self.radius*math.sin(theta)-10)
            item = QGraphicsTextItem("{0}".format(a+1),self)
            item.setFont(QFont("Comic Sans MS", 36))
            item.setDefaultTextColor(Qt.yellow)
            self.numbers.append(item)
            item.setPos(textPoint)
        for i in range(9):
            self.spin()
        self.currentSpin = 1

    def connectFunc(self,fn):
        self.tickSignal.connect(fn)

    def toRad(self,deg):
        return deg*math.pi/180

    def spin(self):
        for i in self.numbers:
            i.setDefaultTextColor(Qt.black)
        scale = self.spinner.scale
        r = self.spinner.boundingRect() 
        transform = self.spinner.transform() \
                        .translate(self.spinner.scale*r.width()/2,self.spinner.scale*r.height()/2) \
                        .rotate(self.spinner.rotation()+self.div) \
                        .translate(-self.spinner.scale*r.width()/2,-self.spinner.scale*r.height()/2)
        self.spinner.setTransform(transform)
        self.tickSignal.emit(self.currentSpin)
        self.numbers[self.currentSpin%(self.spinCount//2)].setDefaultTextColor(Qt.yellow)
        self.currentSpin += 1
        if self.currentSpin > self.spinCount-1:
            self.currentSpin = 0

    def randomSpin(self):
        stop = random.randint(50,75)
        print(stop)
        
    def boundingRect(self):
        r = self.spinner.boundingRect()
        return QRectF(r.left(),r.top(),r.width()*(self.spinner.scale),r.width()*(self.spinner.scale))

    def movable(self,m=True):
        self.setFlag(QGraphicsObject.ItemIsMovable,m)
        return self

    def paint(self, painter, option, widget):
        #painter.drawEllipse(self.rect)
        # for a in range(self.spinCount):
        #     angle = a*self.div
        #     startAngle = angle * 16
        #     spanAngle = self.div*16
        #     if a % 2:
        #         painter.setBrush(Qt.red)
        #         painter.setPen(Qt.red)
        #     else:
        #        painter.setBrush(Qt.blue)
        #        painter.setPen(Qt.blue)
            #painter.drawPie(self.rect, startAngle, spanAngle);
        painter.setBrush(Qt.white)
        painter.drawEllipse(QRectF(self.rect.width()/2-300,self.rect.height()/2-285,600,600))
        painter.setBrush(Qt.red)
        painter.drawEllipse(QRectF(self.rect.width()/2-50,self.rect.height()/2-35,100,100))
