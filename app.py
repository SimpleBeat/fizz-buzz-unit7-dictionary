from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/start")
@app.route("/dictionary/<string:word>")
def start(word=""):

    f = open("words.txt")
    all_words = f.read().splitlines()
    f.close()

    number_of_words_left = 0

    if word == "":
        number_of_words_left = len(all_words)
    else:
        for w in all_words:
            if w.startswith(word):
                number_of_words_left += 1

    return render_template('dictionary.html', number_of_words=number_of_words_left, word=word)
