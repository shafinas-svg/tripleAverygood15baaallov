# Класс "Фильм" с атрибутами: идентификатор, название, жанры, режиссер, год выпуска, рейтинг
class Film:
    def __init__(self, identifier, name, genres, director, year, rating):
        self.identifier = identifier 
        self.name = name
        self.genres = genres  
        self.director = director
        self.year = year
        self.rating = rating
    
    def __str__(self):
        return f"{self.name} ({self.year}), реж. {self.director}, рейтинг: {self.rating}"
        
# Класс "Пользователь" с атрибутами: идентификатор, имя, список просмотренных фильмов с оценками, предпочтительные жанры
class User:
    def __init__(self, identifier, name):
        self.identifier = identifier
        self.name = name
        self.watched_films = {}  
        self.preferred_genres = []
    
    def add_rating(self, film_id, rating):
        """Добавить оценку фильму с валидацией"""
        if 1 <= rating <= 10:
            self.watched_films[film_id] = rating
            return True
        return False
    
    def add_preferred_genre(self, genre):
        """Добавить предпочтительный жанр"""
        if genre not in self.preferred_genres:
            self.preferred_genres.append(genre)
    
    def get_average_rating(self):
        """Получить среднюю оценку пользователя"""
        if not self.watched_films:
            return 0
        return sum(self.watched_films.values()) / len(self.watched_films)
    
    def __str__(self):
        return f"Пользователь: {self.name} (ID: {self.identifier}), оценок: {len(self.watched_films)}"


# Перечисление "Жанры" с основными кино-жанрами
from enum import Enum
class Genre(Enum):
    ACTION = "Боевик"
    COMEDY = "Комедия"
    DRAMA = "Драма"
    THRILLER = "Триллер"
    HORROR = "Ужасы"
    SCI_FI = "Фантастика"
    FANTASY = "Фэнтези"
    ROMANCE = "Романтика"
    ANIMATION = "Анимация"
    ADVENTURE = "Приключения"

# - Реализовать менеджер данных для хранения фильмов и пользователей

class DataManager:
    def __init__(self):
        self.films = {}
        self.users = {}
    
    def add_film(self, film):
        # Добавить фильм
        self.films[film.identifier] = film
    
    def add_user(self, user):
        # Добавить пользователя
        self.users[user.identifier] = user
    
    def get_film(self, film_id):
        # Получить фильм по ID
        return self.films.get(film_id)
    
    def get_user(self, user_id):
        # Получить пользователя по ID
        return self.users.get(user_id)
    
    def add_rating(self, user_id, film_id, rating):
        # Добавить оценку фильма пользователем
        user = self.get_user(user_id)
        film = self.get_film(film_id)
        
        if user and film:
            return user.add_rating(film_id, rating)
        return False

