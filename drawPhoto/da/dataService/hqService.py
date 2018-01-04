# coding=utf-8
import json
import datetime
import threading
from config import logger

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


# app = create_flask_app('config')


class hqService:
    def getUrlData(self, httpUrl):
        try:
            # "http://apihq.cnstock.com/apihq/min.do?code=" + secucode
            # http://php.cnstock.com/news_new/index.php/codelist/ag
            request = Request(httpUrl)
            data_str = urlopen(request, timeout=10).read()
            data = json.loads(data_str)
            # with open('C:\\Users\\admin\\Desktop\\FeHelper-20171221164431.json') as json_file:
            #     data = json.load(json_file)
            #     return data
            return data
        except:
            logger.info("取出数据失败%s再次请求", httpUrl)
            try:
                request = Request(httpUrl)
                data_str = urlopen(request, timeout=10).read()
                data = json.loads(data_str)
                return data
            except:
                logger.exception("取出数据失败%s",httpUrl)

    # 13:00过后向前减一个半小时
    def delTimeStr(self, str):
        # 是否在交易时间内
        isTime = 0
        str = str[8:10] + ":" + str[10:]
        t = self.timeStr(str)
        time13 = self.timeStr("13:00")
        time113 = self.timeStr("11:30")
        time9 = self.timeStr("09:30")
        time15 = self.timeStr("15:00")
        if t >= time113 and t <= time13:
            isTime = 1
        elif t < time9:
            isTime = 2
        elif t > time15:
            isTime = 3

        if t > time13:
            str = (t - datetime.timedelta(minutes=90)).strftime("%H:%M")
        else:
            pass
        return str, isTime

    def envData(self, data):
        dataMap = {}
        timeData = []
        priceData = []
        amount = []
        lowprice=[]
        highprice=[]
        secName = ""
        lastTime = ""
        # thisMonth = datetime.datetime.now().month
        # thisDay = datetime.datetime.now().day
        # 处理日期 <10的情况 例如 11-7 改成 11-07

        # if thisDay < 10:
        #     thisday_str = '0' + str(thisDay)
        # else:
        #     thisday_str = str(thisDay)
        # if thisMonth < 10:
        #     thisMonth_str = '0' + str(thisMonth)
        # else:
        #     thisMonth_str = str(thisMonth)
        if len(data) > 0:
            # 昨收
            lastTime = data[0][0]
            title_date = lastTime[4:6] + "-" + lastTime[6:8]
            ylastprice = data[0][2]
            secName = data[0][10]
            length = len(data)
            pda = priceData.append
            tda = timeData.append
            aa = amount.append
            lp = lowprice.append
            hp = highprice.append
            for i in xrange(0, length):
                # 交易时间
                time, isTime = self.delTimeStr2(data[i][0])
                # 在交易时间内，而且现价不为0
                if isTime == 0:
                    lp(data[i][7])
                    hp(data[i][6])
                    lastTime = data[i][0]
                    time_15_00 = lastTime[8:]
                    if time_15_00 != '1500':
                        if data[i][1] != 0:
                            # 现价
                            pda(data[i][1])
                        else:
                            # 现价
                            pda(ylastprice)
                    tda(time)
                    # 交易量
                    aa(data[i][8])
                    if time_15_00 == '1500':
                        # print 'dsadada'
                        # # 最新一次交易时间
                        # #解决15：00的时候  由于行情数据的错误导致的画图错误
                        # #如果15:00数据为空，，将14:59的数据赋予15:00的数据
                        data_i = data[i]
                        pda(data_i[1])
                        lp(data_i[7])
                        hp(data_i[6])
                        aa(data_i[8])
                        lastTime = lastTime[4:6] + "-" + lastTime[6:8] + "  " + lastTime[8:10] + ":" + lastTime[10:]
                        break
                    lastTime = lastTime[4:6] + "-" + lastTime[6:8] + "  " + lastTime[8:10] + ":" + lastTime[10:]
                elif isTime == 1:
                    lastTime = title_date + "  " + "11:30"
                elif isTime == 2:
                    lastTime = title_date + "  " + "09:30"
                elif isTime == 3:
                    lastTime = title_date + "  " + "15:00"
                else:
                    pass

        # if lastTime!=None and lastTime!='' and (lastTime.count('-', 0, len(lastTime))!=1 or lastTime.count('-', 0, len(lastTime)) != 1):
        #     self.delTimeStr2(lastTime)

        dataMap['timeData'] = timeData
        dataMap['priceData'] = priceData
        dataMap['amount'] = amount
        dataMap['secName'] = secName
        dataMap['lastTime'] = lastTime
        dataMap['ylastprice'] = ylastprice
        dataMap['lowprice'] = lowprice
        dataMap['highprice'] = highprice
        return dataMap

    def timeStr(self, string):
        t = datetime.datetime.strptime(string, '%H:%M')
        return t

    def delTimeStr2(self, time_str):
        hour = int(time_str[8:10])
        minute = int(time_str[10:])
        isTime = 0
        #
        time_str = time_str[8:10] + ":" + time_str[10:]
        if (hour == 11 and minute > 30) or (hour > 11 and hour < 13):
            isTime = 1
        elif (hour == 9 and minute < 30) or (hour < 9):
            isTime = 2
        elif hour > 15 or (hour == 15 and minute > 0):
            isTime = 3

        if (hour > 13) or (hour == 13 and minute >= 0):
            if minute >= 30:
                if (minute - 30) < 10:
                    time_str = str(hour - 1) + ":0" + str(minute - 30)
                else:
                    time_str = str(hour - 1) + ":" + str(minute - 30)
            elif minute < 30:
                time_str = str(hour - 2) + ":" + str(minute + 30)
        return time_str, isTime


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self):
        hs = hqService()
        t = hs.timeStr("13:00")
        print t
