#coding=utf-8
import os 

SECRET_KEY = os.environ.get('SECRET_KEY') or '1234abcd!'

MONGODB_HOST = '192.168.102.120'
MONGODB_PORT = 27017
MONGODB_DB = 'photo'
