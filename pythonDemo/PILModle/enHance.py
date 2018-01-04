# coding=utf-8
from PIL import Image
from PIL import ImageEnhance


def open_img():
    # 原始图像
    image = Image.open('img/IOU.jpg')
    image.show()
    return image


def bri_enh():
    # 亮度增强
    image = open_img()
    enh_bri = ImageEnhance.Brightness(image)
    brightness = 2.0
    image_brightened = enh_bri.enhance(brightness)
    image_brightened.show()


def color_enh():
    # 色度增强
    image = open_img()
    enh_col = ImageEnhance.Color(image)
    color = 1.5
    image_colored = enh_col.enhance(color)
    image_colored.show()


def con_enh():
    # 对比度增强
    image = open_img()
    enh_con = ImageEnhance.Contrast(image)
    contrast = 15
    image_contrasted = enh_con.enhance(contrast)
    image_contrasted.show()


def sha_enh():
    # 锐度增强
    image = open_img()
    enh_sha = ImageEnhance.Sharpness(image)
    sharpness = 15.0
    image_sharped = enh_sha.enhance(sharpness)
    image_sharped.show()

if __name__ == '__main__':
    sha_enh()