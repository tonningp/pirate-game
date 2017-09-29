#!/usr/bin/env python3

from PyQt5.QtWidgets import (
    QDialog, QPushButton, 
    QHBoxLayout, QVBoxLayout,
    QLabel
    )


class Dialog(QDialog):
    def __init__(self, parent):
        super(Dialog, self).__init__(parent)
        self.parent = parent
        self.setupUi()
        self.okButton.clicked.connect(self.onOkClicked)
        self.cancelButton.clicked.connect(self.onCancelClicked)
        self.result = None

    def onOkClicked(self):
        self.parent.cutlass1.prizes[self.parent.cutlass1.randomNumber]['taken'] = True
        self.hide()

    def show(self):
        #self.label.setText(self.parent.cutlass1.prizes[self.parent.cutlass1.randomNumber]['prize'])
        super(Dialog,self).show()
        print(self.parent.cutlass1.prizes)

    def onCancelClicked(self):
        self.hide()

    def setupUi(self):
        self.okButton = QPushButton("OK")
        self.cancelButton = QPushButton("Cancel")
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)    
        self.setGeometry(300, 300, 300, 150)
        #self.setWindowTitle(self.parent.cutlass1.prizes[self.parent.cutlass1.randomNumber]['prize'])    