#Создать систему загрузки тестовых данных (20-30 фильмов)
def load_test_data(data_manager):
    # Создаем тестовые фильмы
    films_data = [
        (1, "Побег из Шоушенка", [Genre.DRAMA], "Фрэнк Дарабонт", 1994, 9.3),
        (2, "Начало", [Genre.SCI_FI, Genre.ACTION], "Кристофер Нолан", 2010, 8.8),
        (3, "Криминальное чтиво", [Genre.CRIME, Genre.DRAMA], "Квентин Тарантино", 1994, 8.9),
        (4, "Темный рыцарь", [Genre.ACTION, Genre.DRAMA], "Кристофер Нолан", 2008, 9.0),
        (5, "Форрест Гамп", [Genre.DRAMA, Genre.ROMANCE], "Роберт Земекис", 1994, 8.8),
        (6, "Зеленая миля", [Genre.DRAMA, Genre.FANTASY], "Фрэнк Дарабонт", 1999, 8.6),
        (7, "Интерстеллар", [Genre.SCI_FI], "Кристофер Нолан", 2014, 8.6),
        (8, "Леон", [Genre.ACTION, Genre.DRAMA], "Люк Бессон", 1994, 8.5),
        (9, "Бойцовский клуб", [Genre.DRAMA], "Дэвид Финчер", 1999, 8.8),
        (10, "Король Лев", [Genre.ANIMATION, Genre.DRAMA], "Роджер Аллерс", 1994, 8.5),
        (11, "Матрица", [Genre.SCI_FI, Genre.ACTION], "Лана Вачовски", 1999, 8.7),
        (12, "Список Шиндлера", [Genre.DRAMA], "Стивен Спилберг", 1993, 8.9),
        (13, "Властелин колец", [Genre.FANTASY], "Питер Джексон", 2001, 8.8),
        (14, "Титаник", [Genre.DRAMA, Genre.ROMANCE], "Джеймс Кэмерон", 1997, 7.9),
        (15, "Остров проклятых", [Genre.THRILLER], "Мартин Скорсезе", 2010, 8.2),
        (16, "Гладиатор", [Genre.ACTION], "Ридли Скотт", 2000, 8.5),
        (17, "Джокер", [Genre.DRAMA], "Тодд Филлипс", 2019, 8.4),
        (18, "Паразиты", [Genre.DRAMA, Genre.THRILLER], "Пон Чжун Хо", 2019, 8.6),
        (19, "Довод", [Genre.SCI_FI, Genre.ACTION], "Кристофер Нолан", 2020, 7.4),
        (20, "Мгла", [Genre.HORROR], "Фрэнк Дарабонт", 2007, 7.1),
        (21, "Игра в имитацию", [Genre.DRAMA], "Мортен Тильдум", 2014, 8.0)
    ]
    
    for data in films_data:
        film = Film(*data)
        data_manager.films[film.identifier] = film
    
    # Создаем тестовых пользователей
    users_data = [
        (1, "Амир"),
        (2, "Афина"),
        (3, "Артем")
    ]
    
    for data in users_data:
        user = User(*data)
        data_manager.add_user(user)
    
    # Добавим предпочтительные жанры и оценки для демонстрации
    data_manager.users[1].add_preferred_genre(Genre.ACTION)
    data_manager.users[1].add_preferred_genre(Genre.SCI_FI)
    data_manager.add_rating(1, 2, 9)  # Амир оценил "Начало" на 9
    data_manager.add_rating(1, 11, 10)  # Амир оценил "Матрица" на 10
    data_manager.users[2].add_preferred_genre(Genre.DRAMA)
    data_manager.users[2].add_preferred_genre(Genre.ROMANCE)
    data_manager.add_rating(2, 5, 8)  # Афина оценила "Форрест Гамп" на 8
    data_manager.add_rating(2, 14, 9)  # Афина оценила "Титаник" на 9


# Организовать возможность добавления пользователей и записи их оценок фильмов

def add_user(data_manager, name):
    new_id = max(data_manager.users.keys()) + 1 if data_manager.users else 1
    user = User(new_id, name)
    data_manager.users[new_id] = user
    return user

def add_film_rating(data_manager, user_id, film_id, rating):
    if user_id in data_manager.users and film_id in data_manager.films:
        user = data_manager.users[user_id]
        user.watched_films[film_id] = rating
        return True
    return False


from abc import ABC, abstractmethod

class RecommendationStrategy(ABC):
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.users = data_manager.users
        self.films = data_manager.films
    @abstractmethod
    def recommend(self, user):
        pass

class recomend_by_rating(RecommendationStrategy):
    def __init__(self, data_manager):
        super().__init__(data_manager)
        self.users = data_manager.users
        self.films = data_manager.films

    def recommend(self, user):
        if not user.watched_films:
            return []

        avr_rating = 0
        count = 0
        for rate in user.watched_films.values():
            avr_rating += rate
            count += 1
        avr_rating /= count

        result = []

        for film_id, film in self.data_manager.films.items():
            if film_id in user.watched_films:
                continue

            ratings = []
            for other_user in self.data_manager.users.values():
                if film_id in other_user.watched_films:
                    ratings.append(other_user.watched_films[film_id])

            if ratings and (sum(ratings) / len(ratings)) >= avr_rating:
                result.append(film_id)

        return result

class recomend_by_genre(RecommendationStrategy):
    def __init__(self, data_manager):
        super().__init__(data_manager)
        self.users = data_manager.users
        self.films = data_manager.films

    def recommend(self, user):  # Измените recommend_by_genre на recommend
        if not user.preferred_genres:
            return []

        result = []

        for film_id, film in self.data_manager.films.items():
            if film_id in user.watched_films:
                continue

            for genre in film.genres:
                if genre in user.preferred_genres:
                    result.append(film_id)
                    break

        return result


class recomend_by_same_users(RecommendationStrategy):
    def __init__(self, data_manager):
        super().__init__(data_manager)
        self.users = data_manager.users
        self.films = data_manager.films

    def recommend(self, user):
        if not user.watched_films:
            return []
        result = []

        similar_users = []
        for other_id, other_user in self.users.items():
            if other_id == user.identifier:
                continue

            common_films = 0
            for film_id, rating in user.watched_films.items():
                if film_id in other_user.watched_films:
                    if abs(rating - other_user.watched_films[film_id]) <= 2:
                        common_films += 1

            if common_films > 0:
                similar_users.append(other_user)

        for similar_user in similar_users:
            for film_id, rating in similar_user.watched_films.items():
                if film_id not in user.watched_films and film_id not in result:
                    if rating >= 7:
                        result.append(film_id)

        return result

