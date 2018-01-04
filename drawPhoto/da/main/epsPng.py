# coding=utf-8
"""
@desc:eps转png
"""
import datetime
from flask import send_file, g
import da.photoService.fenshiPlan as plan
import os
import sys
import time
import threading
from da.dataService.hqService import hqService
from da.main import main
import csv

from da.main.TreadingDay import TreadingDay
from da.utils.configutil import ConfigUtil

mutex = threading.Lock()

mutex.acquire()
# 存放 图片生成时间
time_map = {}
# 存放 图片访问次数
count_map = {}
mutex.release()


# 单独访问获取图片
@main.route('/fs_code_eps/<code>')
def get_fs_code_eps(code):
    img_path = sys.path[0] + "/da/static/img/" + code + ".png"
    eps_path = sys.path[0] + "/da/static/eps/" + code + ".eps"

    now_time_str = datetime.datetime.now().strftime("%Y-%m-%d")
    td = TreadingDay()
    IfTradingDay, trading_date = td.if_TreadingDay_F10(now_time_str)
    now_datetime = datetime.datetime.strptime(now_time_str, "%Y-%m-%d")
    if IfTradingDay is True or trading_date == now_datetime:
        # png是否存在
        return is_tradingdate_eps(code, eps_path, img_path)

    else:
        return is_not_tardingdate_eps(code, eps_path, img_path,trading_date)


"""
今天不是交易日的处理
"""


def is_not_tardingdate_eps(code, eps_path, img_path, trading_date):
    # png是否存在
    end_15 = trading_date.strftime("%Y-%m-%d") + " %2d:02:00" % 15
    timeArray_end_15 = datetime.datetime.strptime(end_15, "%Y-%m-%d %H:%M:%S")
    yes_int_15 = time.mktime(timeArray_end_15.timetuple())
    now = time.time()
    img_exist = os.path.exists(img_path)
    eps_exist = os.path.exists(eps_path)
    now_time = datetime.datetime.now()
    if code in time_map.keys():
        # map中的时间没有过期
        code_time = time_map[code]
        # 图片时间差距
        if timeArray_end_15 <= code_time <= now_time:
            # 直接返回
            count_eps(code)
            return send_file(img_path, cache_timeout=0)
        else:
            # 执行下面判断
            pass

    if img_exist:
        stat_img = os.stat(img_path)
        stat_time_img = stat_img.st_mtime
        if yes_int_15 <= stat_time_img <= now:
            count_eps(code)
            return send_file(img_path, cache_timeout=0)
        stat_eps = os.stat(eps_path)
        stat_time_eps = datetime.datetime.fromtimestamp(stat_eps.st_mtime)
        # 图片时间差距
        if yes_int_15 <= stat_time_eps <= now:
            eps_to_png(img_path, eps_path)
            return return_file(img_path, code)
        else:
            # 过期
            return create_eps(code, img_path, eps_path)
    else:
        if eps_exist:
            stat = os.stat(eps_path)
            stat_time = datetime.datetime.fromtimestamp(stat.st_mtime)
            if yes_int_15 <= stat_time <= now:
                eps_to_png(img_path, eps_path)
                return return_file(img_path, code)
            # 图片时间差距
            else:
                # 过期 生成 转换 返回
                return create_eps(code, img_path, eps_path)
        else:
            # 判断是否存在code
            try:
                if plan.fs_secucode(code, 1) is False:
                    return "请输入正确的编号"
            except Exception as er:
                return "请输入正确的编号"
            eps_to_png(img_path, eps_path)
            return return_file(img_path, code)


"""
今天是交易日的处理
"""


