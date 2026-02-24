from flask import Flask, render_template, request, redirect, get_flashed_messages

from data import db_session
from data.abouts import Abouts
from data.peoples import People
from random import shuffle

app = Flask(__name__)
app.secret_key = 'decembrists'


@app.route('/', methods=['GET'])
def start():
    return redirect("/main")


@app.route('/main', methods=['GET'])
def main():
    return render_template("main.html")


@app.route("/portrait", methods=["GET", "POST"])
def portrait():
    global people
    if request.method == "GET":
        db_sess = db_session.create_session()
        dec = db_sess.query(People).all()
        shuffle(dec)
        people = dec[0]
        return render_template("portrait.html", portrait=people.portrait, dec=dec)
    elif request.method == "POST":
        return redirect(f"/answer/{request.form.get('ans_list') == people.name}")


@app.route("/factsquestion", methods=["GET", "POST"])
def factsquestion():
    global people
    if request.method == "GET":
        db_sess = db_session.create_session()
        dec = db_sess.query(People).all()
        shuffle(dec)
        people = dec[0]
        abouts = db_sess.query(Abouts).filter(Abouts.people_id == people.id).all()
        shuffle(abouts)
        about = abouts[:2]
        return render_template("factsquize.html", fact1=about[0], fact2=about[1], dec=dec)
    elif request.method == "POST":
        return redirect(f"/answer/{request.form.get('ans_list') == people.name}")


@app.route("/answer/<f>", methods=["GET"])
def ans(f):
    if f == "True":
        return render_template("ans.html", answer="Правильно")
    return render_template("ans.html", answer="Неправильно")


@app.route("/facts", methods=["GET"])
def facts():
    d = dict()
    db_sess = db_session.create_session()
    dec = db_sess.query(People).all()
    for p in dec:
        abouts = db_sess.query(Abouts).filter(Abouts.people_id == p.id).all()
        d[p] = abouts
    return render_template("facts.html", d=d)


if __name__ == '__main__':
    db_session.global_init("db/decembrists.db")
    people = None
    app.run(debug=True)
