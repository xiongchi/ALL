# -*- coding: utf-8 -*-
class PrivateVar:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class PrivateVar2:
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender


if __name__ == '__main__':
    Pv = PrivateVar("hello", "world")
    print Pv.name
    print Pv.gender
    Pv.name = "你好"
    print Pv.name
    Pv2 = PrivateVar2('great','China')
    #print Pv2.__name   #__name 加__表示私有变量 不能直接访问
    #内部将__name变为_PrivateVar2__name 不推荐这样访问
    #可以加get set方法
    print Pv2._PrivateVar2__name
