# coding:utf-8
import math
import numpy as np
from mayavi import mlab
import turtle
#2.1
def t1():
    celsius = input("enter the degree in Celsius:")
    fahrenheit = (9.0 / 5) * celsius + 32
    print fahrenheit


#2.2
def t2():
    radius, height = input("enter the radius and the length of a cylinder:")
    area = radius * radius * math.pi
    volume = area * height
    print  area, volume


def t3():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.write("centre")
    turtle.circle(200)


def t4(x, y, s, length = 20):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    degree = 360 / s
    for i in xrange(s):
        turtle.fd(length)
        turtle.lt(degree)
    turtle.done()

def t5():
    # 玫瑰花的花朵
    [x, t] = np.meshgrid(np.array(range(25)) / 24.0, np.arange(0, 575.5, 0.5) / 575 * 17 * np.pi - 2 * np.pi)
    p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
    u = 1 - (1 - np.mod(3.6 * t, 2 * np.pi) / np.pi) ** 4 / 2
    y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
    r = u * (x * np.sin(p) + y * np.cos(p))
    mlab.mesh(r * np.cos(t), r * np.sin(t), u * (x * np.cos(p) - y * np.sin(p)))

    # 玫瑰花的花杆
    x1 = np.linspace(-0.1, 0, 200)
    y1 = np.linspace(-0.1, 0, 200)
    z1 = np.linspace(-4, 0.0, 200)
    mlab.plot3d(x1, y1, z1, colormap='copper', representation='wireframe')

    mlab.show()
    pass


def t6():
    ch = 'a'
    print ord(ch)
    print chr(98)


def t7():
    turtle.circle(20, steps=4)
    turtle.circle(30, steps=5)
    turtle.circle(40, steps=6)
    turtle.circle(50, steps=7)
    turtle.done()

if __name__ == '__main__':
    #t2()
    #t3()
    #t4(0, 0, 5)
    #t5()
    #t6()
    t7()
