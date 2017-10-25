# -*- coding:utf-8 -*-
#编码声明
import uuid
 
unique_id = lambda: str(uuid.uuid1())
 
class MessageServer(object):
    
    servers = {}
     
    def __init__(self, id=None):
        self.id = id or unique_id()
        self.observers = []
        self.messages = []
        self.__class__.servers[id] = self
     
    def listen(self, success_callback):
        self.observers.append(success_callback)
        return success_callback
     
    def add_message(self, message, id=None):
        id = id or unique_id()
        try:
            self.messages.append((id,message))
            [callback(id, message) for callback in self.observers]
        finally:
            self.observers = []