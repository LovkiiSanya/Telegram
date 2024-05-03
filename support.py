from Message import *
from AudioMessage import *
from VideoMessage import *
from create_db import *


def CRUDoperations():
    CRUDoperation = int(input("Для создания и отправки сообщения нажмите: (1) \nДля редактирования (текстовых) "
                              "сообщений нажмите: (2) \nДля просмотра архива сообщений нажмите: (3)\nДля удалений "
                              "сообщений нажмите(4)"))
    if CRUDoperation == 1:
        create_message()
    elif CRUDoperation == 2:
        change_message()
    elif CRUDoperation == 3:
        check_message()
    elif CRUDoperation == 4:
        delete_message()


def delete_message():
    delete_message_table = input("Удалить можно любое сообщение,нужно только выбрать его формат и айди: \nAUDIO\n"
                                 "VIDEO\n"
                                 "TEXT\n").lower()
    match delete_message_table:
        case "audio":
            audio_delete_message = int(input("Отлично,удаляем аудиосообщение,осталось ввести его id: "))
            is_id_exists = basic_audio_message.select().where(basic_audio_message.id == audio_delete_message).exists()
            if is_id_exists:
                basic_audio_message.delete_by_id(audio_delete_message)
            else:
                print("Такого id нет в базе")
        case "video":
            video_delete_message = int(input("Отлично,удаляем видеосообщение,осталось ввести его id: "))
            is_id_exists = basic_video_message.select().where(basic_video_message.id == video_delete_message).exists()
            if is_id_exists:
                basic_video_message.delete_by_id(video_delete_message)
            else:
                print("Такого id нет в базе")
        case "text":
            text_delete_message = int(input("Отлично,удаляем текстовое сообщение,осталось ввести его id: "))
            is_id_exists = basic_text_message.select().where(basic_text_message.id == text_delete_message).exists()
            if is_id_exists:
                basic_text_message.delete_by_id(text_delete_message)
            else:
                print("Такого id нет в базе")


def check_message():
    check_message = int(input("Хотите посмотреть весь архив (1) или конкретное сообщение ?(2)"))
    if check_message == 1:
            print(basic_text_message.select())
            print(basic_audio_message.select())
            print(basic_video_message.select())



    elif check_message == 2:
        check_message_id = int(input("Введите нужный айди:"))
        if check_message_id in message_dict:
            print(message_dict.get(check_message_id))
        else:
            print("Ошибка ввода айди")


def change_message():
    change_id = int(input("Для изменений текстовых сообщений надо ввести его айди!"))
    if type(message_dict[change_id]) == Message:
        create_message()
    else:
        print("что-то пошло не так")


def format_message():
    format_message = int(input("Отлично!Собщение будет текстовое (1), Видеосообщение (2) или Аудиосообщение (3)?"))
    if 1 <= format_message <= 3:
        return format_message
    else:
        print("Что-то пошло не так, давайте еще разок")


def create_message(self=None):
    format = format_message()
    if format == 1:
        Message.set_message_parameters(self)
        one_more_message()
    elif format == 2:
        VideoMessage.set_message_parameters(self)
        one_more_message()
    elif format == 3:
        AudioMessage.set_message_parameters(self)
        one_more_message()


def one_more_message():
    one_more_message = input("Хотите создать еще одно сообщение ?(д = да/н = нет)")
    if one_more_message == "д":
        create_message()
    else:
        CRUDoperations()
