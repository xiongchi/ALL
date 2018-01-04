# coding:utf-8
"""
装饰器
"""


def my_deco(func):
    def in_deco(x,y):
        print "in_deco"
        return func(x,y)
    return in_deco


#my_deco(my_sum) -> in_deco(x,y) -> my_sum(x,y)
@my_deco
def my_sum(x, y):
    return x+y

#my_sum(x, y)相当于调用in_deco(x, y)
my_sum(1, 2)
print my_sum(3, 4)


class WhatFor(object):

    #在此对象下使用 可用于对象的计数
    @classmethod
    def it(cls):
        print "it is %s"%cls

    #全局
    @staticmethod
    def commfunc():
        print "it's common"

    #私有方法
    def __privatefunc(self):
        #私有变量
        self.__name = "hello"
        print "I'm private"

"""
 1.@classmethod 是一个函数修饰符，它表示接下来的是一个类方法，
 而对于平常我们见到的则叫做实例方法。 类方法的第一个参数cls，而实例方法的第一个参数是self，表示该类的一个实例。 

 2.普通对象方法至少需要一个self参数，代表类对象实例

 3.类方法有类变量cls传入，从而可以用cls做一些相关的处理。
   并且有子类继承时，调用该类方法时，传入的类变量cls是子类，而非父类。 
   对于类方法，可以通过类来调用，就像C.f()，有点类似C＋＋中的静态方法, 
   也可以通过类的一个实例来调用，就像C().f()，这里C()，写成这样之后它就是类的一个实例了。
   所以我们在写类的方法的时候如果要传2个参数，
   在类中定义方法的时候要写三个加一个cls或self其中cls可以点出用@classmethod的方法，self可以点出未用@classmethod方法
"""

if __name__ == '__main__':
    wf = WhatFor()
    wf.it()
    WhatFor.commfunc()
    WhatFor.it()

