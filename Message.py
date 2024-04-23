from typing import Self
import schedule
import datetime
import random
import time
import enum
import psycopg2
from peewee import *
from create_DB import *


message_dict = {}



class Message:

    def __init__(self) -> None:
        self.__id: int = random.randint(1, 1000000)
        self.__content: str = None # текст сообщения 
        self.__recipient: str = None # имя получателя 
        self.__time: datetime = None # время отправки сообщения 

    def get_id(self):
        return self.__id
    
    def set_content(self,content:str)->str:
        self.__content = content

    def get_content(self):
        return self.__content
    
    def set_recipient(self,recipient:str)->str:
        self.__recipient = recipient

    def get_recipient(self):
        return self.__recipient

    def set_time(self,time:datetime)->datetime:
        self.__time = time

    def get_time(self):
        return self.__time
        
    def set_message_parameters() -> "Message":
        message = Message()
        content = input("Тут вы можете ввести свое сообщение,но не хулиганьте!")
        message.set_content(content)
        user_name = input("Кому отправляем сообщение ? ")
        message.set_recipient(user_name)
        time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        message.set_time(time)
        message_dict[message.get_id()] = message
        print("Айди для архива сообщений,", message.get_id())
        TelegaTable.create(message_table_type = "Text Format",message_table_content = message.get_content(),message_table_recipient = message.get_recipient(),message_table_date = message.get_time())
        return message

    

    
    def __repr__(self):
        Message = type(self).__name__
        return f"{Message}({self.get_id()!r},{self.get_content()!r},{self.get_recipient()!r},{self.get_time()!r})"

    def __str__(self):
        return f"ID вашего сообщения:{self.get_id()} Ваше сообщение: {self.get_content()} Получатель: {self.get_recipient()} Время отправки {self.get_time()}"