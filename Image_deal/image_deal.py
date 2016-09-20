#-*- coding:utf-8 -*-
import Image
from pytesser.pytesser import *

# name = '1.jpg'
# #打开图片
# im = Image.open('1.jpg')
# #转化到亮度
# imgry = im.convert('L')
# imgry.save('g'+name)
# #二值化
# table = []
# out = imgry.point(table,'1')
# out.save('b'+name)
# #识别
# text = image_to_string(out)
# #识别对吗
# text = text.strip()
# text = text.upper()
#
# print text

print image_file_to_string('1.jpg')
