import json
import sqlite3

from flask import jsonify


def search_title(title):
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = (f"SELECT title, country,release_year,listed_in,description FROM netflix WHERE title = '{title}' ORDER BY release_year DESC LIMIT 1 ")
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    result = {
        "title": executed_query[0][0],
        "country": executed_query[0][1],
        "release_year": executed_query[0][2],
        "genre": executed_query[0][3],
        "description": executed_query[0][4]
    }
    return jsonify(result)


def search_date(year, toyear):
    result = []
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = (f"SELECT title,release_year FROM netflix WHERE release_year BETWEEN {year} AND {toyear} LIMIT 100")
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    for querys in range(len(executed_query)):
        result.append({
            "title": executed_query[querys][0],
            "release_year": executed_query[querys][1]
        })
    return jsonify(result)


def search_rating_children():
    result=[]
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = f"SELECT title, rating, description FROM netflix WHERE rating = 'G'"
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    for querys in range(len(executed_query)):
        result.append({
        "title": executed_query[querys][0],
        "rating": executed_query[querys][1],
        "description": executed_query[querys][2]
    })
    return jsonify(result)


def search_rating_family():
    result=[]
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = f"SELECT title, rating, description FROM netflix WHERE rating = 'G' OR rating='PG' OR rating='PG-13'" #(G, PG, PG-13)
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    for querys in range(len(executed_query)):
        result.append({
        "title": executed_query[querys][0],
        "rating": executed_query[querys][1],
        "description": executed_query[querys][2]
    })
    return jsonify(result)


def search_rating_adult():
    result=[]
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = f"SELECT title, rating, description FROM netflix WHERE rating = 'R' OR rating = 'NC-17'" #(R, NC-17)
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    for querys in range(len(executed_query)):
        result.append({
        "title": executed_query[querys][0],
        "rating": executed_query[querys][1],
        "description": executed_query[querys][2]
    })
    return jsonify(result)


def search_rating_genre(genres):
    result = []
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = f"SELECT title,description FROM netflix WHERE listed_in LIKE '{genres}%' "
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    print(executed_query)
    for querys in range(len(executed_query)):
        result.append({
            "title": executed_query[querys][0],
            "description": executed_query[querys][1]
        })
    return jsonify(result)


def name_director(name_director_1,name_director_2):
    result = []
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = f"SELECT director FROM netflix  WHERE  director LIKE 'name_director_1%' OR 'name_director_2%'"
    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    print(executed_query)
    pass


name_director("Rose McIver","Ben Lamb")