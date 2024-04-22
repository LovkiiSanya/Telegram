from Message import * 
from AudioMessage import *
from VideoMessage import *
from support import *


def main():
    pass



while True:
    if __name__ == "__main__":
        main()  
    CRUDoperations()
    
    try:
        connection = psycopg2.connect(
        host="127.0.0.1", user="admin", password="root", dbname="postgres"
    )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            print(cursor.fetchone())

        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO telega (message_type) VALUES ('message') """)

    except Exception as _ex:
        print("[INFO] Ошибка при работе с Базой данных", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] Соединение с Базой данных закрыто.")
