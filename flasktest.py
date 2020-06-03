#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask
from flask import request

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)


@app.route("/")
def my_main():
   return "Seasonal information is avaliable at /inseason"
# in season ask for fruit

@app.route("/inseason")

def season():
    if request.args.get("fruit"):
        fruitq = request.arg.get("fruit")
    else:
        return "Please supply a 'fruit'"
    if fruitq =="strawberries":
        return "Yes, strawberries are in season"
    elif fruitq == "pumpkins":
        return "NO, pumpkins are not in season"
    elif fruitq == "purnes":
        return "oh I see what issue you have. yes prunes are in season"
    else:
        return "This Item is not in our inventory"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) 
