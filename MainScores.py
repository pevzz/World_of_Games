from flask import Flask, render_template
from Utils import *

app = Flask(__name__)


@app.route("/scores", methods=['GET'])
def read_score():
    with open("Scores.txt", "r") as data_file:
        score = data_file.readline()
        print(score)
    return render_template("index.html", SCORE=score), 200


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
