#!/usr/bin/env python3
TITLE="Pi-Day"
NUMBER_OF_PLAYERS = 5
TIMER_INTERVAL = 10000
import sys
import math
import asyncio
import datetime
import random
import websockets
import resources
from questions import questions
from dialogs.treasure import Dialog

import etchlib.websocketmanager
from etchlib.serialcomm import (
    EventEmitter,
    SerialManager)
from PyQt5.QtCore import (
        Qt,
        QTime,
        QTimer,
        pyqtSignal,
        qsrand,
        QPointF,
        QRectF
)
from PyQt5.QtCore import pyqtSlot
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
        QGraphicsProxyWidget,
        QWidget,
        QFrame,
        QStyle,
        QTabWidget,
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
    produceSig = pyqtSignal(dict)

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

    def spin(self,i):
        self.cutlass1.spin()

    def buttonPress(self,b):
        print('button:{0}'.format(b))

    def player1Point(self,event):
        self.player1.addPoint()

    def player2Point(self,event):
        self.player2.addPoint()

    def player3Point(self,event):
        self.player3.addPoint()

    def resetPlayers(self,event):
        self.player1.reset()
        #self.player2.reset()
        self.player3.reset()

    def prizeNumberHandler(self,number):
        #print(self.cutlass1.prizes[self.cutlass1.randomNumber]['prize'])
        pass

    def loadMainView(self):
        from etchlib.scenes.main import Scene as MScene 
        from etchlib.views.mainview import View as MainView
        from etchlib.graphicsitem.svg import Item as SvgItem
        from etchlib.widgets.circledisplay import Circle
        from etchlib.widgets.radian import Spinner
        from etchlib.widgets.leaderboard import Leaderboard
        from etchlib.widgets.linewidget import Line
        from etchlib.widgets.log import Log
        from etchlib.widgets.debrujn import Debrujn
        from etchlib.widgets.questionwidget import Question
        from etchlib.graphicsitem.waveanimation import WaveAnimation
        from etchlib.graphicsitem.player import Item as Player

        scene = MScene(QRectF(-self.size().width()/2,-self.size().height()/2,self.size().width(),self.size().height()))
        objsize = 1200
        self.timer_interval = TIMER_INTERVAL
        self.circle = Circle(objsize)
        self.spinner = Spinner(objsize)
        self.wave = WaveAnimation()
        self.wave.movable(True)
        #q = Question(objsize)
        #l = Line(objsize)
        #l.connectFunc(self.circle.valueChanged)
        #l.connectFunc(self.spinner.valueChanged)
        #self.line = scene.addWidget(l)
        #self.line.setFlag(QGraphicsProxyWidget.ItemIsMovable,True)
        #self.line.resize(math.pi*objsize,objsize/8)
        #self.line.setPos(QPointF(-math.pi*objsize/2,objsize/2))
        self.leader = Leaderboard(NUMBER_OF_PLAYERS,objsize)
        self.produceSig.connect(self.leader.questionChanged)
        self.leaderwidget = scene.addWidget(self.leader)
        self.leaderwidget.resize(objsize,objsize/2)
        self.leaderwidget.setPos(QPointF(0,-0.5*scene.height()))
        self.debrujn = Debrujn(objsize*0.5)
        self.circle.movable(True).selectable(True)
        self.circle.setPos(QPointF(-0.25*scene.width(),0))
        self.debrujn.movable(True).selectable(True)

        # self.log = Log(objsize)
        # self.logwidget = scene.addWidget(self.log)
        # self.logwidget.resize(objsize,objsize/2)
        # self.logwidget.setPos(QPointF(0,0))

        #self.question = scene.addWidget(q)
        #self.question.setFlag(QGraphicsProxyWidget.ItemIsMovable,True)
        #self.question.resize(3*objsize/4,objsize/2)
        #self.question.setPos(QPointF(-5*objsize/4,-0.7*objsize))
        #q.connectFunc(self.circle.valueChanged)
        #q.random_question()
        scene.addItem(self.circle)
        scene.addItem(self.spinner)
        scene.addItem(self.debrujn)
        #scene.addItem(self.wave)
        #self.debrujn.hide()
        self.spinner.hide()
        self.circle.update()
        #scene.addItem(self.wave)
        view = MainView(self)
        view.setScene(scene)
        vbox = QVBoxLayout()
        vbox.addWidget(view)
        self.treasuredialog = Dialog(self) 
        self.setCentralWidget(view)
        self.game_timer = QTimer(self)
        self.game_timer.timeout.connect(self.gameTimer_slot)
        self.game_timer.start(self.timer_interval)
 

    def run_code(self):
        self.runCode.emit()

    def help(self):
        dialog = QMessageBox.about(self,"About Pi Day Program","Proudly developed by Paul Tonning (CIS) and Darrel Harriman (Electronics)")

    def showTreasure(self):
        self.treasuredialog.setWindowTitle(self.cutlass1.prizes[self.cutlass1.randomNumber]['prize'])    
        self.treasuredialog.show()

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

        # player1Button = QAction(QIcon(':/images/player1_sb.svg'), 'Player 1', self)
        # player1Button.setShortcut('Ctrl+1')
        # player1Button.setStatusTip('Add 1 to player 1')
        # player1Button.triggered.connect(self.player1Point)
        # fileMenu.addAction(player1Button)
        # self.toolbar = self.addToolBar('Player 1')
        # self.toolbar.addAction(player1Button)
        # # player2Button = QAction(QIcon(':/images/player2_sb.svg'), 'Player 1', self)
        # # player2Button.setShortcut('Ctrl+2')
        # # player2Button.setStatusTip('Add 1 to player 2')
        # # player2Button.triggered.connect(self.player2Point)
        # # fileMenu.addAction(player2Button)
        # # self.toolbar = self.addToolBar('Player 2')
        # # self.toolbar.addAction(player2Button)
        # player3Button = QAction(QIcon(':/images/player3_sb.svg'), 'Player 1', self)
        # player3Button.setShortcut('Ctrl+3')
        # player3Button.setStatusTip('Add 1 to player 3')
        # player3Button.triggered.connect(self.player3Point)
        # fileMenu.addAction(player3Button)
        # self.toolbar = self.addToolBar('Player 3')
        # self.toolbar.addAction(player3Button)
        # resetButton = QAction(QIcon(':/images/reset_sb.svg'), 'Player 1', self)
        # resetButton.setShortcut('Ctrl+R')
        # resetButton.setStatusTip('Reset Players')
        # resetButton.triggered.connect(self.resetPlayers)
        # fileMenu.addAction(resetButton)
        # self.toolbar = self.addToolBar('Reset')
        # self.toolbar.addAction(resetButton)

        # aboutButton = QAction(QIcon(':/images/icons/about64x64.png'), 'About', self)
        # aboutButton.setShortcut('F1')
        # aboutButton.setStatusTip('About the application')
        # aboutButton.triggered.connect(self.help)
        # helpMenu.addAction(aboutButton)
        # mainButton = QAction(QIcon(':/images/icons/home64x64.png'), 'Main View', self)
        # mainButton.setShortcut('Ctrl+M')
        # mainButton.setStatusTip('Main View')
        # mainButton.triggered.connect(self.loadMainView)
        # gameMenu.addAction(mainButton)
        # treasureButton = QAction(QIcon(':/images/Treasure_chest.svg'), 'Treasure Chest', self)
        # treasureButton.setShortcut('Ctrl+T')
        # treasureButton.setStatusTip('TreasureChest')
        # treasureButton.triggered.connect(self.showTreasure)
        # gameMenu.addAction(treasureButton)
        # self.statusBar().showMessage('Message in statusbar.')

    def data_slot(self,message):
        #self.log.setText(str(message))
        self.leader.processMessage(message)

    def gameTimer_slot(self):
        question = self.circle.random_question(self.produceSig)
        

class MyTableWidget(QWidget): 
    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
 
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()   
        self.tab2 = QWidget()
        self.tabs.resize(300,200) 
 
        # Add tabs
        self.tabs.addTab(self.tab1,"Tab 1")
        self.tabs.addTab(self.tab2,"Tab 2")
 
        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)
 
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
 
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    now = QTime.currentTime()
    qsrand(now.msec())
    app = QApplication(sys.argv)
    #sreader = SerialManager()
    #sreader.setEmitter(EventEmitter())
    #sreader.finished.connect(app.exit)
    win = App(TITLE)
    ws_manager = etchlib.websocketmanager.WebSocketManager(asyncio.get_event_loop())
    ws_manager.finished.connect(app.exit)
    ws_manager.connect_data_slot(win.data_slot)
    win.produceSig.connect(ws_manager.set_data_slot)
    #ws_manager.connect_producer_slot(win.gameTimer_slot)
    #ws_manager.set_producer(win.circle)
    ws_manager.start()
    #sreader.setPlatterHandler(win.spin)    
    #sreader.setButtonHandler(win.buttonPress)   
    #sreader.start()
    sys.exit(app.exec_())
