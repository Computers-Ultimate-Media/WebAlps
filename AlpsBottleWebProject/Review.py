import datetime


class Review(object):
    author: str
    date: datetime.datetime
    text: str

    def __init__(self, author: str, date: datetime.datetime, text: str):
        self.author = author
        self.date = date
        self.text = text
