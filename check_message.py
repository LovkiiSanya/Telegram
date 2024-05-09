import psycopg2


conn = psycopg2.connect(
    dbname="postgres",
    host="127.0.0.1", user="admin", password="root"
                                )


cur = conn.cursor()


cur.execute("SELECT content,recipient,time,message_type FROM basic_text_message")
text_message_columns = cur.fetchall()
for column in text_message_columns:
    content, recipient, time, message_type = column
import_text_column = text_message_columns

cur.execute("SELECT content, recipient, time, message_type,duration, format FROM basic_audio_message")
audio_message_columns = cur.fetchall()

for column in audio_message_columns:
    content, recipient, time, message_type, duration, format = column
import_audio_column = audio_message_columns

cur.execute("SELECT content, recipient, time, message_type,duration, format,quality FROM basic_video_message")
video_message_columns = cur.fetchall()

for column in video_message_columns:
    content, recipient, time, message_type, duration, format, quality = column
import_video_column = video_message_columns

cur.close()
conn.close()
