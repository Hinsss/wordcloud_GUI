from tkinter import *
from tkinter.messagebox import *  # 这是弹出窗口
from tkinter import ttk
from tkinter import scrolledtext
import matplotlib as mpl
import pandas
import matplotlib.pyplot as plt
import numpy as np
import draw_it
import cloud

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.serif'] = ['SimHei']
class MainPage(object):
    def __init__(self, master=None):
            self.root = master  # 定义内部变量root
            self.root.title('简便招聘词云')
            self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小
            self.language = StringVar()
            self.place = StringVar()
            self.salary = StringVar()
            self.table = pandas.read_excel("IT各部分数据.xlsx")
            self.createPage()

    def createPage(self):
        # 创建一个menu
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu.add_command(label='python', command=draw_it.draw_python)  # accelerator 快捷键，  new  点击事件函数
        filemenu.add_command(label='java', command=draw_it.draw_java)
        filemenu.add_command(label='C', command=draw_it.draw_C)
        filemenu.add_command(label='PHP', command=draw_it.draw_PHP)
        filemenu.add_command(label='HTML5', command=draw_it.draw_HTML5)
        filemenu.add_separator()  # 分隔符
        filemenu.add_command(label='总地区分布',command=draw_it.draw_IT)
        menubar.add_cascade(label='IT地区现状', menu=filemenu)

        editmenu = Menu(menubar)
        editmenu.add_command(label='python',command=draw_it.Salary_python)
        editmenu.add_command(label='java',command=draw_it.Salary_java)
        editmenu.add_command(label='C',command=draw_it.Salary_C)
        editmenu.add_command(label='PHP',command=draw_it.Salary_PHP)
        editmenu.add_command(label='HTML5',command=draw_it.Salary_HTML5)
        editmenu.add_separator()  # 分隔符
        editmenu.add_command(label='总薪资分布',command=draw_it.Salary_IT)
        menubar.add_cascade(label='IT薪资水平分布', menu=editmenu)

        wordcloudmenu = Menu(menubar)
        wordcloudmenu.add_command(label='地区词云', command=cloud.word_cloud_places)
        wordcloudmenu.add_command(label='岗位词云', command=cloud.word_cloud_jods)
        wordcloudmenu.add_separator()  # 分隔符
        wordcloudmenu.add_command(label='招聘词云', command=cloud.word_cloud)
        menubar.add_cascade(label='词云可视化', menu=wordcloudmenu)



        aboutmenu = Menu(menubar)
        aboutmenu.add_command(label='作者', command=self.author)  # command  对应的函数定义在前面
        aboutmenu.add_command(label='版权', command=self.about)
        menubar.add_cascade(label='关于', menu=aboutmenu)

        toolbar = Label(self.root, text='招聘网信息', height=1, bg='light sea green')
        toolbar.pack(expand=NO, fill=X)  # 全部填充海蓝色，显示toolbar栏

        lnlabel = Label(self.root, width=3, bg='antique white')
        lnlabel.pack(side=LEFT, fill=Y)

        fm = Frame(self.root)

        fm1 = Frame(fm)
        ttk.Label(fm1, width=8, text="语言").pack(side=TOP)
        languageChosen = ttk.Combobox(fm1, width=10, textvariable=self.language)
        languageChosen['values'] = ('python', 'java', 'PHP', 'HTML5', 'C')  # 设置下拉列表的值
        languageChosen.pack(side=TOP)  # 设置其在界面中出现的位置  column代表列   row 代表行
        languageChosen.current(0)
        fm1.pack(side=LEFT)

        fm2 = Frame(fm)
        ttk.Label(fm2, width=8, text="城市").pack(side=TOP)
        placeChosen = ttk.Combobox(fm2, width=10, textvariable=self.place)
        placeChosen['values'] = ('广州', '深圳', '惠州','东莞','珠海','中山','佛山')
        placeChosen.pack(side=TOP)
        placeChosen.current(0)
        fm2.pack(side=LEFT)

        fm3 = Frame(fm)
        ttk.Label(fm3, width=8, text="初薪资").pack(side=TOP)
        salaryChosen = ttk.Combobox(fm3, width=10, textvariable=self.salary)
        salaryChosen['values'] = ('5000+', '6000+', '7000+', '8000+', '9000+', '10000+')
        salaryChosen.pack(side=TOP)
        salaryChosen.current(0)
        fm3.pack(side=LEFT)

        fm4 = Frame(fm)
        ttk.Label(fm4, width=8, text="确定").pack(side=TOP)
        action = ttk.Button(fm4, text="点击!",command=self.clickMe)
        action.pack(side=TOP)
        fm4.pack(side=LEFT)

        fm.pack(side=TOP)

        gm = Frame(self.root)
        scrolW = 300
        scrolH = 20
        self.scr = scrolledtext.ScrolledText(gm, width=scrolW, height=scrolH, wrap=WORD)
        self.scr.pack()
        gm.pack(side=TOP)

        lnlabel = Label(self.root, width=3, bg='antique white')
        lnlabel.pack(side=BOTTOM, fill=X)
        lnlabel = Label(self.root, width=3, bg='antique white')
        lnlabel.pack(side=RIGHT, fill=Y)

    def clickMe(self):  # 当acction被点击时,该函数则生效
        if self.salary.get() == '5000+':
            money = '50'
        elif self.salary.get() == '6000+':
            money = '60'
        elif self.salary.get() == '7000+':
            money = '70'
        elif self.salary.get() == '8000+':
            money = '80'
        elif self.salary.get() == '9000+':
            money = '90'
        else:
            money = '10'
        table_all = self.table[self.table['语言'].str.contains(self.language.get(), regex=True)]
        table_all = table_all[table_all['城市'].str.contains(self.place.get(), regex=True)]
        table_all = table_all[table_all['工资'].str.contains(money, regex=True)]
        table_all = table_all[['职位', '公司', '工资']]
        value = table_all
        self.scr.delete(0.0, END)
        self.scr.insert(INSERT, value)

    def author(self):  # 将函数与about进行了绑定
        showinfo('作者信息', '本软件由叶国栋，温家奇完成！')

    def about(self):
        showinfo('版权信息。copyright', '本软件归属于叶国栋，温家奇')



