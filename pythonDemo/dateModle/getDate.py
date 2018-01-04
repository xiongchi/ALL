# coding=utf-8
import datetime


#获取当前时间
def get_now_date():
    nowTime = datetime.datetime.now()
    year = nowTime.year
    date = nowTime.date()
    time = nowTime.time()
    print nowTime,year,date,time

#设置时间
def set_date():
    setDate = datetime.datetime(2017,11,30,10,31,00)
    #向前减去90分钟
    subTime = setDate - datetime.timedelta(minutes=90)
    print setDate,subTime


def str_time():
    nowTime = datetime.datetime.now()
    #date -> 字符串
    time_str = datetime.datetime.strftime(nowTime,"%Y-%m-%d %H:%M:%S")
    print time_str
    date_time = datetime.datetime.strptime(time_str,"%Y-%m-%d %H:%M:%S")
    print date_time
    pass


if __name__ == '__main__':
    get_now_date()
    set_date()
    str_time()