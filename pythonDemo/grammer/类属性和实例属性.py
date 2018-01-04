# -*- coding: utf-8 -*-
class Student(object):
    count = 1
    name = "china"

    def count_add(self):
        self.count += 1
        self.name = "world"

if __name__ == '__main__':
    s1 = Student()
    print s1.count
    s1.count_add()
    print s1.count
    s2 = Student()
    print s2.count
    print Student.name
    #类属性会覆盖实例属性
    print s2.name
    """
    从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
    因为相同名称的实例属性将屏蔽掉类属性，
    但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
    """


