# encoding: utf-8

'''
@author: zhu

@file: test.py

@time: 2018/6/27 14:04

@desc:

'''
import requests, re
from lxml import etree
from bs4 import BeautifulSoup
from distutils.filelist import findall
import numpy as np
import  pandas as pd
import xlrd
import os
result_project = []
result_type = []
result_status = []
result_address = []
result_type1 = []
result_specific = []
result_money = []
result_s = []
result_name = []
result_piece = []
data_arr=[]

url = 'https://bj.fang.lianjia.com/loupan/pg{}/'
path_project = '/html/body/div[4]/ul[2]/li/div/div[1]/a/text()'
path_type = '/html/body/div[4]/ul[2]/li/div/div[1]/span[1]/text()'
path_status = '/html/body/div[4]/ul[2]/li/div/div[1]/span[2]/text()'
path_address = '/html/body/div[4]/ul[2]/li/div/div[2]/span[1]/text()'
path_type1 = '/html/body/div[4]/ul[2]/li/div/div[2]/span[2]/text()'
path_specific_address_ = '/html/body/div[4]/ul[2]/li/div/div[2]/a/text()'
path_money = '/html/body/div[4]/ul[2]/li/div/div[6]/div[2]/text()'
path_s = '/html/body/div[4]/ul[2]/li/div/div[3]/span/text()'
path_name = '/html/body/div[4]/ul[2]/li/div/div[4]/span/text()'
path_piece = '/html/body/div[4]/ul[2]/li/div/div[6]/div[1]/span[1]//text()'



for i in range(1):
    res = requests.get(url.format(i)).text
    tree = etree.HTML(res)
    xpath_project = tree.xpath(path_project)
    xpath_type = tree.xpath(path_type)
    xpath_status = tree.xpath(path_status)
    xpath_address = tree.xpath(path_address)
    xpath_type1 = tree.xpath(path_type1)
    xpath_sep_address = tree.xpath(path_specific_address_)
    xpath_money = tree.xpath(path_money)
    xpath_s = tree.xpath(path_s)
    print(type(xpath_s))
    # xpath_s=str(xpath_s).split(' ')[1].split('m')[0]

    xpath_name = tree.xpath(path_name)
    xpath_piece = tree.xpath(path_piece)
    print(xpath_s)

    result_project += xpath_project
    result_type += xpath_type
    result_status += xpath_status
    result_address += xpath_address
    result_type1 += xpath_type1
    result_specific += xpath_sep_address
    result_money += xpath_money
    result_s += xpath_s
    result_name += xpath_name
    result_piece += xpath_piece

    data_arr.append(result_project)
    data_arr.append(result_type)
    data_arr.append(result_status)
    data_arr.append(result_address)
    data_arr.append(result_type1)
    data_arr.append(result_specific)
    data_arr.append(result_money)
    data_arr.append(result_s)
    data_arr.append(result_piece)
    data=np.mat(data_arr).T
    juzhen=[]
    for i in data_arr:
        data=np.mat(i).T
        juzhen.append(data)
        # print(data)
        print(type(data))
    data1=np.hstack((juzhen[0],juzhen[1],juzhen[2],juzhen[3],juzhen[4],juzhen[5],juzhen[7],juzhen[8]))
    naems=['项目','业态','状态','地址','地址2','具体地址','建筑面积','单价/元']
    data1=pd.DataFrame(data1,columns=naems)
    data1.to_excel('C:\\Users\\anzhi\\Desktop\\slianjia.xlsx', 'w++')

    print(data1)


    # url='https://bj.fang.lianjia.com/loupan/pg1/'
    # res=requests.get(url).text
    #
    #
    # result =re.findall('"(<span class="agent">.*?)".*?</span>',res)
    # print(result)
    #     def data_write(self):
