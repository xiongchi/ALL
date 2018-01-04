# -*- coding: utf-8 -*-
from types import MethodType


class Student(object):
    pass


 # 定义一个函数作为实例方法
def set_age(self, age):
    self.age = age
s = Student()

# 动态给实例绑定一个属性
s.name = 'tom'
print s.name

#给一个实例绑定的方法，对另一个实例是不起作用的
s.set_age = MethodType(set_age, s)
s.set_age(25)
print s.age


def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(2)
print s.score

#为了给所有实例都绑定方法，可以给class绑定方法
#给class绑定方法后，所有实例均可调用
s2 = Student()
s2.set_score(5)
print s2.score


"""
使用__slots__只允许对Student实例添加name和age属性 
定义一个特殊的__slots__变量，来限制该class实例能添加的属性
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
"""
class Friend(object):
    __slots__ = ('name', 'age')

f = Friend()
f.name = 'tom'
f.age = 2
# f.score = 3   #添加score属性出错



