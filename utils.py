import pymongo
from bson.objectid import ObjectId

import app
import config as conf


client = pymongo.MongoClient(conf.db)
db = client.NIWTD

users = db.users
prizes = db.prizes

def register(username, round):
	if users.find_one({"username" : username}) is None:
		users.insert({ "username" : username, "round" : 0, "prize" : 0})
		return True
	else:
		app.session["error"] = "userExists"
	return False

def addPrize(username, prizename, price, url):
    prizes.insert({'username' : username, 'prize' : prizename, 'price' : price, 'url' : url})
    users.update({'username':username},{'$set':{'prize':getprize(username) + price}})

def getround(username):
    user = users.find_one({'username':username})
    return user['round']

def getprize(username):
    user = users.find_one({'username':username})
    return user['prize']


def loggedIn():
	if "username" in app.session:
		return True
	else:
		app.session["error"] = "mustLogin"
		return False
