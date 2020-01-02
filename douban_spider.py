# -*- coding: utf-8 -*-                                                                                                                                                                         #关注微信公众号“和你学Python”可获取更多资源

#导入selenium的webdriver
from selenium import webdriver

#把网址赋值给url
url = 'https://movie.douban.com/top250'

#创建一个控制Chrome的对象
wd = webdriver.Chrome()

#获取页面
wd.get(url)

#创建一个空列表
data = []

#创建获取数据的函数
def get_data():
    for i in range(10):
        #获取所有class为info的div节点
        div_list = wd.find_elements_by_css_selector('div.info')

        #遍历div获取该页的内容
        for div in div_list:
            #创建一个空字典
            dic = {}
            
            #获取电影名
            dic['title'] = div.find_element_by_css_selector('span.title').text
            
            #获取评分
            dic['rating_num'] = div.find_element_by_css_selector('span.rating_num').text
            
            #获取简介
            dic['inq'] = div.find_element_by_css_selector('span.inq').text

            #把字典添加入列表
            data.append(dic)

        #最后一页不点击换页
        if i != 9:
            wd.find_element_by_link_text('后页>').click()
        print('第' + str(i + 1) + '页数据已获取')
            
#定义保存的函数
def save(lst):
    #以写入方式打开一个文件
    with open(r'C:\Users\Administrator\Desktop\data.txt', 'w') as file:
        #把列表里的字典输入到文件里
        for dic in lst:
            for key, value in dic.items():
                file.write(key + '：' + str(value) + ' ')
            file.write('\n')
    print('文件已保存')

if __name__ == '__main__':
    print('豆瓣爬虫开始运行')
    get_data()
    save(data)
