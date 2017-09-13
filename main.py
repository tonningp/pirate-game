#!/usr/bin/env python3
import sys
import resources

from PyQt5.QtCore import (
        Qt,
        QTime,
        pyqtSignal,
        qsrand,
        QPointF,
        QRectF
)
from PyQt5.QtGui import (
    QIcon,
    QTransform
    )
from PyQt5.QtWidgets import (
        QApplication,
        QMainWindow,
        QPushButton,
        QSplitter,
        QMessageBox,
        QVBoxLayout,
        QHBoxLayout,
        QStyleFactory,
        QWidget,
        QFrame,
        QStyle,
        QAction
)


class App(QMainWindow):
    """
    Resources:
http://www.python-course.eu/index.php
    """
    aboutHTML = """
    Author: Paul Tonning<br>
    License: GPL<br>
    Description: Don't know yet, it's evolving<br>
    Copyright: 2017<br>
    """
    showEditor = pyqtSignal()
    hideEditor = pyqtSignal()
    runCode = pyqtSignal()
    printPDF = pyqtSignal()

    def __init__(self,title):
        super().__init__()
        self.title = title
        self.fullScreen()
        self.initUI()
        self.loadMainView()

    def fullScreen(self):
        self.showFullScreen()

    def ship1Click(self,event):
            print('ship1 clicked {0},{1}'.format(event.pos().x(),event.pos().y()))
            p = self.ship1.mapToScene(event.pos())
            print('ship1 scenePos clicked {0},{1}'.format(p.x(),p.y()))


    def loadMainView(self):
        from etchlib.scenes.main import Scene as MScene 
        from etchlib.views.mainview import View as MainView
        from etchlib.graphicsitem.svg import Item as SvgItem
        from etchlib.graphicsitem.spinner import Spinner
        from etchlib.graphicsitem.speechbubble import Bubble
        from etchlib.graphicsitem.waveanimation import WaveAnimation
        from gameitems.wordboard import WordBoard
        scene = MScene(QRectF(-self.size().width()/2,-self.size().height()/2,self.size().width(),self.size().height()))
        self.treasure_map = SvgItem(":/images/Treasure_map.svg",13.0)
        self.treasure_map.movable()
        self.treasure_map.setPos(QPointF(-self.size().width()/2,-self.size().height()/2))
        self.pirate = SvgItem(":/images/Pirate.svg",0.75)
        self.speechbubble = Bubble()
        transform = QTransform()
        transform.scale(2.0, 1.25)
        self.speechbubble.setTransform(transform);
        self.speechbubble.movable()
        self.speechbubble.setPos(QPointF(-self.size().width()/2+1.5*self.pirate.boundingRect().width(),-600))
        self.pirate.movable()
        self.pirate.setPos(QPointF(-self.size().width()/2+75,-350))
        self.cutlass1 = Spinner(":/images/cutlass1.svg",0.75)
        self.cutlass1.movable(True)
        self.cutlass1.setPos(QPointF(-self.size().width()/2,self.treasure_map.boundingRect().top()))
        self.pirate.onLeftClick(lambda x: self.cutlass1.spin())
        scene.addItem(self.treasure_map)
        scene.addItem(self.pirate)
        scene.addItem(self.speechbubble)
        scene.addItem(self.cutlass1)
        #self.wordboard = WordBoard({"word1":"circumference / diameter"})
        #self.wordboard.setPos(QPointF(self.cutlass1.pos().x()+self.cutlass1.boundingRect().width()+50,-350))
        #scene.addItem(self.wordboard)
        self.wave = WaveAnimation()
        self.cutlass1.connectFunc(self.wave.updateTick)
        self.wave.movable(True)
        scene.addItem(self.wave)
        self.wave.setPos(QPointF(self.cutlass1.pos().x()+2*self.cutlass1.boundingRect().width()+50,300))
        view = MainView(self)
        view.setScene(scene)
        vbox = QVBoxLayout()
        vbox.addWidget(view)
        self.setCentralWidget(view)

    def run_code(self):
        self.runCode.emit()

    def printPDFEmit(self):
        self.printPDF.emit()

    def help(self):
        print("Help")

    def initUI(self):
        self.setWindowTitle(self.title)
 
        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu('File')
        gameMenu = mainMenu.addMenu('View')
        toolMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')
 
        exitButton = QAction(QIcon(':/images/icons/exit64x64.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitButton)

        aboutButton = QAction(QIcon(':/images/icons/about64x64.png'), 'About', self)
        aboutButton.setShortcut('F1')
        aboutButton.setStatusTip('About the application')
        aboutButton.triggered.connect(self.help)
        helpMenu.addAction(aboutButton)
        mainButton = QAction(QIcon(':/images/icons/home64x64.png'), 'Main View', self)
        mainButton.setShortcut('Ctrl+M')
        mainButton.setStatusTip('Main View')
        mainButton.triggered.connect(self.loadMainView)
        gameMenu.addAction(mainButton)
        self.statusBar().showMessage('Message in statusbar.')
        
if __name__ == '__main__':
    now = QTime.currentTime()
    qsrand(now.msec())
    app = QApplication(sys.argv)
    win = App("Talk Like a Pi-Rate Day")
    sys.exit(app.exec_())
