from Message import *

class VideoFormat(enum.Enum):
    MP4 = "Стандартный формат MP4"
    AVI = "Улучшенный формат AVI"
    ANIME = "Аниме формат ANIME"

class VideoQuality(enum.Enum):
    LOW = "Качество видео 144"
    MIDDLE = "Качество видео 360"
    GOOD = "Качество видео 720"
    PERFECT = "Качество видео 1080"

class VideoMessage(Message):
    def __init__(self) -> None:
        super().__init__()
        self.__duration: int = None # длительность видео
        self.__format: str = None # формат видео
        self.__quality: str = None # качество видео 

    def set_duration(self,seconds:int)->int:
        self.__duration = seconds
    
    def get_duration(self):
        return self.__duration

    def set_format(self,video:int)-> None:
        if video == "mp4":
            format = VideoFormat.MP4.value
        elif video == "avi":
            format = VideoFormat.AVI.value
        elif video == "anime":
            format = VideoFormat.ANIME.value
        self.__format = format

    def get_format(self):
        return self.__format
    
    def set_quality(self,pixels):
        if pixels == 144:
            quality = VideoQuality.LOW.value
        elif pixels == 360:
            quality = VideoQuality.MIDDLE.value
        elif pixels == 720:
            quality = VideoQuality.GOOD.value
        elif pixels == 1080:
            quality = VideoQuality.PERFECT.value
        self.__quality = quality
    
    def get_quality(self):
        return self.__quality
    
    def set_message_parameters() -> "VideoMessage":
        message = VideoMessage()
        content = input("Тут вы можете ввести свое сообщение,но не хулиганьте!")
        message.set_content(content)
        user_name = input("Кому отправляем сообщение ? ")
        message.set_recipient(user_name)
        time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        message.set_time(time)
        try:
            duration = int(input("Введите продолжительность видеосообщения 0-60 секунд"))
            if 0 < duration > 60:
                print("Установлена стандартная длительность видео (30 сек)")
                duration = 30
                message.set_duration(duration)
            else:
                message.set_duration(duration)
        except ValueError:
            print("Что-то пошло не так,установлена стандартная длительность видео (30 сек)")
            duration = 30
            message.set_duration(duration)
        try:
            format = input("Какого формата записываем видео?\nMP4\nAVI\nANIME").lower()
            if format == "mp4" or format == "avi" or format == "anime":
                message.set_format(format)
            else:
                print("Установлен стандартный формат")
                format = "mp4"
                message.set_format(format)
        except ValueError:
            print("Что-то пошло не так,установлен стандартный формат видео")
            format = "mp4"
            message.set_format(format)
        
        try:
            quality = int(input("В каком качестве записываем видео?\n Низкое качество (144)\n Среднее качество (360)\n Хорошее качество(720)\n Отличное качество (1080)"))
            if quality == 144 or quality == 360 or quality == 720 or quality == 1080:
                message.set_quality(quality)
            else:
                print("Автоматически установлено среднее качество")
                quality = 360
                message.set_quality(quality)
        except ValueError:
            print("Что-то пошло не так,установлен стандартное качество")
            quality = 360
            message.set_quality(quality)
        
        new_record_table = BasicVideoMessage(content,user_name,time,duration,message.get_format(),message.get_quality())
        new_record_table.save()
        return message

    def __repr__(self):
        VideoMessage = type(self).__name__
        return f"{VideoMessage}({self.get_id()!r},{self.get_content()!r},{self.get_recipient()!r},{self.get_time()!r},{self.get_duration()!r},{self.get_format()!r},{self.get_quality()!r})"

    def __str__(self):
        return f"ID вашего сообщения:{self.get_id()} Ваше сообщение: {self.get_content()} Получатель: {self.get_recipient()} Время отправки {self.get_time()} Длительность : {self.get_duration()} Формат аудио: {self.get_format()} Качество видео: {self.get_quality()}"
