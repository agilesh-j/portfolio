"""Agilesh J – portfolio website (Flask).

Run locally:   python app.py   ->  http://127.0.0.1:5000
All text lives in data.py, so you rarely need to touch this file.
"""
from flask import Flask, render_template

import data

# "public" holds CSS, JS and images. Vercel serves that folder directly,
# and Flask serves it too when you run the site on your own computer.
app = Flask(__name__, static_folder="public", static_url_path="")


@app.route("/")
def home():
    return render_template("index.html", d=data)


if __name__ == "__main__":
    app.run(debug=True)
