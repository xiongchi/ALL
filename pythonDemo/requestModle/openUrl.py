# coding=utf-8
try:
    from urllibDemo.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


#访问url 并且 显示html
def open_url(path):
    request = Request(path)
    data = urlopen(request).read()
    print data

if __name__ == '__main__':
    path = "https://www.baidu.com/"
    open_url(path)