# -*- coding: utf-8 -*-
import cx_Oracle
import datetime
import time
from da.dataService.hqService import hqService
from da.utils.configutil import ConfigUtil
from config import logger


class TreadingDay(object):
    # def __init__(self):
    #     # 连接聚源数据库
    #     self.__conn = cx_Oracle.connect('jydb', '123456', '172.20.1.102:1521/jydb')
    #     self.__cursor = self.__conn.cursor()
    # pass
    def if_TreadingDay_oracle(self, date_str):
        __conn = cx_Oracle.connect('jydb', '123456', '172.20.1.102:1521/jydb')
        __cursor = __conn.cursor()
        try:
            sql = "select t.tradingdate,t.iftradingday from QT_TradingDayNew t where t.tradingdate = to_date('" + date_str + "','YYYY-MM-DD') and secumarket=83"
            __cursor.execute(sql)
            rs = __cursor.fetchall()
            # 是否交易日（IfTradingDay）：2 -> 否 ； 1 -> 是
            IfTradingDay = rs[0][1]
            if IfTradingDay == 1:
                # print '是交易日'
                return True, rs[0][0]
            else:
                # print '不是交易日'
                sql2 = "select s.tradingdate,s.iftradingday from (select t.tradingdate,t.iftradingday from QT_TradingDayNew t where " \
                       "t.tradingdate< to_date('" + date_str + "','YYYYMMDD') and secumarket=83 and t.iftradingday=1 order by t.tradingdate desc) s where rownum=1"
                __cursor.execute(sql2)
                rs2 = __cursor.fetchall()
                return False, rs2[0][0]
        except:
            raise RuntimeError
        finally:
            __cursor.close
            __conn.close

    # 请求F10获取交易日信息
    def if_TreadingDay_F10(self, now_time_str):
        try:
            hq = hqService();
            F10Url = ConfigUtil.getconfig('https', 'F10TrainDay')
            data_map = hq.getUrlData(F10Url)
            now_datetime = datetime.datetime.strptime(now_time_str, "%Y-%m-%d")
            # 是否交易日（IfTradingDay）：2 -> 否 ； 1 -> 是
            if data_map is not None and isinstance(data_map, dict):
                results = data_map['results']
                if results[13][now_time_str] == '1':
                    # print '是交易日'
                    start_9 = datetime.datetime.now().strftime("%Y-%m-%d") + " %2d:25:00" % 9
                    now = time.time()
                    timeArray_start_9 = time.strptime(start_9, "%Y-%m-%d %H:%M:%S")
                    start_int_9 = time.mktime(timeArray_start_9)
                    if start_int_9 > now:
                        treadingday_before_datetime = self.getbefore(results)
                        return True, treadingday_before_datetime
                    else:
                        return True, now_datetime
                else:
                    # print '不是交易日'
                    treadingday_before_datetime = self.getbefore(results)
                    return False, treadingday_before_datetime
            else:
                logger.exception("F10数据处理异常,按正常交易日处理")
                return False, now_datetime
        except:
            logger.exception("F10数据处理异常,按正常交易日处理")
            return False, now_datetime

    def getbefore(self, results):
        leng = len(results)
        # 获取最近一交易日
        treadingday_list = []
        for i in xrange(leng):
            result = results[i]
            if result.values()[0] == '1':
                treadingday_list.append(result.keys()[0])
            if i >= 12:
                break
        treadingday_before_datetime = datetime.datetime.strptime(treadingday_list[-1], "%Y-%m-%d")
        return treadingday_before_datetime


if __name__ == '__main__':
    td = TreadingDay()
    print td.if_TreadingDay_F10()
