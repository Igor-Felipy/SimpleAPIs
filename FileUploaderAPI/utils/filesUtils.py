from datetime import datetime


def createFileName():
    date = datetime.now()
    date_formated = date.strftime("%d%m%Y%H%M%s")
    return date_formated


if __name__=="__main__":
    print(createFileName())