def choose_mode():
    print("1 - по рейтингу")
    print("2 - по жанру")
    print("3 - по похожим пользователям")
    choice = input("выбери: ")
    return choice


def get_rec(data_manager, user):
    choice = choose_mode()

    if choice == "1":
        s = recomend_by_rating(data_manager)
        film_ids = s.recommend(user)
        films = []
        for film_id in film_ids:
            film = data_manager.get_film(film_id)
            if film:
                films.append(film)
        return films, "по рейтингу"

    if choice == "2":
        s = recomend_by_genre(data_manager)
        film_ids = s.recommend(user)
        films = []
        for film_id in film_ids:
            film = data_manager.get_film(film_id)
            if film:
                films.append(film)
        return films, "по жанру"

    if choice == "3":
        s = recomend_by_same_users(data_manager)
        film_ids = s.recommend(user)
        films = []
        for film_id in film_ids:
            film = data_manager.get_film(film_id)
            if film:
                films.append(film)
        return films, "по похожим"

    return [], "не выбрано"

def input_int_or_none(prompt, min_v=None, max_v=None):
    """Ввод целого числа или пустой строки -> None."""
    while True:
        s = input(prompt).strip()
        if s == "":
            return None
        try:
            v = int(s)
            if (min_v is not None and v < min_v) or (max_v is not None and v > max_v):
                print(f"Введите число в диапазоне [{min_v}, {max_v}] или Enter для пропуска.")
                continue
            return v
        except ValueError:
            print("Неверный ввод. Введите целое число или нажмите Enter.")

def register_cli(data_manager):
    name = input("Введите имя для регистрации: ").strip()
    if not name:
        print("Имя не может быть пустым.")
        return None
    user = add_user(data_manager, name)
    print(f"Пользователь зарегистрирован: {user.name} (ID {user.identifier})")
    return user

def login_cli(data_manager):
    if not data_manager.users:
        print("Нет пользователей. Сначала зарегистрируйтесь.")
        return None
    print("Список пользователей:")
    for uid, u in data_manager.users.items():
        print(f"{uid}: {u.name} (оценок: {len(u.watched_films)})")
    uid = input_int_or_none("Введите ID пользователя для входа (или Enter): ")
    if uid is None:
        return None
    user = data_manager.get_user(uid)
    if not user:
        print("Пользователь с таким ID не найден.")
        return None
    print(f"Вход выполнен: {user.name}")
    return user

def show_all_films_cli(data_manager, only_unwatched_by=None):
    print("\n--- Фильмы в базе ---")
    for film_id, film in data_manager.films.items():
        if only_unwatched_by and film_id in only_unwatched_by.watched_films:
            continue
        print(f"{film_id}. {film.name} ({film.year}) — реж. {film.director}, рейтинг: {film.rating}")

def view_film_details_cli(data_manager):
    fid = input_int_or_none("Введите ID фильма для просмотра (или Enter): ")
    if fid is None:
        return
    film = data_manager.get_film(fid)
    if not film:
        print("Фильм не найден.")
        return
    genres = ", ".join([g.value for g in film.genres])
    print(f"\n{film.name} ({film.year})")
    print(f"Режиссер: {film.director}")
    print(f"Жанры: {genres}")
    print(f"Рейтинг: {film.rating}\n")

def rate_film_cli(data_manager, user):
    show_all_films_cli(data_manager)
    fid = input_int_or_none("Введите ID фильма, который хотите оценить (или Enter): ")
    if fid is None:
        return
    if fid not in data_manager.films:
        print("Фильм не найден.")
        return
    rating = input_int_or_none("Введите оценку (1-10): ", 1, 10)
    if rating is None:
        print("Оценка не введена.")
        return
    ok = add_film_rating(data_manager, user.identifier, fid, rating)
    if ok:
        print(f"Оценка сохранена: {data_manager.get_film(fid).name} -> {rating}")
    else:
        print("Не удалось сохранить оценку.")

def set_preferences_cli(user):
    all_genres = list(Genre)
    print("Доступные жанры:")
    for i, g in enumerate(all_genres, start=1):
        print(f"{i} - {g.value}")
    s = input("Введите номера жанров через запятую для добавления в предпочтения (или Enter): ").strip()
    if not s:
        return
    parts = [p.strip() for p in s.split(",")]
    added = 0
    for p in parts:
        if not p.isdigit():
            continue
        idx = int(p)
        if 1 <= idx <= len(all_genres):
            user.add_preferred_genre(all_genres[idx-1])
            added += 1
    print(f"Добавлено предпочтительных жанров: {added}")
    print("Текущие предпочтения:", ", ".join([g.value for g in user.preferred_genres]) or "нет")

