# -*- coding: UTF-8 -*-
import csv
import datetime
import time
import sys

import os
import da.photoService.fenshiPlan as plan
from da.main import main
import json

from da.main.TreadingDay import TreadingDay
from da.utils.configutil import ConfigUtil
from config import logger
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

"""
监控接口
1.行情接口
2.批量画图服务
3.csv生成
4.单张画图
5.F10交易日接口
"""


@main.route('/monitor')
def m_data():
    start_time = time.time()
    monMap = {}
    monList = []
    secucode, agList, codeList, agFlag = ag_test()
    hqList, hqFlag = hq_test(secucode)
    m_batch_msg, m_batch_Flag = m_batch_draw_photo()
    single_msg, single_Flag = m_get_one_by_code()
    F10_getTrainDay_msg, F10_getTrainDay_Flag= F10_getTrainDay()
    csvList, csvFlag = csv_test()
    monList.append(agList)
    monList.append(hqList)
    monList.append(F10_getTrainDay_msg)
    monList.append(csvList)
    monList.append(m_batch_msg)
    monList.append(single_msg)
    if agFlag and hqFlag and csvFlag and m_batch_Flag and single_Flag and F10_getTrainDay_Flag:
        # 1.正常 0.异常
        status = '1'
    else:
        status = '0'
    monMap['status'] = status
    monMap['message'] = monList
    end_time = time.time()
    # print str(end_time - start_time)
    return json.dumps(monMap,ensure_ascii=False,encoding='utf-8')


# 股票列表接口
def ag_test():
    agList = []
    agUrl = ConfigUtil.getconfig('https', 'ag')
    coldList = m_http(agUrl)
    agList.append("codelist")
    if coldList is False:
        agList.append("error")
        secucode = "sz000001"
        Flag = False
    else:
        agList.append("normal")
        secucode = coldList[0]["code"]
        Flag = True
    agList.append(agUrl)
    return secucode, agList, coldList, Flag


# 行情接口
def hq_test(secucode):
    hqList = []
    apihq = ConfigUtil.getconfig('https', 'apihq') + secucode
    # apihq = "http://apihq.cnstock.com/apihq/min.do?code=" + secucode
    hqFlag = m_http(apihq)
    hqList.append("apihq")
    if hqFlag is False:
        hqList.append("error")
        Flag = False
    else:
        hqList.append("normal")
        Flag = True
    hqList.append(apihq)
    return hqList, Flag


# F10交易日接口
def F10_getTrainDay():
    F10TrainDay_List = []
    F10TrainDay_url = ConfigUtil.getconfig('https', 'F10TrainDay')
    # http://192.168.200.110:8080/F10API/getTrainDay.do
    hqFlag = m_http(F10TrainDay_url)
    F10TrainDay_List.append("F10TrainDay")
    if hqFlag is False:
        F10TrainDay_List.append("error")
        Flag = False
    else:
        F10TrainDay_List.append("normal")
        Flag = True
    F10TrainDay_List.append(F10TrainDay_url)
    return F10TrainDay_List, Flag


# csv统计文件是否生成正常
def csv_test():
    csv_list = []
    all_codes = []
    csv_list.append("createcsv")
    hyCodes, hyFlag = m_csv("hy")
    chyCodes, chyFlag = m_csv("chy")
    bhyCodes, bhyFlag = m_csv("bhy")
    all_codes.append(hyCodes)
    all_codes.append(chyCodes)
    all_codes.append(bhyCodes)
    Flag = True
    if hyFlag and chyFlag and bhyFlag:
        # agCodes = []
        # if agList != None and len(agList) > 0:
        #     for i in range(0,len(agList)):
        #         agCodes.append(agList[i]["code"])
        #     #判断csv和接口中的codes是否完全相等
        #     if set(agCodes) == set(all_codes):
        #         csv_list.append("normal")
        #         Flag = True
        #     else:
        #         csv_list.append("error")
        #         csv_list.append("统计数据缺失")
        #         Flag = False
        # else:
        #     csv_list.append("error")
        #     csv_list.append("行情接口异常")
        csv_list.append("normal")
        csv_list.append("统计文件正常")
    else:
        csv_list.append("error")
        csv_list.append("统计文件不存在")
        Flag = False
    return csv_list, Flag


