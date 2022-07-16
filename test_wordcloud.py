# -*- codeing = utf-8 -*-
# @Time :  16:48
# @Author : JIN XIUSHU
# @File : test_wordcloud.py
# @Software : PyCharm

import jieba  # 将一个句子变成很多个词
from matplotlib import pyplot as plt  # 绘图，可视化
from wordcloud import WordCloud       # 词云
from PIL import Image                 # 图片处理
import numpy as np                    # 矩阵运算
import sqlite3                        # 数据库

#准备词云所需的文字
con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'select instroduction from movie'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
cur.close()
con.close()

cut = jieba.cut(text)
string = ""
for item in cut:
    if len(item) > 1:
        string = string + " " + item
print(string)

img = Image.open(r'.\static\img\img.png')  # 打开遮罩图片
img_array = np.array(img)  # 将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='STXINGKA.TTF'  # 字体所在位置： C:\Windows\Fonts
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')  # 关闭坐标轴

plt.savefig(r'.\static\img\word.jpg', dpi=500)