def remove_preferences_cli(user):
    if not user.preferred_genres:
        print("У вас нет предпочтений.")
        return
    print("Текущие предпочтения:")
    for i, g in enumerate(user.preferred_genres, start=1):
        print(f"{i} - {g.value}")
    s = input("Введите номера жанров для удаления через запятую (или Enter): ").strip()
    if not s:
        return
    parts = [p.strip() for p in s.split(",")]
    removed = 0

    to_remove = []
    for p in parts:
        if not p.isdigit():
            continue
        idx = int(p)
        if 1 <= idx <= len(user.preferred_genres):
            to_remove.append(user.preferred_genres[idx-1])
    for g in to_remove:
        if g in user.preferred_genres:
            user.preferred_genres.remove(g)
            removed += 1
    print(f"Удалено: {removed}")
    print("Оставшиеся предпочтения:", ", ".join([g.value for g in user.preferred_genres]) or "нет")

def get_recommendations_cli(data_manager, user):

    print("Выбор стратегии рекомендаций:")
    print("1 - по рейтингу")
    print("2 - по жанру")
    print("3 - по похожим пользователям")
    mode = choose_mode()

    films, label = get_rec(data_manager, user)
    if not films:
        print("Рекомендаций не найдено по выбранной стратегии.")
        return


    print("Фильтрация рекомендаций (нажмите Enter чтобы пропустить):")
    min_rating = input("Минимальный рейтинг (например 8.0): ").strip()
    min_year = input("Минимальный год выпуска (например 2000): ").strip()
    try:
        min_rating_val = float(min_rating) if min_rating else None
    except ValueError:
        min_rating_val = None
    try:
        min_year_val = int(min_year) if min_year else None
    except ValueError:
        min_year_val = None

    filtered = []
    for f in films:
        if min_rating_val is not None and getattr(f, "rating", 0) < min_rating_val:
            continue
        if min_year_val is not None and getattr(f, "year", 0) < min_year_val:
            continue
        filtered.append(f)

    if not filtered:
        print("Нет фильмов, удовлетворяющих фильтрам.")
        return

    print(f"\nРекомендации ({label}):")
    for f in filtered:
        genres = ", ".join(g.value for g in f.genres)
        print(f"{f.identifier}. {f.name} ({f.year}) — реж. {f.director}, жанры: {genres}, рейтинг: {f.rating}")

def show_current_user(user):
    if not user:
        print("Пользователь не выбран.")
        return
    print(user)
    print("Предпочтения:", ", ".join([g.value for g in user.preferred_genres]) or "нет")
    print("Просмотренные фильмы и оценки:")
    if not user.watched_films:
        print("  нет")
    else:
        for fid, score in user.watched_films.items():
            print(f"  ID {fid} -> оценка {score}")

def main_cli():
    dm = DataManager()
    load_test_data(dm)
    current_user = None
    print("Тестовые данные загружены.")
    while True:
        print("\n=== Меню системы рекомендаций ===")
        print("1 - Регистрация")
        print("2 - Вход")
        print("3 - Просмотреть все фильмы")
        print("4 - Просмотреть детали фильма")
        print("5 - Оценить фильм (нужно войти)")
        print("6 - Настройка предпочтений (нужно войти)")
        print("7 - Удалить предпочтения (нужно войти)")
        print("8 - Получить рекомендации (нужно войти)")
        print("9 - Показать текущего пользователя")
        print("0 - Выход")
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            current_user = register_cli(dm)
        elif choice == "2":
            current_user = login_cli(dm)
        elif choice == "3":
            show_all_films_cli(dm)
        elif choice == "4":
            view_film_details_cli(dm)
        elif choice == "5":
            if not current_user:
                print("Сначала войдите в систему.")
            else:
                rate_film_cli(dm, current_user)
        elif choice == "6":
            if not current_user:
                print("Сначала войдите в систему.")
            else:
                set_preferences_cli(current_user)
        elif choice == "7":
            if not current_user:
                print("Сначала войдите в систему.")
            else:
                remove_preferences_cli(current_user)
        elif choice == "8":
            if not current_user:
                print("Сначала войдите в систему.")
            else:
                get_recommendations_cli(dm, current_user)
        elif choice == "9":
            show_current_user(current_user)
        elif choice == "0":
            print("Выход. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main_cli()