def is_tradingdate_eps(code, eps_path, img_path):
    # png是否存在
    img_exist = os.path.exists(img_path)
    eps_exist = os.path.exists(eps_path)
    now_time = datetime.datetime.now()
    time_before_3 = now_time + datetime.timedelta(minutes=-2)
    if code in time_map.keys():
        # map中的时间没有过期
        code_time = time_map[code]
        # 图片时间差距
        code_time_s = (code_time - time_before_3).total_seconds()
        if int(code_time_s) >= 0:
            # 直接返回
            return send_file(img_path, cache_timeout=0)
        else:
            # 执行下面判断
            pass

    if img_exist:
        if time_manage(img_path) is True:
            count_eps(code)
            return send_file(img_path, cache_timeout=0)
        stat = os.stat(eps_path)
        stat_time = datetime.datetime.fromtimestamp(stat.st_mtime)
        # 图片时间差距
        stat_time_s = (stat_time - time_before_3).total_seconds()
        if int(stat_time_s) >= 0:
            # 不过期
            img_stat = os.stat(img_path)
            # img修改时间 > eps修改时间
            if img_stat.st_mtime > stat.st_mtime:
                eps_to_png(img_path, eps_path)
                return return_file(img_path, code)
            else:
                return create_eps(code, img_path, eps_path)
        else:
            # 过期
            return create_eps(code, img_path, eps_path)
    else:
        if eps_exist:
            stat = os.stat(eps_path)
            stat_time = datetime.datetime.fromtimestamp(stat.st_mtime)
            if time_manage(eps_path) is True:
                eps_to_png(img_path, eps_path)
                return return_file(img_path, code)
            # 图片时间差距
            stat_time_s = (stat_time - time_before_3).total_seconds()
            if int(stat_time_s) >= 0:
                # 不过期 转换 返回
                eps_to_png(img_path, eps_path)
                return return_file(img_path, code)
            else:
                # 过期 生成 转换 返回
                return create_eps(code, img_path, eps_path)
        else:
            # 判断是否存在code
            try:
                if plan.fs_secucode(code, 1) is False:
                    return "请输入正确的编号"
            except Exception as er:
                return "请输入正确的编号"
            eps_to_png(img_path, eps_path)
            return return_file(img_path, code)


def create_eps(code, img_path, eps_path):
    plan.fs_secucode(code, 1)  # 画eps
    eps_to_png(img_path, eps_path)
    return return_file(img_path, code)


def return_file(path, code):
    try:
        count_eps(code)
        time_map[code] = datetime.datetime.now()
        return send_file(path, cache_timeout=0)
    except Exception as er:
        return "返回图片错误"


"""
计数
"""


def count_eps(code):
    if code not in count_map.keys():
        count_map[code] = 1
    else:
        count_map[code] += 1


def eps_to_png(img_path, eps_path):
    # starttime = time.time()
    # windows pngalpha
    #os.system(sys.path[
    #             0] + "/da/static/lib/gswin64c -dBATCH -dNOPAUSE -dEPSCrop -r140 -sDEVICE=png256 "
    #                  "-dGraphicsAlphaBits=4 -dTextAlphaBits=4 -sOutputFile=" + img_path + " " + eps_path)
    #cmd = sys.path[0] + "/da/static/lib/pngquant.exe --force --speed=3 " + img_path + " -o " + img_path;
    # linux
    os.system(
         "gs -dBATCH -dNOPAUSE -dEPSCrop -r140 -sDEVICE=png256 -dGraphicsAlphaBits=4 -dTextAlphaBits=4 -sOutputFile=" + img_path + " " + eps_path)
    # endtime = time.time()
    cmd = "pngquant --force --speed=3 " + img_path + " -o " + img_path;
    os.system(cmd)
    # print str(endtime - starttime)


