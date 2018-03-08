#websocketmanager.py
import asyncio
import datetime
import random
import websockets
import json
TIME = 10.0
HOSTADDRESS = '172.17.1.7'
PORT = 8000

from PyQt5.QtCore import (
    Qt,
    QObject,
    QRunnable,
    QThread,
    QCoreApplication,
    pyqtSignal
    )

class EventEmitter(QObject):
    dataSignal = pyqtSignal(dict)
    def __init__(self,parent=0):
        super().__init__()

    
class Worker(QObject):
    def __init__(self):
        super(Worker,self).__init__() 

    def process(self):
        pass
'''
'_client_connected_cb', '_connection_lost', '_drain_helper', '_drain_lock', '_drain_waiter', '_is_server_shutting_down', '_loop', '_over_ssl', '_paused', '_stream_reader', '_stream_writer', 
'client_connected', 'close', 'close_code', 'close_connection', 'close_reason', 'closing_handshake', 'connection_closed', 'connection_lost', 'connection_made', 'data_received', 'encode_data', 
'ensure_open', 'eof_received', 'extra_headers', 'fail_connection', 'handler', 'handler_task', 'handshake', 'host', 'is_client', 'legacy_recv', 'local_address', 'loop', 'max_queue', 'max_size', 
'messages', 'open', 'opening_handshake', 'origin', 'origins', 'path', 'pause_writing', 'ping', 'pings', 'pong', 'port', 'process_origin', 'process_request', 'process_subprotocol', 
'raw_request_headers', 'raw_response_headers', 'read_data_frame', 'read_frame', 'read_http_request', 'read_limit', 'read_message', 'reader', 'recv', 'remote_address', 'request_headers', 
'response_headers', 'resume_writing', 'run', 'secure', 'select_subprotocol', 'send', 'state', 'state_name', 'subprotocol', 'subprotocols', 'timeout', 'worker_task', 'write_frame', 
'write_http_response', 'write_limit', 'writer', 'ws_handler', 'ws_server'
'''
class WebSocketManager(QThread):

    def __init__(self,loop,parent=None):
        super(WebSocketManager,self).__init__(parent)
        self.loop = loop
        self.current_data = None
        self.data_receive_event = EventEmitter()
        self.producer_event = EventEmitter()
        self.producer = None
        self.connections = set()

    def set_producer(self,producer):
        self.producer = producer

    def connect_data_slot(self,slot):
        self.data_receive_event.dataSignal.connect(slot)

    def connect_producer_slot(self,slot):
        self.producer_event.dataSignal.connect(slot)

    def connect_producer(self,sig):
        sig.connect(self.incoming_data)

    async def get_data(self):
        return self.producer.produce()

    def set_data_slot(self,data):
        self.current_data = data

    async def handler(self,websocket, path):
        consumer_task = asyncio.ensure_future(self.consumer_handler(websocket,path))
        #producer_task = asyncio.ensure_future(self.producer_handler(websocket,path))
        self.connections.add(websocket)
        #[print(s) for s in self.connections]
        #done, pending = await asyncio.wait(
        #    [consumer_task, producer_task],
        #    return_when=asyncio.FIRST_COMPLETED,
        #)
        done, pending = await asyncio.wait(
           [consumer_task],
           return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()

    async def process_message(self,wsocket,message,path):
        if path in ['/connect','/user']:
            self.data_receive_event.dataSignal.emit({'message':message,'path':path,'headers':{'request':wsocket.raw_request_headers,'response':wsocket.raw_response_headers} })
        if self.current_data:
            await wsocket.send(json.dumps(self.current_data))


    async def consumer_handler(self,websocket, path):
        while True:
            try:
                message = await websocket.recv()
                await self.process_message(websocket,message,path)
            except websockets.exceptions.ConnectionClosed:
                print('consumer_handler','ConnectionClosed: ',path)
                self.connections.remove(websocket)


    async def producer_handler(self,websocket, path):
        pass
        while True:
            data = await self.get_data()
            await websocket.send(json.dumps(data))
            await asyncio.sleep(TIME)


    def run(self):
        self.start_server = websockets.serve(self.handler, HOSTADDRESS, PORT)
        self.loop.run_until_complete(self.start_server)
        self.loop.run_forever()

