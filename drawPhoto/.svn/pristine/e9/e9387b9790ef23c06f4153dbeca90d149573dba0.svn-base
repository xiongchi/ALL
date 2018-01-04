# -*- coding: utf-8 -*-
import ConfigParser
import csv
import sys


class ConfigUtil(object):
    # 默认读取配置文件http.conf
    @staticmethod
    def getconfig(section, key, filename=sys.path[0]+'/http.conf'):
        cf = ConfigParser.ConfigParser()  # 实例化
        cf.read(filename)  # 读取配置文件
        item = cf.get(section, key)
        return item

    #读取csv文件
    @staticmethod
    def read_csv(file_path):
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            codes = [row['secucode'] for row in reader]
            csvfile.close
        return codes




