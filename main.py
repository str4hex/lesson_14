import sqlite3
from utils import search_title, search_date, search_rating_children, search_rating_family, search_rating_adult, \
    search_rating_genre
from flask import Flask

app = Flask(__name__)

con = sqlite3.connect("../netflix.db")
cur = con.cursor()


@app.route("/movie/<title>")
def movie_title_page(title):
    return search_title(title)


@app.route("/movie/<int:year>/to/<int:toyear>")
def movie_year_page(year, toyear):
    return search_date(year, toyear)


@app.route("/rating/children")
def rating_children():
    return search_rating_children()


@app.route("/rating/family")
def rating_family():
    return search_rating_family()


@app.route("/rating/adult")
def rating_adult():
    return search_rating_adult()


@app.route("/genre/<genre>")
def rating_genre(genre):
    return search_rating_genre(genre)


app.run()