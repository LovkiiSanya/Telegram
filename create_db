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
    #id_message = IntegerField(column_name="id") 
    message_table_type = TextField(column_name="message_type") #формат сообщения
    message_table_content = TextField(column_name="message_content") #содержимое сообщения
    message_table_recipient = TextField(column_name="message_recipient") #имя получателя
    message_table_date = TimeField(column_name="message_date") #дата отправки
    message_table_duration = IntegerField(column_name="message_duration") #длительность сообщения (аудио или видео)
    message_table_quality = TextField(column_name="message_quality") #качество сообщения (видео)
    class Meta:
        table_name = "telega"
