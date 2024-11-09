import time


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname            # никнейм
        self.password = hash(password)      # хеш пароля
        self.age = age                      # возраст

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title           # заголовок
        self.duration = duration     # продолжительность
        self.time_now = 0            # время начала
        self.adult_mode = adult_mode # режим для взрослых


class UrTube:
    def __init__(self):
        self.users = []            # список пользователей в системе
        self.videos = []           # список видео в системе
        self.current_user = None   # текущий пользователь

    def register(self, nickname: str, password: str, age: int):       # регистрация нового пользователя
        list_nicknames = []                                           # список никнеймов
        for user in self.users:                                       # проверка наличия уникального никнейма
            list_nicknames.append(user.nickname)                      # добавляем никнеймы в список
        if nickname not in list_nicknames:                            # если такой никнейм уже есть
            user = User(nickname, password, age)                      # создаем нового пользователя
            self.users.append(user)                                   # добавляем нового пользователя в список
            self.log_in(nickname, password)                           # авторизуем нового пользователя
        else:
            print(f'Пользователь {nickname} уже существует')          # выводим сообщение об ошибке

    def log_out(self):                                                # выход из текущего пользователя
        self.current_user = None                                      # сбрасываем текущего пользователя

    def log_in(self, nickname: str, password: str):                   # авторизация пользователя
        for user in self.users:                                       # проверяем авторизацию пользователя
            if user.nickname == nickname and user.password == hash(password): # если авторизация успешна
                self.current_user = user                              # если авторизация успешна, сохраняем пользователя

    def add(self, *videos):                                             # добавление видео в систему
        list_title = []                                               # список добавленных видео
        for video in self.videos:                                            # проверяем наличие видео в системе
            list_title.append(video.title)                             # добавляем заголовки видео в список
        for video in videos:
            if video.title not in list_title:                           # если видео не добавлено ранее
                self.videos.append(video)                                # добавляем видео в систему

    def get_videos(self, search_word: str):                                  # получение списка видео по тексту
        list_titles = []                                                     # список найденных видео
        for video in self.videos:
            if search_word.lower() in video.title.lower():                # если текст совпадает с заголовком видео
                list_titles.append(video.title)                       # добавляем заголовки найденных видео в список
        return list_titles

    def watch_video(self, title: str):                                # смотреть видео
        if self.current_user is None:                                     # если пользователь не авторизован, выводим сообщение
            print('Войдите в аккаунт, чтобы смотреть видео')          # выводим сообщение об ошибке
            return
        for video in self.videos:
            if video.title == title:
                if self.current_user.age >= 18 and video.adult_mode == True:
                    for second in range(1, video.duration + 1):  # если пользователь является взрослым и видео является для взрослых
                        print(second, end=" ")
                        time.sleep(1)
                        video.time_now += 1
                    video.time_now = 0
                    print(' Конец видео')
                else:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')