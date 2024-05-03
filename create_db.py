
from peewee import *

connection = PostgresqlDatabase("postgres",
                                host="127.0.0.1", user="admin", password="root"
                                )
# try:
#     connection = PostgresqlDatabase("postgres",
#                                     host="127.0.0.1", user="admin", password="root"
#                                     )
#     connection.autocommit = True
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT version();")
#         print(cursor.fetchone())
#
# except Exception as _ex:
#     print("[INFO] Ошибка при работе с Базой данных", _ex)
# finally:
#     if connection:
#         connection.close()
#         print("[INFO] Соединение с Базой данных закрыто.")

connection.connect()

class BaseModel(Model):
    class Meta:
        database = connection

class TelegaText(BaseModel):
    message_table_type = TextField(column_name="message_type")  # тип сообщения
    message_table_content = TextField(column_name="content")  # содержимое сообщения
    message_table_recipient = TextField(column_name="recipient")  # имя получателя
    message_table_date = DateTimeField(column_name="time")  # дата отправки


class TelegaAudio(BaseModel):
    message_table_type = TextField(column_name="message_type")  #тип сообщения
    message_table_content = TextField(column_name="content")  #содержимое сообщения
    message_table_recipient = TextField(column_name="recipient")  #имя получателя
    message_table_date = DateTimeField(column_name="time")  #дата отправки
    message_table_duration = IntegerField(column_name="duration")  #длительность сообщения (аудио или видео)
    message_table_format = TextField(column_name="format")  # формат сообщения

class TelegaVideo(BaseModel):
    message_table_type = TextField(column_name="message_type")  #тип сообщения
    message_table_content = TextField(column_name="content")  #содержимое сообщения
    message_table_recipient = TextField(column_name="recipient")  #имя получателя
    message_table_date = DateTimeField(column_name="time")  #дата отправки
    message_table_duration = IntegerField(column_name="duration")  #длительность сообщения (аудио или видео)
    message_table_quality = TextField(column_name="quality")  #качество сообщения (видео)
    message_table_format = TextField(column_name="format")  # формат сообщения


class basic_text_message(TelegaText):
    def __init__(self, content, recipient, time, message_type='text') -> None:
        super().__init__(
            message_table_type=message_type,
            message_table_content=content,
            message_table_recipient=recipient,
            message_table_date=time,
        )


class basic_audio_message(TelegaAudio):
    def __init__(self, content, recipient, time, duration, message_type, format) -> None:
        super().__init__(
            message_table_type=message_type,
            message_table_content=content,
            message_table_recipient=recipient,
            message_table_date=time,
            message_table_duration=duration,
            message_table_format=format)


class basic_video_message(TelegaVideo):
    def __init__(self, content, recipient, time, duration, message_type, quality, format) -> None:
        super().__init__(
            message_table_type=message_type,
            message_table_content=content,
            message_table_recipient=recipient,
            message_table_date=time,
            message_table_duration=duration,
            message_table_quality=quality,
            message_table_format=format

        )
