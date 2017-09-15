#!/usr/bin/env python3
import serial, time

class SerialManager:
	def __init__(self):

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

		try: 
		    self.ser.open()
		except Exception as e:
		    print ("error open serial port: " + str(e))
		    exit()
		if self.ser.isOpen():
		    #try:
		        self.ser.flushInput() #flush input buffer, discarding all its contents
		        #self.ser.flushOutput()#flush output buffer, aborting current output 
		                 #and discard all that is in buffer
		        #write data
		        #ser.write("AT+CSQ")
		        #print("write data: AT+CSQ")
		        time.sleep(0.5)  #give the serial port sometime to receive the data
		        numOfLines = 0
		        while True:
		            response = self.ser.readline().strip()
		            print("{0}".format(str(response)))
		        self.ser.close()
		    #except Exception as e1:
		    #    print("error communicating...: " + str(e1))
		else:
		    print ("cannot open serial port ")

if __name__ == "__main__":
	sm = SerialManager()