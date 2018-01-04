# coding:utf-8
import urllib
import urllib2

URL = "http://www.baidu.com"


#最基本不带参数请求
def use_simple_urllib2():
    response = urllib2.urlopen(URL)
    print response.info()
    print ">>>>>>>>>>>>>>>>>>>>>>>>>"
    print ''.join([line for line in response.readlines()])


#带参数的请求
def use_params_urllib2():
    #构造请求参数
    params = urllib.urlencode({'param1':'hello','param2':'world'})
    print params
    #发送请求
    response = urllib2.urlopen('?'.join([URL, '%s'])%params)
    print response.getcode()
    print ''.join([line for line in response.readlines()])


if __name__ == '__main__':
    #use_simple_urllib2()
    use_params_urllib2()