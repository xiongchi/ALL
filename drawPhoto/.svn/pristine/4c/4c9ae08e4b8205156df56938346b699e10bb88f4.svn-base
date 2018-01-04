# coding=utf-8
import multiprocessing
import time
from pylab import *
from da.dataService.hqService import hqService
from config import logger
from da.photoService.fenshiPlan import fs_dorang
from da.utils.configutil import ConfigUtil


def fs_all(proNum,data):
    pro_list = []
    # count = len(data);
    count = len(data)
    # 全局变量
    for i in range(1, proNum + 1):
        if i != proNum:

            p = multiprocessing.Process(name="t" + str(i), target=fs_dorang,
                                        args=(count / proNum * (i - 1), count / proNum * i, data))
        else:
            p = multiprocessing.Process(name="t" + str(i), target=fs_dorang,
                                        args=(count / proNum * (i - 1), count, data))
        pro_list.append(p)

    for i in range(0, len(pro_list)):
        pro_list[i].start()

    for i in range(0, len(pro_list)):
        pro_list[i].join()


def getData():
    hq = hqService()
    hqUrl = ConfigUtil.getconfig('https', 'ag')
    data = hq.getUrlData(hqUrl)
    return data


def test1():
    logger.info("1/1开始测试")
    data = getData()
    test_list = []
    for i in range(36,46):
        test_map = {}
        starttime = time.time()
        fs_all(i, data)
        endtime = time.time()
        logger.info(str(i) + "个进程存储时间:" + str(endtime - starttime))
        test_map["cpuNum"] = i
        test_map["time"] = str(endtime - starttime)
        test_list.append(test_map)
    return test_list


def test2(type,x,y,z):
    logger.info("1/3开始测试")
    test_map = {}
    data = getData()
    length = len(data)
    if type == 'hy':
        starttime = time.time()
        data1 = data[:int(length / 3)]
        fs_all(x, data1)
        endtime = time.time()
        test_map["hy" + str(x)] = str(endtime - starttime)
        logger.info("hy"+str(x) + "个进程存储时间:" + str(endtime - starttime))
    elif type == "chy":
        starttime = time.time()
        data2 = data[int(length / 3):int(length / 3 * 2)]
        fs_all(y, data2)
        endtime = time.time()
        test_map["chy" + str(y)] = str(endtime - starttime)
        logger.info("chy"+str(y) + "个进程存储时间:" + str(endtime - starttime))
    else:
        starttime = time.time()
        data3 = data[int(length / 3 * 2):]
        fs_all(z, data3)
        endtime = time.time()
        test_map["bhy" + str(z)] = str(endtime - starttime)
        logger.info("bhy"+str(z) + "个进程存储时间:" + str(endtime - starttime))
    return test_map


def test3(type,x,y,z):
    logger.info("1/2,3,6开始测试")
    test_map = {}
    data = getData()
    length = len(data)
    if type == 'hy':
        starttime = time.time()
        data1 = data[:int(length / 2)]
        fs_all(x, data1)
        endtime = time.time()
        test_map["hy" + str(x)] = str(endtime - starttime)
        logger.info("hy" + str(x) + "个进程存储时间:" + str(endtime - starttime))
    elif type == "chy":
        starttime = time.time()
        data2 = data[int(length / 2):int(length / 6 * 5)]
        fs_all(y, data2)
        endtime = time.time()
        test_map["chy" + str(y)] = str(endtime - starttime)
        logger.info("chy" + str(y) + "个进程存储时间:" + str(endtime - starttime))
    else:
        starttime = time.time()
        data3 = data[int(length / 6 * 5):]
        fs_all(z, data3)
        endtime = time.time()
        test_map["bhy" + str(z)] = str(endtime - starttime)
        logger.info("bhy" + str(z) + "个进程存储时间:" + str(endtime - starttime))
    return test_map





