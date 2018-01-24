#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   {taowang7}
 
@License :   (C) Copyright 2013-2017, {iflytek}
 
@Contact :   {taowang7@iflytek.com}
 
@Software:   IntelliJ IDEA
 
@File    :   test.py
 
@Time    :   2018/1/16 0016 15:39
 
@Desc    :
 
'''

default_min = 10


def get(value, minute=default_min):
    print value, minute


if __name__ == "__main__":
    # values = 12
    # default_min = 5
    # get(values,default_min)
    # import datetime
    #
    # file_list = datetime.datetime.now() + datetime.timedelta(minutes=-5)
    # print file_list.year
    # print file_list.month
    # print file_list.day
    # print file_list.hour
    # print file_list.minute
    # print "/user/taowang7/out/transbrain/anhui/hefei/stander_data/{}/{:02}/{:02}/{:02" \
    #       "}/{:02}/".format(file_list.year,file_list.month,file_list.day,file_list.hour,file_list.minute)
    import requests
    response = requests.get("http://api.map.baidu.com/direction/v2/transit?origin=40.056878,116.30815&destination=31.222965,121.505821&ak=96o4fmSE6kYDLAUkULLGDhEyqbhkwQtx")
    print response.text