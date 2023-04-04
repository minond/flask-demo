import os
import time
import flask

app = flask.Flask(__name__)

@app.route("/")
def index_page():
    return "Hello, World"

# http://127.0.0.1:5000/time
@app.route("/time")
def time_page():
    return time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())

app.run(port=os.environ.get("PORT", 8080))
