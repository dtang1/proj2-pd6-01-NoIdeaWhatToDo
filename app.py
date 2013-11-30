from flask import Flask
from flask import render_template, redirect, url_for
from flask import session, request
from flask import url_for, request, session, redirect
from flask_oauth import OAuth

import config as conf
import utils
import datetime
import etsy

FACEBOOK_APP_ID = '1423888951173454'
FACEBOOK_APP_SECRET = '465eb41ada435a758eca69a16b47c8e2'

oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': ('email, ')}
)

app = Flask(__name__)
app.secret_key = conf.SECRET_KEY

#renders home.html, which includes the option to sign in and displays a leaderboard
@app.route("/")
def home():
<<<<<<< HEAD
        return render_template("home.html")
=======
        return render_template("home.html", leaders = utils.getusers())
>>>>>>> Derek

#allows user to create a username to play under. user is allowed to play under the same username multiple times. also option to play under facebook account
@app.route("/register", methods = ["GET", "POST"])
def register():
        if request.method == "GET":
                return render_template("register.html")

        elif not utils.loggedIn():
                username = request.form["username"]
                if utils.register(username):
                        session["username"] = username
                        return redirect(url_for("home"))
                else:
                        return error()
        else:
                return redirect(url_for("home"))


@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')

def pop_login_session():
    session.pop('logged_in', None)
    session.pop('facebook_token', None)

@app.route("/facebook_login")
def facebook_login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next'), _external=True))

@app.route("/facebook_authorized")
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('home')
    if resp is None or 'access_token' not in resp:
        return redirect(next_url)

    session['logged_in'] = True
    session['facebook_token'] = (resp['access_token'], '')

    return redirect(next_url)

<<<<<<< HEAD
=======
#logs user out of session
>>>>>>> Derek
@app.route("/logout")
def logout():
    pop_login_session()
    session.pop("username")
    return redirect(url_for('home'))

<<<<<<< HEAD
=======
#initiates random api search to find an object. Declares item as global var and then redirects to actual game
>>>>>>> Derek
@app.route("/start")
def start():
    global gnum
    #if (gnum > 0):
    #    redirect(url_for('game'))
    gnum = 1
    global randitem
    randitem = etsy.getItem()
    
    return redirect(url_for('game'))

<<<<<<< HEAD
=======
#This is the link to the game. uses global var from /start to display various aides to user for help in guessing price
#Guesses limited to 6 per round. There are 7 rounds in total. Uses while loop to allow for multiple guesses in a given round
>>>>>>> Derek
@app.route("/game", methods = ["GET", "POST"])
def game():
    global gnum
    global randitem
    round = utils.getround(session['username'])
<<<<<<< HEAD
    if round > 9:
=======
    if round > 7:
>>>>>>> Derek
        return redirect(url_for('gameend'))
    itemname = etsy.getTitle(randitem)
    imageurl = etsy.getImage(randitem)
    itemdescription = etsy.getDescrip(randitem)
    price = etsy.getPrice(randitem)
    if request.method == "GET":
        return render_template("game.html", round = round, itemname = itemname, url = imageurl, itemdescription = itemdescription, message = "Enter your guess for the price of this item to see if the Price Is Right!")
    elif utils.loggedIn():
        user = session["username"]
    else:
        return redirect("home")
    while gnum < 6:
        guess = request.form["price"]
        if (abs(float(guess) - float(price)) < (float(price) / 10)):
            utils.addPrize(session['username'],itemname,float(price),etsy.getUrl(randitem))
            break
        elif (guess > price):
            gnum = gnum + 1
<<<<<<< HEAD
            return render_template("game.html", round = round, itemname = itemname, url = imageurl, itemdescription = itemdescription, message = str(gnum) + "Your previous guess was too high! Enter your guess for the price of this item to see if the Price Is Right!")
        else:
            gnum = gnum + 1
            return render_template("game.html", round = round, itemname = itemname, url = imageurl, itemdescription = itemdescription, message = str(gnum) +  "Your previous guess was too low! Enter your guess for the price of this item to see if the Price Is Right!")
    return redirect(url_for('endround'))

=======
            return render_template("game.html", round = round, itemname = itemname, url = imageurl, itemdescription = itemdescription, message = "This is guess number " + str(gnum) + ". Your previous guess was too high! Enter your guess for the price of this item to see if the Price Is Right!")
        else:
            gnum = gnum + 1
            return render_template("game.html", round = round, itemname = itemname, url = imageurl, itemdescription = itemdescription, message = "This is guess number " + str(gnum) + ". Your previous guess was too low! Enter your guess for the price of this item to see if the Price Is Right!")
    return redirect(url_for('endround'))

#the round ends and user is given link to website where they can purchase the previously shown item.
#if the user guessed the item's price correctly, the prize is stored in the prize db and total winnings are kept track of
>>>>>>> Derek
@app.route("/endround")
def endround():
    global gnum
    global randitem
    round = utils.getround(session['username'])
    itemname = etsy.getTitle(randitem)
    imageurl = etsy.getImage(randitem)
    itemdescription = etsy.getDescrip(randitem)
    price = etsy.getPrice(randitem)
    url = etsy.getUrl(randitem)
    #if gnum > 0 and gnum < 7:
    #    return redirect(url_for('game'))
    #else:
    gnum = 0
    utils.addRound(session['username'])
    return render_template("endround.html", round = round, itemname = itemname, url = imageurl, itemdescription = itemdescription, price = price, link = url)

<<<<<<< HEAD
=======
#displays user's prizes and winnings after game is complete
@app.route("/gameend")
def gameend():
    return render_template("gameend.html", prizes = utils.getPrizes(session['username']), prizemoney = utils.getprize(session['username']))
>>>>>>> Derek

def error():
        error = session["error"]
        return render_template("error.html", error = error)

if __name__ == "__main__":
        app.run(debug = True)