# 记录访问每只股票访问次数
def get_count_map():
    hq = hqService()
    hqUrl = ConfigUtil.getconfig('https', 'ag')
    # hqUrl = 'http://php.cnstock.com/news_new/index.php/codelist/ag'
    data = hq.getUrlData(hqUrl)
    secu_list = []
    for i in range(len(data)):
        secu_list.append(data[i]['code'])
    sub_secu_list = list(set(secu_list).difference(set(count_map.keys())))

    now_time_str = time.strftime("%Y%m%d", time.localtime(time.time()))
    dir_path = sys.path[0] + "/da/static/count/" + now_time_str
    isExists = os.path.exists(dir_path)
    if not isExists:
        os.makedirs(dir_path)
    else:
        pass

    f_max = file(dir_path + '/hy_code.csv', 'wb')
    f_max_writer = csv.writer(f_max)
    f_mid = file(dir_path + "/chy_code.csv", 'wb')
    f_mid_writer = csv.writer(f_mid)
    f_min = file(dir_path + "/bhy_code.csv", 'wb')
    f_min_writer = csv.writer(f_min)

    max_map = []
    mid_map = []
    min_map = []

    if len(sub_secu_list) > 0:
        for i in range(len(sub_secu_list)):
            count_map[sub_secu_list[i]] = 0

    count_list = sorted(count_map.items(), key=lambda d: d[1], reverse=True)
    length = len(count_list)
    for i in range(length):
        if i <= length / 3:
            max_map.append([count_list[i][0], count_list[i][1]])
        elif (i > length / 3) and (i <= (length / 3) * 2):
            mid_map.append([count_list[i][0], count_list[i][1]])
        else:
            min_map.append([count_list[i][0], count_list[i][1]])

    f_max_writer.writerow(['secucode', 'count'])
    f_mid_writer.writerow(['secucode', 'count'])
    f_min_writer.writerow(['secucode', 'count'])
    f_max_writer.writerows(max_map)
    f_mid_writer.writerows(mid_map)
    f_min_writer.writerows(min_map)
    f_max.close()
    f_mid.close()
    f_min.close()


"""
判断图片的更新时间是否在
昨天的15:10-今天9:20或者11:40-12:50
"""


def time_manage(image_path=None):
    # print '判断交易时间'
    # 11:40>< 13:40
    # 9:20 <>15:10

    now = time.time()
    start_9 = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:25:00" % 9
    timeArray_start_9 = time.strptime(start_9, "%Y-%m-%d %H:%M:%S")
    start_int_9 = time.mktime(timeArray_start_9)
    end_15 = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:05:00" % 15
    timeArray_end_15 = time.strptime(end_15, "%Y-%m-%d %H:%M:%S")
    end_int_15 = time.mktime(timeArray_end_15)
    start_11 = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:35:00" % 11
    end_12 = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:00:00" % 13
    timeArray_start_11 = time.strptime(start_11, "%Y-%m-%d %H:%M:%S")
    start_int_11 = time.mktime(timeArray_start_11)
    timeArray_end_12 = time.strptime(end_12, "%Y-%m-%d %H:%M:%S")
    end_int_12 = time.mktime(timeArray_end_12)
    if start_int_9 > now:
        if image_path:
            stat = os.stat(image_path)
            stat_time = stat.st_mtime
            now_time_str = datetime.datetime.now().strftime("%Y-%m-%d")
            td = TreadingDay()
            IfTradingDay, trading_date = td.if_TreadingDay_F10(now_time_str)
            if IfTradingDay is False and isinstance(trading_date, str):
                return False
            end_15 = trading_date.strftime("%Y-%m-%d") + " %2d:01:00" % 15
            timeArray_end_15 = datetime.datetime.strptime(end_15, "%Y-%m-%d %H:%M:%S")
            yest_int_15 = time.mktime(timeArray_end_15.timetuple())
            if yest_int_15 < stat_time < start_int_9:
                return True
            else:
                return False
    elif now > end_int_15:
        if image_path:
            stat = os.stat(image_path)
            stat_time = stat.st_mtime
            if stat_time > end_int_15:
                return True
            else:
                return False
    elif start_int_11 < now < end_int_12:
        # print '11:40之后'
        if image_path:
            stat = os.stat(image_path)
            stat_time = stat.st_mtime
            if start_int_11 < stat_time < end_int_12:
                # print 'True'
                return True
            else:
                # print 'False'
                return False
        else:
            return True
    else:
        return False
