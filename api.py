import etsy
import edmunds

def getTitle(item):
    if len(item) == 6:
        return edmunds.getTitle(item)
    else:
        return etsy.getTitle(item)


def getPrice(item):
    if len(item) == 6:
        return edmunds.getPrice(item)
    else:
        return etsy.getPrice(item)


def getDescrip(item):
    if len(item) == 6:
        return edmunds.getDescrip(item)
    else:
        return etsy.getDescrip(item)

def getUrl(item):
    if len(item) == 6:
        return edmunds.getUrl(item)
    else:
        return etsy.getUrl(item)

def getImage(item):
    if len(item) == 6:
        return edmunds.getImage(item)
    else:
        return etsy.getImage(item)
