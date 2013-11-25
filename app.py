from flask import Flask
from flask import render_template, redirect, url_for
from flask import session, request

import config as conf
import utils
import datetime

app = Flask(__name__)
app.secret_key = conf.SECRET_KEY

@app.route("/")
def home():
        return render_template("home.html", posts = utils.getPosts())

@app.route("/register", methods = ["GET", "POST"])
def register():
        if request.method == "GET":
                return render_template("register.html")

        elif not utils.loggedIn():
                username = request.form["username"]
                if utils.register(username, password, passRetype, security, answer):
                        session["username"] = username
                        return redirect(url_for("home"))
                else:
                        return error()
        else:
                return redirect(url_for("home"))



def error():
        error = session["error"]
        return render_template("error.html", error = error)

if __name__ == "__main__":
        app.run(debug = True)