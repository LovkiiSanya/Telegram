from peewee import *
import psycopg2
try:
    connection = PostgresqlDatabase("postgres",
        host="127.0.0.1", user="admin", password="root"
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        print(cursor.fetchone())

except Exception as _ex:
    print("[INFO] Ошибка при работе с Базой данных", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] Соединение с Базой данных закрыто.")

class BaseModel(Model):
    class Meta:
        database = connection

class TelegaTable(BaseModel):
    message_table_type = TextField(column_name="message_type") #формат сообщения
    message_table_content = TextField(column_name="message_content") #содержимое сообщения
    message_table_recipient = TextField(column_name="message_recipient") #имя получателя
    message_table_date = DateTimeField(column_name="message_date") #дата отправки
    message_table_duration = IntegerField(column_name="message_duration") #длительность сообщения (аудио или видео)
    message_table_quality = TextField(column_name="message_quality") #качество сообщения (видео)
    class Meta:
        table_name = "telega"

class BasicTextMessage(TelegaTable):
    def __init__(self, content, recipient, time, message_type='text') -> None:
        super().__init__(
            message_table_type=message_type,
            message_table_content=content,
            message_table_recipient=recipient,
            message_table_date=time,
        )
        self.save()  # Сохранение записи в базе данных



class BasicAudioMessage(TelegaTable):
    def __init__(self, content, recipient, time,duration, message_type) -> None:
        super().__init__(
            message_table_type=message_type,
            message_table_content=content,
            message_table_recipient=recipient,
            message_table_date=time,
            message_table_duration = duration
        )
        self.save()  # Сохранение записи в базе данных

class BasicVideoMessage(TelegaTable):
    def __init__(self, content, recipient, time,duration, message_type,quality) -> None:
        super().__init__(
            message_table_type=message_type,
            message_table_content=content,
            message_table_recipient=recipient,
            message_table_date=time,
            message_table_duration = duration,
            message_table_quality = quality

        )
        self.save()  # Сохранение записи в базе данных
