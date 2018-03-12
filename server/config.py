#coding=utf-8
import os 

SECRET_KEY = os.environ.get('SECRET_KEY') or '1234abcd!'

ALLOWED_FILE = ['jpg','png','rar','zip']
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DB = 'photo'
