#linewidget.py
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
    QVBoxLayout, 
    QLabel,
    QSlider,
    QGraphicsTextItem
    )
data = [
{   
    'text':'Find the <span style="font-weight:bold;">circumference</span>. Use 3.14 as an approximation for π.<br> A correct answer would look like 4.78 in.',
    'type' : 'circum-approx',
    'diameter' : False,
    'units' : 'in',
    'radius' : 0,
    'answer' : 0
},
{   
    'text':'Find the <span style="font-weight:bold;">circumference</span> in terms of π and the unit of measurement.<br>Type "pi" in for π so that "7.00π m" would look like "7.00pi m".',
    'type' : 'circum-exact',
    'diameter' : False,
    'units' : 'in',
    'radius' : 0,
    'answer' : 0
},
{   
    'text':'Find the <span style="font-weight:bold;">area</span> in terms of π and the unit of measurement.<br>Type "pi" in for π so that "56.25π m<sup>2</sup>" would look like "56.25pi m^2".',
    'type' : 'area-exact',
    'diameter' : False,
    'units' : 'in',
    'radius' : 0,
    'answer' : 0
},
{   
    'text':'Find the <span style="font-weight:bold;">area</span>. Use 3.14 as an approximation for π.<br> A correct answer would look like 314.00 in^2.',
    'type' : 'area-approx',
    'diameter' : False,
    'units' : 'in',
    'radius' : 0,
    'answer' : 0
}
]

units = ['in', 'ft','cubits','yards','furlongs','leagues','m','cm','km','mi','mm','parsecs']
    
class Question(QWidget):
    clickSignal = pyqtSignal(dict)

    #BoundingRect = QRectF(-width/2,-height/2,width,height)
    def __init__(self,w=500,scale=1.0,parent=None):
        super(Question, self).__init__()
        self.w = w 
        #self.setAcceptHoverEvents(True)
        vbox = QVBoxLayout()
        self.question_label = QLabel('', self)
        vbox.addWidget(self.question_label)
        self.answer1_label = QLabel('', self)
        vbox.addWidget(self.answer1_label)
        self.answer2_label = QLabel('', self)
        vbox.addWidget(self.answer2_label)
        self.setLayout(vbox)      
        self.random_question()
        #self.resize(self.w,self.height())
        #self.setWidget(widget)

    def random_question(self):
        index = randint(0,len(data)-1)
        data[index]['radius'] = randint(1,50)
        data[index]['diameter']  = randint(0,1)
        data[index]['units'] = units[randint(0,len(units)-1)]
        if data[index]['type'] == 'circum-approx':
            data[index]['answer'] = '{0:.2f} {1}'.format(data[index]['radius'] /(data[index]['diameter']+1) * 6.28,data[index]['units'])
        elif data[index]['type'] == 'circum-exact':
            data[index]['answer'] = '{0:.2f}pi {1}'.format(float(data[index]['radius']/(data[index]['diameter']+1) * 2) ,data[index]['units'])
        elif data[index]['type'] == 'area-exact':
            data[index]['answer'] = '{0:.2f}pi {1}'.format(float((data[index]['radius']/(data[index]['diameter']+1))**2),'{0}^2'.format(data[index]['units']))
        elif data[index]['type'] == 'area-approx':
            data[index]['answer'] = '{0:.2f} {1}'.format((data[index]['radius'] /(data[index]['diameter']+1)) ** 2*3.14,'{0}^2'.format(data[index]['units']))
        self.question_label.tmpl = '<span style="font-size:48px;font-color:blue;">{0}</span>'
        self.question_label.setText(self.question_label.tmpl.format(data[index]['text']))
        self.answer1_label.tmpl = '<span style="font-size:48px;font-color:blue;">{0}</span>'
        self.answer1_label.setText(self.answer1_label.tmpl.format(data[index]['radius'])+' '+str(data[index]['diameter']))
        self.answer2_label.tmpl = '<span style="font-size:48px;font-color:blue;">{0}</span>'
        self.answer2_label.setText(self.answer2_label.tmpl.format(data[index]['answer']))
        self.question_index = index
        self.clickSignal.emit(data[index])

    def connectFunc(self,fn):
        self.clickSignal.connect(fn)

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


    def hoverMoveEvent(self,event):
        super(Question,self).hoverMoveEvent(event)
        self.update()

    def mouseMoveEvent(self,event):
        super(Question,self).mouseMoveEvent(event)
        self.update()

    def mousePressEvent(self,event):
        self.random_question()
        super(Question,self).mousePressEvent(event)
        self.update()

    def movable(self,m=True):
        self.setFlag(QGraphicsObject.ItemIsMovable,m)
        return self

    def selectable(self,m=True):
        self.setFlag(QGraphicsObject.ItemIsSelectable,m)
        return self
