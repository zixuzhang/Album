#coding=utf-8
from app import db
from datetime import datetime

class Album(db.Document):
    '''
    相册信息
    '''
    name = db.StringField()
    date = db.DateTimeField(default=datetime.now)

    def to_dict(self):
        d = {}
        for key in self:
            if key == 'id':
                d['id'] = str(self.id)
            elif key == 'date':
                d['date'] = self.date.strftime('%Y-%m-%d')
            else:
                d[key] = self[key]
        return d