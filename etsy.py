import urllib2
import json
import random

def url():
    tmp = urllib2.urlopen('https://openapi.etsy.com/v2/listings/active.json?callback=getData&api_key=sj5fo4b3gtjiw3um4yffgleb')
    return tmp

def getItem():
    f = url()
    json_string = f.read()
    parsed_json = json.loads(json_string)
    stuff = parsed_json['results']
    length = len(stuff)
    item = stuff[random.randrange(0,length)]
    f.close()
    return [item['title'],item['listing_id'],item['price'],item['description'],item['url']]

def getTitle(item):
    return item[0]

def getId(item):
    return item[1]

def getPrice(item):
    return item[2]

def getDescrip(item):
    return item[3]

def getUrl(item):
    return item[4]

def getImage(item):
    id = getId(item)
    image = 'https://openapi.etsy.com/v2/listings/%s/images.json?callback=getData&api_key=sj5fo4b3gtjiw3um4yffgleb'%id
    tmp = urllib2.urlopen(image)
    json_string = tmp.read()
    parsed_json = json.loads(json_string)
    imagelink = parsed_json['results'][0]['url_fullxfull']
    return imagelink
