import urllib2
import json
import random

def url():
    tmp = urllib2.urlopen('http://api.edmunds.com/api/vehicle/v2/makes?fmt=json&state=new&api_key=7bvg7mx4qwms54fgkgrdyxv7')
    return tmp


def getIntermediate():
    f = url()
    json_string = f.read()
    parsed_json = json.loads(json_string)
    stuff = parsed_json['makes']
    length = len(stuff)
    item = stuff[random.randrange(0,length)]
    temp = [item['name'],item['niceName']]
    length = len(item)
    item = item['models'][random.randrange(0,length)]
    temp = temp + [item['niceName'], item['name'], item['years'][0]['year']]
    f.close()
    f = urllib2.urlopen('http://api.edmunds.com/api/vehicle/v2/%s/models?fmt=json&state=new&api_key=7bvg7mx4qwms54fgkgrdyxv7'%temp[1])
    json_string = f.read()
    parsed_json = json.loads(json_string)
    stuff = parsed_json['models']
    a = 0
    while a < parsed_json['modelsCount']:
        scan = stuff[a]['niceName']
        if scan == temp[2]:
            scan = stuff[a]
            break
    return temp + [scan]

def getStyle(thing):
     return thing[0:-1] + [thing[5]['years'][0]['styles'][0]['id']]

def getItem():
     c = getIntermediate()
     c = getStyle(c)
     return c

def getTitle(item):
    return str(item[4]) + " " + item[0] + " " + item[3]

def getId(item):
    return item[5]

def getPrice(item):
    f = urllib2.urlopen('http://api.edmunds.com/v1/api/tco/newtotalcashpricebystyleidandzip/%s/10282?fmt=json&api_key=7bvg7mx4qwms54fgkgrdyxv7'%item[5])
    json_string = f.read()
    parsed_json = json.loads(json_string)
    stuff = parsed_json['value']
    return stuff

def getDescrip(item):
    return ""

def getUrl(item):
    return "www.edmunds.com/%s/%s/%s/"%(item[1],item[2],item[4])

def getImage(item):
    f = urllib2.urlopen('http://api.edmunds.com/v1/api/vehiclephoto/service/findphotosbystyleid?styleId=%s&fmt=json&api_key=7bvg7mx4qwms54fgkgrdyxv7'%item[5])
    json_string = f.read()
    parsed_json = json.loads(json_string)
    stuff = parsed_json[0]['photosSrcs'][0]
    image = 'http://media.ed.edmunds-media.com/' + stuff
    return image

