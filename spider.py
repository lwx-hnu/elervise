# -*- coding: utf-8 -*-
#允许中文注释
#需要提取文本夹下所有文本的一些信息(***有些需要转换格式****)，存到一个新文件res.txt中

import re #正则模块
import os #文件处理模块
import json
import string  #字符串


fres = open('C:\\Users\\ASUS\\Desktop\\Res.txt', 'w',encoding='utf-8')
rootdir = 'C:\\Users\\ASUS\\Desktop\\log'
for parent, dirnames, filenames in os.walk(rootdir):
    for filename in filenames:
        #print filename
        fres.write(filename+'\n')  #记录下文件名，便于代码纠错
        # 提取hostname/sysname
        f = open('C:\\Users\\ASUS\\Desktop\\log\\'+str(filename),encoding='utf-8')
        lines = f.readlines()  # .readlines() 自动将文件内容分析成一个行的列表，加快编译速度
        for line in lines:
            pattern = re.compile('(hostname|sysname).*')  # s:space;()分组
            match = pattern.match(line)
            if match:
                # 使用Match获得分组信息
                fres.write(match.group() + '\n')  # Ctrl /可以注释多行
        f.close()

        # 提取uptime，将格式转换为days
        f1 = open('C:/Users/ASUS/Desktop/log/'+str(filename),encoding='utf-8')  # 重新打开，不然无法成功写入
        lines = f1.read()
        t = re.findall(r'plastic.*?\.', lines,re.S)  # findall进行正则匹配，不知为何compile不行了o.o
        # .：非换行任意字符，+：1次或任意次数；*：前一个字符0次或任意次
        t_convert = ''.join(t)  # list转string
        list = t_convert.split('.')  # 根据空格切片
        for line in list:
            fres.write(line+ '\r\n')  # 需进行类型转换
        f1.close()
fres.close()
