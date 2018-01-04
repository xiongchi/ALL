# coding=utf-8
from PIL import Image,ImageFilter,ImageEnhance
import time
import math

def get_message():
    im = Image.open("sz000020.png")
    #类型,大小,格式
    print im.format,im.size,im.mode
    # 设置要拷贝的区域
    box = (100,100,200,200)
    # 将im表示的图片对象拷贝到region中，大小为(400*400)像素。
    # 这个region可以用来后续的操作(region其实就是一个Image对象)，
    # box变量是一个四元组(左，上，右，下)。
    region = im.crop(box)
    #将图片旋转180度
    region = region.transpose(Image.ROTATE_180)
    #在看图软件中打开
    #region.show()
    # 粘贴box大小的region到原先的图片对象中
    im.paste(region, box)
    #im.show()


def rgb_op():
    # 分割成三个通道
    im = Image.open("sz000020.png")
    r, g, b, a = im.split()
    r.show()
    g.show()
    b.show()
    a.show()
    # 将b,r两个通道进行翻转
    im = Image.merge("RGBA", (a,b, r, g))
    im.show()


def img_op():
    im = Image.open("sh600401.png")
    #改变像素
    out = im.resize((550,300))
    #逆时针旋转45度
    out = out.rotate(45)
    out.show()


def img_filter():
    im = Image.open("sz000020.png")
    #滤镜模糊
    #out = im.filter(ImageFilter.BLUR)
    #加黑
    #out = im.filter(ImageFilter.EMBOSS)
    #out = im.filter(ImageFilter.FIND_EDGES)
    out = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
    out.show()


def point_op():
    im = Image.open("sz000020.png")
    out = im.point(lambda i : i * 1.2)
    out.show()


def imgEnhance_op():
    starttime = time.time()
    im = Image.open("sz000020.png")
    enh = ImageEnhance.Contrast(im)
    enh.enhance(2.0).save("b.png")
    endtime = time.time()
    print str(endtime - starttime)


def resize_img():
    im = Image.open("sz000020.png")
    out = im.resize((1280, 1280))
    out.show()
    out.save('1111.png')


if __name__ == '__main__':
    print math.ceil(0.02)
    #resize_img()
    #imgEnhance_op()
    #point_op()
    #img_filter()
    #img_op()
    #rgb_op()
    #get_message()