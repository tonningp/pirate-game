#!/usr/bin/env python3
import serial, time
from PyQt5.QtCore import (
    Qt,
    QObject,
    QRunnable,
    QThread,
    QCoreApplication,
    pyqtSignal
    )

class EventEmitter(QObject):
    spinSig = pyqtSignal(int)
    buttonSig = pyqtSignal(int)

    def __init__(self,parent=0):
        super().__init__()


    def setSpinFunction(self,f):
        self.spinSig.connect(f)

    def setButtonFunction(self,f):
        self.buttonSig.connect(f)

    def spin(self,d):
        self.spinSig.emit(int(d))

    def button(self,b):
        self.buttonSig.emit(int(b))


class SerialManager(QThread):

    def initSerial(self):
        #initialization and open the port

        #possible timeout values:
        #    1. None: wait forever, block call
        #    2. 0: non-blocking mode, return immediately
        #    3. x, x is bigger than 0, float allowed, timeout block call

        self.ser = serial.Serial()
        self.ser.port = "/dev/cu.SLAB_USBtoUART"
        self.ser.baudrate = 115200
        self.ser.bytesize = serial.EIGHTBITS #number of bits per bytes
        self.ser.parity = serial.PARITY_ODD #set parity check: no parity
        self.ser.parity = serial.PARITY_NONE #set parity check: no parity
        self.ser.stopbits = serial.STOPBITS_ONE #number of stop bits
        self.ser.timeout = 1            #non-block read
        self.ser.xonxoff = False     #disable software flow control
        self.ser.rtscts = False     #disable hardware (RTS/CTS) flow control
        self.ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
        self.ser.writeTimeout = 2     #timeout for write

    def setEmitter(self,emitter):
        self.emitter = emitter

    def setPlatterHandler(self,f):
        self.emitter.setSpinFunction(f)

    def setButtonHandler(self,f):
        self.emitter.setButtonFunction(f)

    def run(self):
        self.initSerial()
        try: 
            self.ser.open()
        except Exception as e:
            print ("error open serial port: " + str(e))
            exit()
        if self.ser.isOpen():
            try:
                self.ser.flushInput() #flush input buffer, discarding all its contents
                time.sleep(0.5)  #give the serial port sometime to receive the data
                numOfLines = 0
                while True:
                    response = self.ser.readline().strip()
                    response = response.decode('utf-8')
                    if response == '':
                        pass
                    elif 'p' in response:
                        v = response.split(':')
                        self.emitter.spin(v[1])
                    elif 'b' in response:
                        v = response.split(':')
                        self.emitter.button(v[1])
                        
                self.ser.close()
            except Exception as e1:
               print("error communicating...: " + str(e1))
        else:
            print ("cannot open serial port ")

if __name__ == "__main__":
    import sys
    app = QCoreApplication([])
    sreader = SerialManager()
    sreader.setEmitter(EventEmitter())
    sreader.setPlatterHandler(lambda x: print("spin:{0}".format(x)))    
    sreader.setButtonHandler(lambda x: print("button:{0}".format(x)))   
    sreader.finished.connect(app.exit)
    sreader.start()
    sys.exit(app.exec_())
