from PyQt5.QtCore import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import (QWidget,
    QPushButton,
    QVBoxLayout, 
    QLabel,
    QGraphicsProxyWidget,
    QMessageBox)

from PyQt5.QtWebKitWidgets import QWebView

class WebWidget(QGraphicsProxyWidget):

    def __init__(self):
        super(WebWidget,self).__init__()
        w = QWidget()
        self.web = QWebView()
        vbox = QVBoxLayout()
        button = QPushButton("close")
        vbox.addWidget(button)
        vbox.addWidget(self.web)
        w.setLayout(vbox)
        self.setWidget(w)
        self.setFlag(QGraphicsItem.ItemIsMovable,True)
        self.setFlag(QGraphicsItem.ItemIsSelectable,True)
        
    def loadAndShowUrl(self,url):
        self.web.load(url)
        self.show()

