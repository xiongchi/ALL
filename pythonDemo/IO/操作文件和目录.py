# -*- coding: utf-8 -*-
import os

#操作系统类型
print os.name
#环境变量
print os.environ

print os.environ.get('PATH')

#查看当前目录的绝对路径
print os.path.abspath('.')

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
dir_path = os.path.join('E:\\github\\xcrepository\\pythonDemo', 'TO')

#创建一个目录:
os.mkdir(dir_path)
#删除一个目录
os.rmdir(dir_path)
#把一个路径拆分为两部分
print os.path.split('/Users/michael/testdir/file.txt')
#获取文件扩展名
print os.path.splitext('/path/to/file.txt')
