# coding=utf-8
import datetime
import threading

import re
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from flask import send_file

import da.photoService.fenshiPlan as plan
import os
import sys
import time
from da.main import main

from da.main.TreadingDay import TreadingDay

mutex = threading.Lock()

mutex.acquire()
# 存放 图片生成时间
time_map_size = {}
# 存放 图片访问次数
count_map_size = {}
mutex.release()


@main.route('/del_code/<code>')
def delete_size(code):

    try:
        enhance_file_name = sys.path[0] + "/da/static/enhance/" + code
        img_file_name = sys.path[0] + "/da/static/img/" + code + ".png"
        list = [enhance_file_name + ".png", enhance_file_name + "-1.png", enhance_file_name + "-2.png",
                enhance_file_name + "-3.png",
                enhance_file_name + "-4.png"]
        list_code = [code + '-1', code + '-2', code + '-3', code + '-4']
        for path in list:
            if os.path.exists(path):
                os.remove(path)
        for cu_code in list_code:
            if cu_code in time_map_size.keys():
                time_map_size.pop(cu_code)
        if os.path.exists(img_file_name):
            os.remove(img_file_name)

    except:
        return 'del fail'
    return 'success'


# 单独访问获取图片
@main.route('/fs_code_size/<code>/<typeSize>')
def get_fs_code_size(code, typeSize):
    # 判断是否是交易日
    # print type(typeSize)
    if typeSize != '1' and typeSize != '2' and typeSize != '3' and typeSize != '4':
        return '参数有误'
    now_time_str = datetime.datetime.now().strftime("%Y-%m-%d")
    td = TreadingDay()
    IfTradingDay, trading_date = td.if_TreadingDay_F10(now_time_str)

    # IfTradingDay, trading_date = td.if_TreadingDay_oracle(now_time_str)
    enhance_path = sys.path[0] + "/da/static/enhance/" + code + "-" + typeSize + ".png"
    img_path = sys.path[0] + "/da/static/img/" + code + ".png"
    now_datetime = datetime.datetime.strptime(now_time_str, "%Y-%m-%d")
    if IfTradingDay is True or trading_date == now_datetime:
        # png是否存在
        return is_tradingdate_size(code, enhance_path, img_path, typeSize)

    else:
        return is_not_tardingdate_size(code, enhance_path, img_path, trading_date, typeSize)


"""
今天不是交易日的处理
"""


def is_not_tardingdate_size(code, enhance_path, img_path, trading_date, typeSize):
    # 今天不是交易日，判断增强之后的图片更新时间是否在上个交易日和今天之间
    # if true 直接返回图片
    # else 判断未增强的img，是否在上个交易日和今天之间，if true，增强之后返回 ，else  生成图片
    end_15 = trading_date.strftime("%Y-%m-%d") + " %2d:00:00" % 15
    timeArray_end_15 = datetime.datetime.strptime(end_15, "%Y-%m-%d %H:%M:%S")
    yes_int_15 = time.mktime(timeArray_end_15.timetuple())
    now = time.time()
    code_new = code + '-' + typeSize
    if code_new in time_map_size.keys():
        # map中的时间没有过期
        code_time = time_map_size[code_new]
        # 图片时间差距
        if timeArray_end_15 <= code_time <= datetime.datetime.now():
            # 直接返回
            count_size(code)
            return send_file(enhance_path, cache_timeout=0)
        else:
            # 执行下面判断
            pass
    enhance_exist = os.path.exists(enhance_path)
    img_exist = os.path.exists(img_path)
    if enhance_exist:
        # print '增强之后的图片存在'
        stat_enhance = os.stat(enhance_path)
        stat_time_enhance = stat_enhance.st_mtime
        if yes_int_15 <= stat_time_enhance <= now:
            count_size(code)
            return send_file(enhance_path, cache_timeout=0)
        stat_img = os.stat(img_path)
        stat_time_img = datetime.datetime.fromtimestamp(stat_img.st_mtime)
        # 图片时间差距
        if yes_int_15 <= stat_time_img <= now:
            # 不过期
            png_enhance_size(enhance_path, img_path, typeSize)
            return return_file_size(enhance_path, code, typeSize)
        else:
            # 过期
            return create_png_size(code, enhance_path, img_path, typeSize)
    else:
        if img_exist:
            stat = os.stat(img_path)
            stat_time = datetime.datetime.fromtimestamp(stat.st_mtime)
            # print '增强之后的图片不存在'
            if yes_int_15 <= stat_time <= now:
                png_enhance_size(enhance_path, img_path, typeSize)
                return return_file_size(enhance_path, code, typeSize)
            # 图片时间差距
            else:
                # 过期 生成 转换 返回
                return create_png_size(code, enhance_path, img_path, typeSize)
        else:
            # 判断是否存在code
            return create_png_size(code, enhance_path, img_path, typeSize)


"""
今天是交易日的处理
"""


