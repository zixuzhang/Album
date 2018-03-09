#coding=utf-8
from . import main
from flask import render_template, redirect, url_for,request,jsonify
from ..models.Photo import Photo
from ..models.Album import Album

@main.route('/')
def index():
    #首页
    return render_template('home.html')

@main.route('/album')
def album():
    #相册页
    return render_template('album.html')

@main.route('/upload')
def upload():
    #上传照片或者上传压缩文件
    pass

@main.route('/api/new-album',methods=['GET','POST'])
def new_album():
    #新建相册
    name = request.form.get('name')
    try:
        album = Album.objects.get(name=name)
        if album:
            return jsonify({'msg': '创建成功，相册已存在', 'type': 'error'})
    except:
        pass
    Album(name=name).save()
    return jsonify({'msg': '相册创建成功', 'type': 'success'})


@main.route('/api/albums',methods=['GET','POST'])
def albums():
    #获取所有的相册信息
    albums = Album.objects()
    data = [i.to_dict() for i in albums]
    return jsonify(data)

