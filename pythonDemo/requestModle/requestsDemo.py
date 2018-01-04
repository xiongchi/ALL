# coding:utf-8
import requests

URL = "http://www.baidu.com"


#使用requests 简单get请求
def use_simple_requests():
    response = requests.get(URL)
    print response.headers
    print response.text


#使用requests 带参数的get请求
def use_params_requests():
    params = {'param1': 'hello', 'param2': 'world'}
    response = requests.get(URL,params=params)
    print response.headers
    print response.text
    print response.status_code
    print response.cookies


if __name__ == '__main__':
    # use_simple_requests()
    use_params_requests()