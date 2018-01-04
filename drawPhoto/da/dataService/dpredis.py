# -*- coding: utf-8 -*-

'''
@author: yln
@Time    : 2017/12/18 9:35
@Site    : 
@File    : redis.py.py
@Software: PyCharm

'''
# import json

import redis  # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
from da.utils.configutil import ConfigUtil


# host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
class RedisHelper :
    def __init__(self):
        if not hasattr(RedisHelper, 'pool'):
            RedisHelper.create_pool()
        self._connection = redis.StrictRedis(connection_pool=RedisHelper.pool)

    @staticmethod
    def create_pool():
        host = ConfigUtil.getconfig('redis', 'host')
        port = ConfigUtil.getconfig('redis', 'port')
        RedisHelper.pool = redis.ConnectionPool(host=host, port=port)

    def get_list(self, key):
        if self._connection.exists(key):
            list = self._connection.lrange(key, 0, -1)
            list_c = []
            for hq in list:
                files_List = []
                files = hq.replace('[', '').replace(']', '')
                files = files.split(',')
                # print files
                for i in range(len(files)):
                    # file_1 = files[i].replace("'", ' ')
                    files_List.append(eval(files[i]))
                list_c.append(files_List)
            return list_c
        else:
            return None
