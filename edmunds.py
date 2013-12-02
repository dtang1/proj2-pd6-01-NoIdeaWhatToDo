import urllib2
import json
import random

def url():
    tmp = urllib2.urlopen('http://api.edmunds.com/api/vehicle/v2/makes?fmt=json&state=new&api_key=7bvg7mx4qwms54fgkgrdyxv7')
    return tmp

def url2(url):
    tmp = urllib2.urlopen(url)
    return tmp

def getItem():
    f = url()
    json_string = f.read()
    parsed_json = json.loads(json_string)
    stuff = parsed_json['makes']
    length = len(stuff)
    item = stuff[random.randrange(0,length)]
    temp = [item['name'],item['niceName']]
    f.close()
    f = urllib2.urlopen('http://api.edmunds.com/api/vehicle/v2/%s/models?fmt=json&state=new&api_key=7bvg7mx4qwms54fgkgrdyxv7'%temp[1])
    json_string = f.read()
    parsed_json = json.loads(json_string)
    length = parsed_json['modelsCount']
    stuff = parsed_json['models']
    stuff = stuff[random.randrange(0, length)]
    temp = temp + [stuff['niceName'], stuff['name'], stuff['years'][0]['year'], stuff['years'][0]['styles'][0]['id']]
    return temp


def getTitle(item):
    return str(item[4]) + " " + item[0] + " " + item[3]

def getId(item):
    return item[5]

def getPrice(item):
    url = 'http://api.edmunds.com/v1/api/tco/newtotalcashpricebystyleidandzip/%s/10282?fmt=json&api_key=7bvg7mx4qwms54fgkgrdyxv7'%item[5]
    url = urllib2.Request(url)
    try:
     f = urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        return "0"
    #f = url2(url)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    stuff = parsed_json['value']
    return stuff

def getDescrip(item):
    return "It goes Vroom Vroom. Unless this car is electric. If thats the case, then it goes buzz buzz."

def getUrl(item):
    return "http://www.edmunds.com/%s/%s/%s/"%(item[1],item[2],item[4])

def getImage(item):
    url = 'http://api.edmunds.com/v1/api/vehiclephoto/service/findphotosbystyleid?styleId=%s&fmt=json&api_key=7bvg7mx4qwms54fgkgrdyxv7'%item[5]
    url = urllib2.Request(url)
    try:
        f = urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        return ""
    #f = urllib2.urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    stuff = parsed_json[0]['photoSrcs'][0]
    image = 'http://media.ed.edmunds-media.com/' + stuff
    return image

