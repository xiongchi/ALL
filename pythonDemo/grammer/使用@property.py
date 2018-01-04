# -*- coding: utf-8 -*-
class Student(object):
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer')

        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100')

        self.__score = score

    @property
    def age(self):
        return self.age

s = Student()
s.score = 60
print s.score

s.score = 1000  #抛出ValueError
print s.score

"""
age 为只读属性
@property的实现比较复杂，我们先考察如何使用。
把一个getter方法变成属性，只需要加上@property就可以了，
此时，@property本身又创建了另一个装饰器@score.setter，
负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
"""
