from flask import Flask, jsonify

from utils import BaseNeflixDAO

app = Flask(__name__)


@app.route("/movie/<title>")
def movie_title_page(title):
    basenetflix = BaseNeflixDAO("netflix.db")
    films = basenetflix.search_film(title)
    return jsonify(films)


@app.route("/movie/<int:year>/to/<int:toyear>")
def movie_year_page(year, toyear):
    basenetflix = BaseNeflixDAO("netflix.db")
    result = basenetflix.search_date_movie(year, toyear)
    return jsonify(result)


@app.route("/rating/children")
def rating_children():
    basenetflix = BaseNeflixDAO("netflix.db")
    result = basenetflix.search_rating_children()
    return jsonify(result)


@app.route("/rating/family")
def rating_family():
    basenetflix = BaseNeflixDAO("netflix.db")
    result = basenetflix.search_rating_family()
    return jsonify(result)


@app.route("/rating/adult")
def rating_adult():
    basenetflix = BaseNeflixDAO("netflix.db")
    result = basenetflix.search_rating_adult()
    return jsonify(result)


@app.route("/genre/<genre>")
def rating_genre(genre):
    basenetflix = BaseNeflixDAO("netflix.db")
    result = basenetflix.search_rating_genre(genre)
    return jsonify(result)


if __name__ == '__main__':
    app.run()
