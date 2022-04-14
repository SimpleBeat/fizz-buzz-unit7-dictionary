from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def start():

    return render_template('dictionary.html')
