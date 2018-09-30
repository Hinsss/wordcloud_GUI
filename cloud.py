import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud ,ImageColorGenerator#词云
import PIL
from os import path
import jieba


def word_cloud_places():
    d = path.dirname(__file__)
    back_coloring_path = r"bb.jpg"  # 设置背景图片路径
    back_coloring = np.array(PIL.Image.open(path.join(d, back_coloring_path)))  # 设置背景图片
    text_path = '地区.txt'  # 设置要分析的文本路径
    #
    wc = WordCloud(font_path='simhei.ttf',
                   background_color="white",  # 背景颜色
                   max_words=2000,  # 词云显示的最大词数
                   mask=back_coloring,  # 设置背景图片
                   max_font_size=100,  # 字体最大值
                   random_state=42,
                   width=100, height=90, margin=2,  # 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
                   )
    text = open(path.join(d, text_path)).read()
    wordlist = jieba.cut(text, cut_all=False)
    # cut_all, True为全模式，False为精确模式
    wordlist_space_split = ' '.join(wordlist)

    wc.generate(wordlist_space_split)
    image_colors = ImageColorGenerator(back_coloring)
    plt.figure()
    # 以下代码显示图片
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def word_cloud():
    d = path.dirname(__file__)
    back_coloring_path = r"bb.jpg"  # 设置背景图片路径
    back_coloring = np.array(PIL.Image.open(path.join(d, back_coloring_path)))  # 设置背景图片
    text_path = 'test.txt'  # 设置要分析的文本路径
    #
    wc = WordCloud(font_path='simhei.ttf',
                   background_color="black",  # 背景颜色
                   max_words=2000,  # 词云显示的最大词数
                   mask=back_coloring,  # 设置背景图片
                   max_font_size=100,  # 字体最大值
                   random_state=42,
                   width=100, height=90, margin=2,  # 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
                   )
    text = open(path.join(d, text_path)).read()
    # 首先使用 jieba 中文分词工具进行分词
    wordlist = jieba.cut(text, cut_all=False)
    # cut_all, True为全模式，False为精确模式
    wordlist_space_split = ' '.join(wordlist)

    wc.generate(wordlist_space_split)
    image_colors = ImageColorGenerator(back_coloring)
    plt.figure()
    # 以下代码显示图片
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def word_cloud_jods():
    d = path.dirname(__file__)
    back_coloring_path = r"bb.jpg"  # 设置背景图片路径
    back_coloring = np.array(PIL.Image.open(path.join(d, back_coloring_path)))  # 设置背景图片
    text_path = '岗位.txt'  # 设置要分析的文本路径
    #
    wc = WordCloud(font_path='simhei.ttf',
                   background_color="black",  # 背景颜色
                   max_words=2000,  # 词云显示的最大词数
                   mask=back_coloring,  # 设置背景图片
                   max_font_size=100,  # 字体最大值
                   random_state=42,
                   width=100, height=90, margin=2,  # 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
                   )
    text = open(path.join(d, text_path)).read()
    wordlist = jieba.cut(text, cut_all=False)
    # cut_all, True为全模式，False为精确模式
    wordlist_space_split = ' '.join(wordlist)

    wc.generate(wordlist_space_split)
    image_colors = ImageColorGenerator(back_coloring)
    plt.figure()
    # 以下代码显示图片
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