def is_tradingdate_size(code, enhance_path, img_path, typeSize):
    enhance_exist = os.path.exists(enhance_path)
    img_exist = os.path.exists(img_path)
    now_time = datetime.datetime.now()
    time_before = now_time + datetime.timedelta(minutes=-2)
    code_new = code + '-' + typeSize
    if code_new in time_map_size.keys():
        # map中的时间没有过期
        code_time = time_map_size[code_new]
        # 图片时间差距
        code_time_s = (code_time - time_before).total_seconds()
        if int(code_time_s) >= 0:
            # 直接返回
            count_size(code)
            return send_file(enhance_path, cache_timeout=0)
        else:
            # 执行下面判断
            pass
    if enhance_exist:
        # print '增强之后的图片存在'
        if time_manage_size(enhance_path) is True:
            count_size(code)
            return send_file(enhance_path, cache_timeout=0)
        stat = os.stat(img_path)
        stat_time = datetime.datetime.fromtimestamp(stat.st_mtime)
        # 图片时间差距
        stat_time_s = (stat_time - time_before).total_seconds()
        if int(stat_time_s) >= 0:
            # 不过期
            img_stat = os.stat(enhance_path)
            # img修改时间 > eps修改时间
            if img_stat.st_mtime > stat.st_mtime:
                png_enhance_size(enhance_path, img_path, typeSize)
                return return_file_size(enhance_path, code, typeSize)
            else:
                return create_png_size(code, enhance_path, img_path, typeSize)
        else:
            # 过期
            return create_png_size(code, enhance_path, img_path, typeSize)
    else:
        if img_exist:
            stat = os.stat(img_path)
            stat_time = datetime.datetime.fromtimestamp(stat.st_mtime)
            # print '增强之后的图片不存在'
            if time_manage_size(img_path) is True:
                png_enhance_size(enhance_path, img_path, typeSize)
                return return_file_size(enhance_path, code, typeSize)
            # 图片时间差距
            stat_time_s = (stat_time - time_before).total_seconds()
            if int(stat_time_s) >= 0:
                # 不过期 转换 返回
                png_enhance_size(enhance_path, img_path, typeSize)
                return return_file_size(enhance_path, code, typeSize)
            else:
                # 过期 生成 转换 返回
                return create_png_size(code, enhance_path, img_path, typeSize)
        else:
            # 判断是否存在code
            return create_png_size(code, enhance_path, img_path, typeSize)


def count_size(code):
    if code not in count_map_size.keys():
        count_map_size[code] = 1
    else:
        count_map_size[code] += 1


"""
判断图片的更新时间是否在
昨天的15:10-今天9:20或者11:40-12:50
"""


def time_manage_size(image_path=None):
    # print '判断交易时间'
    # 11:40>< 13:40
    # 9:20 <>15:10
    now = time.time()
    start_9 = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:25:00" % 9
    timeArray_start_9 = time.strptime(start_9, "%Y-%m-%d %H:%M:%S")
    start_int_9 = time.mktime(timeArray_start_9)
    end_15 = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:02:00" % 15
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
            end_15 = trading_date.strftime("%Y-%m-%d") + " %2d:02:00" % 15
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


# 直接生成png
def create_png_size(code, enhance_path, img_path, typeSize):
    if plan.fs_secucode_png(code, 1) is False:
        return '请输入正确的编号'  # 画png
    png_enhance_size(enhance_path, img_path, typeSize)
    return return_file_size(enhance_path, code, typeSize)


# 转换png
def png_enhance_size(enhance_path, img_path, typeSize):
    im = Image.open(img_path)
    enh = ImageEnhance.Contrast(im)
    enh = enh.enhance(2.0)
    if typeSize == '1':
        enh = enh.resize((250, 125), Image.ANTIALIAS)
        loc = (120, 90)
        add_watermark(enh, loc)
    elif typeSize == '2':
        enh = enh.resize((350, 175), Image.ANTIALIAS)
        loc = (205, 130)
        add_watermark(enh, loc)
    elif typeSize == '3':
        enh = enh.resize((450, 220), Image.ANTIALIAS)
        loc = (295, 170)
        add_watermark(enh, loc)
    else:
        loc = (390, 205)
        add_watermark(enh, loc)
    enh.save(enhance_path)
    # windos
    #cmd = sys.path[0] + "/da/static/lib/pngquant.exe --force --speed=3 " + enhance_path + " -o " + enhance_path;
    # linux
    cmd = "pngquant --force --speed=3 " + enhance_path + " -o " + enhance_path;
    os.system(cmd)


def add_watermark(enh, loc):
    draw = ImageDraw.Draw(enh)
    Font = ImageFont.truetype(sys.path[0] + '/da/static/font/simsun.ttc', 15)
    draw.text(loc, "cnstock.com", (220, 220, 220), font=Font)
    ImageDraw.Draw(enh)


# 返回图片并记录图片更新时间和访问次数
def return_file_size(enhance_path, code, typeSize):
    try:
        count_size(code)
        code_new = code + '-' + typeSize
        time_map_size[code_new] = datetime.datetime.now()
        return send_file(enhance_path, cache_timeout=0)
    except:
        return "返回图片错误"
