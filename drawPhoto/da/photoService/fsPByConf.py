# coding=utf-8
"""    分类画图    ~~~~~~~~~~~~~~~~ """
import matplotlib

from da.utils.configutil import ConfigUtil

matplotlib.use('Agg')
import multiprocessing
import time
from pylab import *
from config import logger
import threading
import da.photoService.fenshiPlan as plan

counter_lock = threading.Lock()


# 分类画图
def fs_do_rang_by_conf(start, end, data):
    for i in xrange(start, end):
        plan.fs_secucode_png(data[i], 1)


def fs_all_by_conf(pro_num, code_list):
    pro_list = []
    count = len(code_list);
    for i in xrange(1, pro_num + 1):
        if i != pro_num:
            p = multiprocessing.Process(name="t" + str(i), target=fs_do_rang_by_conf,
                                        args=(count / pro_num * (i - 1), count / pro_num * i, code_list))
        else:
            p = multiprocessing.Process(name="t" + str(i), target=fs_do_rang_by_conf,
                                        args=(count / pro_num * (i - 1), count, code_list))
        pro_list.append(p)

    for i in xrange(0, len(pro_list)):
        pro_list[i].start()

    for i in xrange(0, len(pro_list)):
        pro_list[i].join()


# 定时任务 生成图片
def batch_by_conf(type, code_list):
    # for i in range(4, 16):
    logger.info(type + "定时任务开始")
    if type == 'hy':
        i = ConfigUtil.getconfig('pros', 'hy')
    elif type == 'chy':
        i = ConfigUtil.getconfig('pros', 'chy')
    elif type == 'bhy':
        i = ConfigUtil.getconfig('pros', 'bhy')
    start_time = time.time()
    if code_list:
        fs_all_by_conf(eval(i), code_list)
    end_time = time.time()
    lock = multiprocessing.Lock()
    lock.acquire()
    logger.info(type + str(i) + "个进程存储时间:" + str(end_time - start_time))
    lock.release()


if __name__ == '__main__':
    print
