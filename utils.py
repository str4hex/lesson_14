# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание


import sqlite3
from collections import Counter


class BaseNeflixDAO:

    def __init__(self, path_base):
        self.path_base = path_base

    def load_connect(self):
        with sqlite3.connect(self.path_base) as connection:
            cursor = connection.cursor()
        return cursor

    def search_film(self, film_name):
        cursor = self.load_connect()
        sqlite_query = (
            f"SELECT title, country,release_year,listed_in,description FROM netflix WHERE title = '{film_name}' ORDER BY release_year DESC LIMIT 1 ")

        cursor.execute(sqlite_query)
        result = cursor.fetchall()

        result_search = {
            "title": result[0][0],
            "country": result[0][1],
            "release_year": result[0][2],
            "genre": result[0][3],
            "description": result[0][4]
        }

        return result_search

    def search_date_movie(self, year, toyear):
        cursor = self.load_connect()
        sqlite_query = (
            f"SELECT title,release_year FROM netflix WHERE release_year BETWEEN {year} AND {toyear} LIMIT 100")

        cursor.execute(sqlite_query)
        executed_query = cursor.fetchall()
        result = []
        for querys in range(len(executed_query)):
            result.append({
                "title": executed_query[querys][0],
                "release_year": executed_query[querys][1]
            })
        return result

    def search_rating_children(self):
        result = []
        cursor = self.load_connect()
        sqlite_query = f"SELECT title, rating, description FROM netflix WHERE rating = 'G'"
        cursor.execute(sqlite_query)
        executed_query = cursor.fetchall()
        for querys in range(len(executed_query)):
            result.append({
                "title": executed_query[querys][0],
                "rating": executed_query[querys][1],
                "description": executed_query[querys][2]
            })
        return result

    def search_rating_family(self):
        result = []
        cursor = self.load_connect()
        sqlite_query = f"SELECT title, rating, description FROM netflix WHERE rating = 'G' OR rating='PG' OR rating='PG-13'"  # (G, PG, PG-13)
        cursor.execute(sqlite_query)
        executed_query = cursor.fetchall()
        for querys in range(len(executed_query)):
            result.append({
                "title": executed_query[querys][0],
                "rating": executed_query[querys][1],
                "description": executed_query[querys][2]
            })
        return result

    def search_rating_adult(self, ):
        result = []
        cursor = self.load_connect()
        sqlite_query = f"SELECT title, rating, description FROM netflix WHERE rating = 'R' OR rating = 'NC-17'"  # (R, NC-17)
        cursor.execute(sqlite_query)
        executed_query = cursor.fetchall()
        for querys in range(len(executed_query)):
            result.append({
                "title": executed_query[querys][0],
                "rating": executed_query[querys][1],
                "description": executed_query[querys][2]
            })
        return result

    def search_rating_genre(self, genres):
        result = []
        cursor = self.load_connect()
        sqlite_query = f"SELECT title,description FROM netflix WHERE listed_in LIKE '%{genres}%' ORDER BY listed_in DESC LIMIT 10"
        cursor.execute(sqlite_query)
        executed_query = cursor.fetchall()
        for querys in range(len(executed_query)):
            result.append({
                "title": executed_query[querys][0],
                "description": executed_query[querys][1]
            })
        return result

    def name_cast(self, name_director_1, name_director_2):
        cursor = self.load_connect()
        sqlite_query = f"SELECT netflix.cast FROM netflix  WHERE  netflix.cast LIKE '%{name_director_1}%' OR '%{name_director_2}%'"
        cursor.execute(sqlite_query)
        executed_query = cursor.fetchall()

        result_case = []
        result_count_case = []
        result_total = []

        for list in range(len(executed_query)):
            for list_one in executed_query[list][0].split(", "):
                load_list = list_one
                result_case.append(load_list)
        result_count_case.append(Counter(result_case))

        for name, score in result_count_case[0].items():
            if score > 1:
                result_total.append(name)
        result_total.remove(name_director_1)
        result_total.remove(name_director_2)
        return result_total

    def get_by_type_movie(self, types, release, gengre):
        cursor = self.load_connect()
        sqlite_query = f"SELECT title,description FROM netflix WHERE type = '{types}' AND release_year = '{release}' " \
                       f"AND listed_in LIKE '%{gengre}%'"
        cursor.execute(sqlite_query)
        executed_query = cursor.fetchall()
        result = []
        for query in executed_query:
            result.append({"title": query[0],
                           "description": query[1]})
        return result


basenetflix = BaseNeflixDAO("netflix.db")
result_name_cast = basenetflix.name_cast("Rose McIver", "Ben Lamb")

basenetflix = BaseNeflixDAO("netflix.db")
result_type_movie = basenetflix.get_by_type_movie("TV Show", 2005, "Dramas")

print(result_name_cast)
print(result_type_movie)
