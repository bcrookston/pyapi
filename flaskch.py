#!/usr/bin/python3
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

#index
@app.route("/")
def homepage():
    return "Welcome on ths page you can search movies by actor Names"

@app.route("/actor/name")
def return_movies():
    return movie_template("movies.html", actor=name)
    








if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
