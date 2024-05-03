from Message import *


class AudioFormat(enum.Enum):
    MP3 = "Стандартный формат МР3"
    AMV = "Улучшенный формат AMV"
    AUF = "Пацанский формат AUF"


class AudioMessage(Message):
    def __init__(self) -> None:
        super().__init__()
        self.__duration: int = None  # длительность аудио
        self.__format: str = None  # формат аудио

    def set_duration(self, seconds: int) -> int:
        self.__duration = seconds

    def get_duration(self):
        return self.__duration

    def set_format(self, audio: str) -> None:
        match audio:
            case "mp3":
                self.__format = AudioFormat.MP3.value
            case "amv":
                self.__format = AudioFormat.AMV.value
            case "auf":
                self.__format = AudioFormat.AUF.value
            case _:
                self.__format = AudioFormat.MP3.value

    def get_format(self):
        return self.__format

    def set_message_parameters(self) -> "AudioMessage":
        message = AudioMessage()
        content = input("Тут вы можете ввести свое сообщение,но не хулиганьте!")
        message.set_content(content)
        user_name = input("Кому отправляем сообщение ? ")
        message.set_recipient(user_name)
        time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        message.set_time(time)
        try:
            duration = int(input("Введите продолжительность аудиосообщения 0-120 секунд"))
            if 0 < duration > 120:
                print("Установлена стандартная длительность аудио (30 сек)")
                duration = 30
                message.set_duration(duration)
            else:
                message.set_duration(duration)
        except ValueError:
            print("Что-то пошло не так,установлена стандартная длительность аудио (30 сек)")
            duration = 30
            message.set_duration(duration)
        try:
            format = input("Какого формата записываем аудио?\nMP3\nAMV\nAUF").lower()
            if format == "mp3" or format == "amv" or format == "auf":
                message.set_format(format)
            else:
                print("Установлен стандартный формат")
                format = "mp3"
                message.set_format(format)
        except ValueError:
            print("Что-то пошло не так,установлен стандартный формат аудио")
            format = "mp3"
            message.set_format(format)

        new_record_table = basic_audio_message(content, user_name, time, duration, "Audio Message", format)
        new_record_table.save()
        return message

    def __repr__(self):
        AudioMessage = type(self).__name__
        return f"{AudioMessage}({self.get_content()!r},{self.get_recipient()!r},{self.get_time()!r},{self.get_duration()!r},{self.get_format()!r})"

    def __str__(self):
        return f"Ваше сообщение: {self.get_content()} Получатель: {self.get_recipient()} Время отправки {self.get_time()} Длительность : {self.get_duration()} Формат аудио: {self.get_format}"
