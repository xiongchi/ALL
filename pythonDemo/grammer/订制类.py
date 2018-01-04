# -*- coding: utf-8 -*-


class Man(object):
    def __init__(self, name):
        self.name = name

    #相当于java 中的toString()
    def __str__(self):
        return 'Student object (name=%s)'%self.name

    #__repr__ = __str__


"""
__getitem__ 实现取出第几个数 f[i]
"""
class Fib(object):
   def __getitem__(self, item):
       a, b = 1, 1
       for x in range(item):
           a, b = b, a + b
       return a

if __name__ == '__main__':
    pass
    # man = Man('hello world')
    # print man
    # f = Fib()
    # for i in f:
    #     print i




"""
__call__
一个对象实例可以有自己的属性和方法，当我们调用实例方法时，
我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
"""
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student("tom")
s()

"""
__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()
"""

