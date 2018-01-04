# coding=utf-8
def set_passline(passline):
    def cmp(val):
        if val < passline:
            print "%d failed"%val
        else:
            print "%d pass"%val
    return cmp


#设置passline = 100
fun_100 = set_passline(60)
#passline = 100 存放在__closure__属性中 如下地址
#(<cell at 0x0000000001DE9E88: int object at 0x0000000001DB82C0>,)
#返回的是cmp函数地址 其中passline变量是fun_100.__closure__地址中的值
print fun_100.__closure__
fun_100(89)
fun_150 = set_passline(90)
print fun_150.__closure__
fun_150(89)
