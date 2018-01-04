# -*- coding: utf-8 -*-
import base64

import time

starttime = time.time()
f=open(r'IOU.jpg','rb') #二进制方式打开图文件
for i in xrange(5000):
    ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
endtime = time.time()
print str(endtime - starttime)
print ls_f
