# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

# 生成指定大小的文件

import os
import random

def genSizeFile(fileName, fileSize):
    #file path
    filePath="Data"+fileName+".doc"

    # 生成固定大小的文件
    # date size
    ds=0
    with open(filePath, "w", encoding="utf8") as f:
        while ds<fileSize:
            f.write(str(round(random.uniform(-1000, 1000),2)))
            # f.write("\n")
            ds=os.path.getsize(filePath)
    # print(os.path.getsize(filePath))

# start here.
genSizeFile("CS",1.9*1024*1024)