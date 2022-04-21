# -*- coding: utf-8 -*-

"""
@Time : 2022/4/21
@Author : yan
@File : make_txt
@Description : 
"""
# -*- coding:utf-8 -*
import os
import random

trainval_percent = 0.3  #训练验证集比例
train_percent = 0.9
xmlfilepath = 'data/Annotations'
txtsavepath = 'data/ImageSets'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)  #统计所有的标注文件
list = range(num)
tv = int(num * trainval_percent)  # 设置训练验证集的数目
tr = int(tv * train_percent)      # 设置训练集的数目
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

# txt 文件写入的只是xml 文件的文件名（数字），没有后缀，如下图。
ftrainval = open('data/ImageSets/trainval.txt', 'w')
ftest = open('data/ImageSets/test.txt', 'w')
ftrain = open('data/ImageSets/train.txt', 'w')
fval = open('data/ImageSets/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
