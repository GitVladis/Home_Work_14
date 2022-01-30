from flask import Flask, request, render_template, jsonify
from utils import get_movie_by_title

app = Flask(__name__)

@app.route('/movies/<title>')
def page_index(title):
    movie = get_movie_by_title(title)
    return jsonify(movie)

app.run()
