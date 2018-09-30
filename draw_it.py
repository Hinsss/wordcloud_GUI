import matplotlib as mpl
import pandas
import matplotlib.pyplot as plt


def draw_java():
    data = pandas.read_excel('IT各部分数据.xlsx',
                             sheet_name='java', index_col='职位')
    data = data['城市'].value_counts()
    data = pandas.DataFrame(data)
    data = data.head(10)['城市']
    data.plot(kind='barh', figsize=(7, 6), title='java')
    plt.show()


def draw_C():
    data = pandas.read_excel('IT各部分数据.xlsx',
                             sheet_name='C', index_col='职位')
    data = data['城市'].value_counts()
    data = pandas.DataFrame(data)
    data = data.head(10)['城市']
    data.plot(kind='barh', figsize=(7, 6), title='C')
    plt.show()


def draw_PHP():
    data = pandas.read_excel('IT各部分数据.xlsx',
                             sheet_name='PHP', index_col='职位')
    data = data['城市'].value_counts()
    data = pandas.DataFrame(data)
    data = data.head(10)['城市']
    data.plot(kind='barh', figsize=(7, 6), title='PHP')
    plt.show()


def draw_HTML5():
    data = pandas.read_excel('IT各部分数据.xlsx',
                             sheet_name='HTML5', index_col='职位')
    data = data['城市'].value_counts()
    data = pandas.DataFrame(data)
    data = data.head(10)['城市']
    data.plot(kind='barh', figsize=(7, 6), title='HTML5')
    plt.show()


def draw_python():
    data = pandas.read_excel('IT各部分数据.xlsx',
                             sheet_name='python', index_col='职位')
    data = data['城市'].value_counts()
    data = pandas.DataFrame(data)
    data = data.head(10)['城市']
    data.plot(kind='barh', figsize=(7, 6), title='python')
    plt.show()


def draw_IT():
    data = pandas.read_excel('IT各部分数据.xlsx',
                              index_col='职位')
    data = data['城市'].value_counts()
    data = pandas.DataFrame(data)
    data = data.head(20)['城市']
    data.plot(kind='barh', figsize=(7, 6), title='IT')
    plt.show()


def Salary_python():
    data = pandas.read_excel('IT各部分数据.xlsx',
                             sheet_name='python', index_col='职位')
    data = data['工资'].value_counts()
    data = pandas.DataFrame(data)
    data = data.head(10)['工资']
    data.plot(kind='barh', figsize=(7, 6), title='python')
    plt.show()


def Salary_java():
    data = pandas.read_excel('IT各部分数据.xlsx',
                             sheet_name='java', index_col='职位')
    data = data['工资'].value_counts()
    data = pandas.DataFrame(data)
    data = data.head(10)['工资']
    data.plot(kind='barh', figsize=(7, 6), title='java')
    plt.show()


def Salary_C():
    data = pandas.read_excel('IT各部分数据.xlsx',
                             sheet_name='C', index_col='职位')
    data = data['工资'].value_counts()
    data = pandas.DataFrame(data)
    data = data.head(10)['工资']
    data.plot(kind='barh', figsize=(7, 6), title='C')
    plt.show()


def Salary_HTML5():
    data = pandas.read_excel('IT各部分数据.xlsx',
                             sheet_name='HTML5', index_col='职位')
    data = data['工资'].value_counts()
    data = pandas.DataFrame(data)
    data = data.head(10)['工资']
    data.plot(kind='barh', figsize=(7, 6), title='HTML5')
    plt.show()


def Salary_PHP():
    data = pandas.read_excel('IT各部分数据.xlsx',
                             sheet_name='PHP', index_col='职位')
    data = data['工资'].value_counts()
    data = pandas.DataFrame(data)
    data = data.head(10)['工资']
    data.plot(kind='barh', figsize=(7, 6), title='PHP')
    plt.show()


def Salary_IT():
    data = pandas.read_excel('IT各部分数据.xlsx',
                              index_col='职位')
    data = data['工资'].value_counts()
    data = pandas.DataFrame(data)
    data = data.head(20)['工资']
    data.plot(kind='barh', figsize=(7, 6), title='IT')
    plt.show()