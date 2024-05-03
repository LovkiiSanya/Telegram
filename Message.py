
import schedule
import datetime
import random
import time
import enum
import psycopg2
from create_db import *


message_dict = {}



class Message:

    def __init__(self) -> None:
        self.__content: str = None  # текст сообщения 
        self.__recipient: str = None  # имя получателя 
        self.__time: datetime = None  # время отправки сообщения 

    # def get_id(self):
    #     return self.__id
    
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
        
    def set_message_parameters(self) -> "Message":
        message = Message()
        content = input("Тут вы можете ввести свое сообщение,но не хулиганьте!")
        message.set_content(content)
        user_name = input("Кому отправляем сообщение ? ")
        message.set_recipient(user_name)
        time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        message.set_time(time)
    
        new_record_table = basic_text_message(content, user_name, time, "Text message")
        new_record_table.save()
        new_record_id = new_record_table.id
        print("ID новой записи:", new_record_id)


    

    
    def __repr__(self):
        Message = type(self).__name__
        return f"{Message}({self.get_content()!r},{self.get_recipient()!r},{self.get_time()!r})"

    def __str__(self):
        return f"Ваше сообщение: {self.get_content()} Получатель: {self.get_recipient()} Время отправки {self.get_time()}"
