#coding:utf-8
def my_sum(*args):
    return sum(args)


def my_average(*args):
    return sum(args)/len(args)


#传入函数 相当于aop
def dec(func):
    def in_dec(*args):
        if len(args) == 0:
            return 0
        for val in args:
            if not isinstance(val,int):
                return 0
        return func(*args)
    return in_dec

my_sum(1,2,3)
my_sum = dec(my_sum)
my_average = dec(my_average)

print my_sum(1,2,3,4,5)
print my_sum(1,2,3,'4')
print my_average(1,2,3,4)
print my_average(1,2,3,'5')
