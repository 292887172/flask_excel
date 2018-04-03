#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from flask import request

from wtforms import Form
from wtforms.fields import simple

import sys
import os
import datetime
import xlrd
import xlwt

account = Blueprint('account', __name__)


class Up_file_Foem(Form):
    body = simple.FileField(u'选择上传文件')
    submit = simple.SubmitField(u'开始上传')

@account.route('/index', methods=['GET', "POST"])
def index():
    if request.method=='GET':
        return render_template('index.html')
    else:
        DOWLOAD = r'D:\flask-excel\pro_flask\down'
        f=request.files.get('myfile')
        # s='D：\\flask-excel\pro_flask\down\\'
        s=os.path.join(DOWLOAD,f.filename)
        with open (s,'wb') as v:
            v.write(f.read())

        workbook = xlrd.open_workbook(s)
        sheet = workbook.sheet_by_index(0)
        print(sheet.row_values(1))
        return 'sfsdfsd'


