#log.py
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
    QTextEdit,
    QGraphicsProxyWidget,
    QPushButton,
    QVBoxLayout, 
    QLabel
    )

    
class Log(QWidget):
    clickSignal = pyqtSignal(dict)

    #BoundingRect = QRectF(-width/2,-height/2,width,height)
    def __init__(self,w=500,parent=None):
        super(Log, self).__init__()
        self.w = w 
        self.setStyleSheet("background-color : white")
        fonttype = "Helvetica"
        layout = QVBoxLayout()
        title = QLabel("Log",self)
        title.setFont(QFont(fonttype,12))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        self.log = QTextEdit(self)
        self.log.setReadOnly(True)
        layout.addWidget(self.log)
        self.setLayout(layout)      
    
    def setText(self,text):
        self.log.setText(self.log.toPlainText()+'--------------------\n'+text)

    def connectFunc(self,fn):
        self.clickSignal.connect(fn)

