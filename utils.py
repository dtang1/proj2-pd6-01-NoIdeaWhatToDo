import pymongo
from bson.objectid import ObjectId

import app
import config as conf


client = pymongo.MongoClient(conf.db)
db = client.TPIS

users = db.users
prizes = db.prizes

def register(username, url):
	if users.find_one({"username" : username, "done" : False}) is None:
		users.insert({ "username" : username, "done": False, "round" : 1, "prize" : 0, "fb" : url})
		return True
	else:
		app.session["error"] = "userExists"
	return False

#returns users that have completed game in order
def getusers():
    return users.find({'done' : True}).sort(u'prize', -1).limit(20)

#adds prize to user
def addPrize(username, prizename, price, url):
    prizes.insert({'username' : username, 'prize' : prizename, 'price' : price, 'url' : url})
    users.update({'username':username, "done" :False},{'$set':{'prize':getprize(username) + price}})

#adds round to user
def addRound(username):
    users.update({'username':username , 'done' : False},{'$set':{'round':getround(username) + 1}})

#gets a user's number of rounds
def getround(username):
    user = users.find_one({'username':username, 'done' : False})
    return user['round']

#gets a user's total winnings
def getprize(username):
    user = users.find_one({'username':username})
    return user['prize']

#changes user's attribute of done to True after completing game
def done(username):
    user = users.find_one({'username':username, 'done' : False})
    users.update({'username':username, "done" :False},{'$set':{'done':True}})

#returns all of users prizes and then removes them from database
def getPrizes(username):
    temp = prizes.find({'username':username})
    done(username)
    return temp

def clearPrizes(username):
    prizes.remove({'username':"Derek Tang"})
    users.remove({'username':"DerekTang"})
    #users.update({'username':username, "done" :False},{'$set':{'prize':0}})

def loggedIn():
	if "username" in app.session:
		return True
	else:
		app.session["error"] = "mustLogin"
		return False