# 请求url
def m_http(httpUrl):
    try:
        request = Request(httpUrl)
        data_str = urlopen(request, timeout=10).read()
        data = json.loads(data_str)
    except Exception as er:
        return False
    return data


# 判断csv是否存在
def m_csv(type):
    now_time_str = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y%m%d")
    path = sys.path[0] + "/da/static/count/" + now_time_str + "/" + type + '_code.csv'
    isExists = os.path.exists(path)
    flag = True
    if isExists:
        codes = read_csv(path)
        return flag, codes
    else:
        flag = False
        return flag, None


# 读取csv数据
def read_csv(file_path):
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        codes = [row['secucode'] for row in reader]
        return codes


"""
检查批量画图是否正常。
"""


def m_batch_draw_photo():
    hy_status = codes_mange('hy')
    chy_status = codes_mange('chy')
    bhy_status = codes_mange('bhy')
    if hy_status and chy_status and bhy_status:
        msg = ['batchdrawing', 'normal', '批量画图正常']
        return msg, True
    else:
        msg = ['batchdrawing', 'error', '批量画图异常']
        return msg, False


"""
csv 数据处理 并判断图片时间是否在10分钟之内
"""


def codes_mange(type):
    img_path = sys.path[0] + "/da/static/img/"
    flag, codes = m_csv(type)
    if flag:
        # dir_path ="E:\pyWork\drawPhoto\drawPhoto\da\static\count\\" + now_time_str
        # img_path ="E:\pyWork\drawPhoto\drawPhoto\da\static\img\\"
        td = TreadingDay()
        # 判断是否是交易日
        now_time_str = datetime.datetime.now().strftime("%Y-%m-%d")
        IfTradingDay, trading_date = td.if_TreadingDay_F10(now_time_str)
        now_datetime = datetime.datetime.strptime(now_time_str, "%Y-%m-%d")
        if IfTradingDay is True or trading_date == now_datetime:
            #判断交易时间
            end_15 = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:00:00" % 15
            end_12 = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:10:00" % 13
            start_11 = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:30:00" % 11
            start_9 = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:35:00" % 9
            timeArray_start_9 = time.strptime(start_9, "%Y-%m-%d %H:%M:%S")
            start_int_9 = time.mktime(timeArray_start_9)
            timeArray_end_15 = time.strptime(end_15, "%Y-%m-%d %H:%M:%S")
            end_int_15 = time.mktime(timeArray_end_15)
            timeArray_start_11 = time.strptime(start_11, "%Y-%m-%d %H:%M:%S")
            start_int_11 = time.mktime(timeArray_start_11)
            timeArray_end_12 = time.strptime(end_12, "%Y-%m-%d %H:%M:%S")
            end_int_12 = time.mktime(timeArray_end_12)
            now = time.time()
            if start_int_9 > now or now > end_int_15 or (start_int_11 < now < end_int_12):
                return True

            now_time = datetime.datetime.now()
            time_before = now_time + datetime.timedelta(minutes=-10)
            for index in range(len(codes)):
                if index == 1:
                    break
                code_img_path = img_path + codes[index] + '.png'
                try:
                     stat = os.stat(code_img_path)
                except:
                    logger.exception('图片不存在%s', code_img_path)
                    return False
                stat_time = datetime.datetime.fromtimestamp(stat.st_mtime)
                code_time_s = (stat_time - time_before).total_seconds()
                if int(code_time_s) >= 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return True


"""
监控生成单张图片是否正常
"""


def m_get_one_by_code():
    flag, codes = m_csv('hy')
    png_path = sys.path[0] + "/da/static/img/" + codes[0] + 'flag.png'
    if flag:
        if plan.fs_secucode_png(codes[0], 1, flag=False) is False:
            return False
        else:
            now_time = datetime.datetime.now()
            time_before = now_time + datetime.timedelta(minutes=-1)
            stat = os.stat(png_path)
            stat_time = datetime.datetime.fromtimestamp(stat.st_mtime)
            code_time_s = (stat_time - time_before).total_seconds()
            os.remove(png_path)
            if int(code_time_s) >= 0:
                return ['singledrawing', 'normal', '单张画图正常'],True
            else:
                return ['singledrawing', 'error', '单张画图异常'],False


if __name__ == '__main__':
    m_get_one_by_code()
