#!/usr/bin/python3
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to My Movie Page"

@app.route("/movies/")
def ciscoios():
    try:
        qparms = {}
        # user passes moviename"
        qparms["moviename"]  = request.args.get("moviename", "bootstrapped switch")
        # user passes rating"
        qparms["rating"]  = request.args.get("rating", "10")
        # user passes reviewer
        qparms["reviewer"] = request.args.get("reviewer", "Unknown")
        # user passes comments"
        qparms["comments"] = request.args.get("comments", "N/A")
       

        # render template and save as baseIOS.conf
        return render_template("movies.conf.j2", **qparms)

    except Exception as err:
        return "Uh-oh! " + err

if __name__ == "__main__":
    app.run(host=0.0.0.0, port=2224)

