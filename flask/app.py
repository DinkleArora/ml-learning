from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this flask course. I love this course"

@app.route("/index")
def index():
    return "Welcome to the index page of the flask course"

if __name__ == "__main__":
    app.run(debug=True)