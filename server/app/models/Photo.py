#coding=utf-8
from app import db
from datetime import datetime

class Photo(db.Document):
    '''
    照片
    '''
    album_name = db.StringField()
    date = db.DateTimeField(default=datetime.now)
    img = db.FileField()

    def to_dict(self):
        d = {}
        d['id'] = str(self.id)
        return d