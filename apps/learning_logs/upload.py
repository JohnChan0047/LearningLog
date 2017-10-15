# -*- coding:utf-8 -*- 
__author__ = 'John 2017/10/15 23:13'

from django.http import HttpResponse
from LearningLog.settings import MEDIA_ROOT, MEDIA_URL
from django.views.decorators.csrf import csrf_exempt
import os
import uuid
import json
import datetime as dt


@csrf_exempt
def upload_image(request, dir_name):
    result = {'error': 1, 'message': '上传出错'}
    files = request.FILES.get('imgFile', '')
    if files:
        result = image_upload(files, dir_name)
    return HttpResponse(json.dumps(result), content_type='application/json')


def upload_generation_dir(dir_name):
    today = dt.datetime.today()
    dir_name = dir_name + '/%d/%d/' %(today.year, today.month)
    if not os.path.exists(MEDIA_ROOT):
        os.makedirs(MEDIA_ROOT)
    return dir_name


def image_upload(files, dir_name):
    allow_suffix = ['jpg', 'png', 'jpeg', 'gif', 'bmg', 'mp4']
    file_suffix = files.name.split('.')[-1]
    if file_suffix not in allow_suffix:
        return {'error': 1, 'message': '格式错误'}
    relative_path_file = upload_generation_dir(dir_name)
    path = os.path.join(MEDIA_ROOT, relative_path_file)
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = str(uuid.uuid1()) + '.' + file_suffix
    path_file = os.path.join(path, file_name)
    file_url = MEDIA_URL + relative_path_file + file_name
    open(path_file, 'wb').write(files.file.read())
    return {'error': 0, 'url': file_url}