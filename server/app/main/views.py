#coding=utf-8
import zipfile
from . import main
from flask import render_template, redirect, url_for,request,jsonify
from ..models.Photo import Photo
from ..models.Album import Album
# from config import ALLOWED_FILE
# allowed_files = ['jpg','png','zip','rar']

def filetype(filename):
    return '.' in filename and filename.rsplit('.',1)[1]

@main.route('/')
def index():
    #首页
    #页码
    page = int(request.args.get('page',0))
    count = int(request.args.get('count',1))
    print page
    print count
    # imgs = Photo.objects[(page-1)*count:page*count]
    imgs = Photo.objects
    imgs = [i.to_dict() for i in imgs]
    return render_template('home.html',imgs=imgs)



@main.route('/album')
def album():
    #相册页
    return render_template('album.html')

@main.route('/upload',methods=['GET','POST'])
def upload():
    #上传照片或者上传压缩文件
    album_name = ''
    file = request.files['file']
    filename = file.filename
    if file:
        if filetype(filename) in ['zip','rar']:
            #压缩文件
            z = zipfile.ZipFile(file,'r')
            for i in z.namelist():
                img_name = i
                if filetype(img_name) in ['png','jpg']:
                    #判断压缩文件是否是图片
                    img = z.read(i)
                    Photo(img_name=img_name,img=img).save()
            return jsonify({'msg': '压缩包上传成功', 'type': 'success'})
        elif filetype(filename) in ['png','jpg']:
            #图片文件
            Photo(album_name=album_name,img=file).save()
            return jsonify({'msg': '图片上传成功', 'type': 'success'})


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

