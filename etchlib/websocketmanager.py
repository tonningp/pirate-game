#websocketmanager.py
import asyncio
import datetime
import random
import websockets

from PyQt5.QtCore import (
    Qt,
    QObject,
    QRunnable,
    QThread,
    QCoreApplication,
    pyqtSignal
    )

class EventEmitter(QObject):
    dataSignal = pyqtSignal(str)
    def __init__(self,parent=0):
        super().__init__()

    
class Worker(QObject):
    def __init__(self):
        super(Worker,self).__init__() 

    def process(self):
        pass

class WebSocketManager(QThread):

    def __init__(self,loop,parent=None):
        super(WebSocketManager,self).__init__(parent)
        self.loop = loop
        self.event = EventEmitter()

    def connect_data_slot(self,slot):
        self.event.dataSignal.connect(slot)

    async def handler(self,websocket, path):
        consumer_task = asyncio.ensure_future(self.consumer_handler(websocket,path))
        producer_task = asyncio.ensure_future(self.producer_handler(websocket,path))
        done, pending = await asyncio.wait(
            [consumer_task, producer_task],
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()

    async def consumer(self,message):
        #print(message)
        self.event.dataSignal.emit(message)

    async def consumer_handler(self,websocket, path):
       while True:
          message = await websocket.recv()
          await self.consumer(message)

    #async def consumer_handler(websocket, path):
    #    async for message in websocket:
    #        await consumer(message)

    async def producer_handler(self,websocket, path):
        while True:
            now = datetime.datetime.utcnow().isoformat() + 'Z'
            await websocket.send(now)
            await asyncio.sleep(random.random() * 3)

    def set_loop(self,loop):
        self.loop = loop
    def run(self):
        start_server = websockets.serve(self.handler, '127.0.0.1', 8000)
        self.loop.run_until_complete(start_server)
        self.loop.run_forever()

