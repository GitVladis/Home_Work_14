import json
import sqlite3
import pprint

DB_PATH = "netflix.db"


def get_movie_by_title(title):

    con = sqlite3.connect(DB_PATH)

    sqlite_query = "SELECT 'title', 'country', 'release_year', 'listed_in', 'description' " \
                   "FROM netflix " \
                   f"WHERE title = '{title}' " \
                   "ORDER BY 'release_year' " \
                   "LIMIT 1"

    cur = con.cursor()
    cur.execute(sqlite_query)
    data_raw = cur.fetchone()

    data = {
        "title": data_raw[0],
        "country": data_raw[1],
        "release_year": data_raw[2],
        "genre": data_raw[3],
        "description": data_raw[4]
    }

    con.close()

    return data

def get_movies_between_years(year1, year2):

    con = sqlite3.connect(DB_PATH)

    sqlite_query = "SELECT 'title', 'country', 'release_year', 'listed_in', 'description' " \
                    "FROM netflix " \
                    f"WHERE 'release_year' BETWEEN {year1} AND {year2} " \
                    "LIMIT 100"

    cur = con.cursor()
    cur.execute(sqlite_query)
    data = []

    for row in cur.fetchall():

        movie = {
            "title": row[0],
            "country": row[1],
            "release_year": row[2],
            "genre": row[3],
            "description": row[4]
        }

        data.append(movie)

    return data

pprint.pprint(get_movies_between_years(2020, 2021))




def get_movies_by_genre(genre):

    pass


def get_movies_rating(rating):

    pass


def get_actors_company(first, second):

    con = sqlite3.connect(DB_PATH)

    sqlite_query = "SELECT GROUP_CONTACT('cast', ",") as cast" \
                    "FROM netflix " \
                    f"WHERE 'cast' LIKE '%{first}%' AND 'cast' LIKE '%{second}%' "

    cur = con.cursor()
    cur.execute(sqlite_query)
    data_raw = cur.fetchone()
    actors_list = data_raw[0].split(", ")
    actors_list_unique = set(actors_list)

    actors_list_unique.remove(first)
    actors_list_unique.remove(second)

    return actors_list_unique


def filter_movies(movie_type, year, genre):

    pass