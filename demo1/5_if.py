# -*- codeing = utf-8 -*-
# @Time : 2022/5/12 20:35
# @Author : keaihh
# @File : 5_if.py
# @Software : PyCharm

# 石头剪刀布
import random
b=random.randint(0,2)
a=int(input("请输入：剪刀（0）、石头（1）、布（2）："))
print("你的输入为：",a)
print("随机生成数字为：",b)
if a==0:
    if b==1:
        print("哈哈，你输了")
    elif b==0:
        print("平局")
    elif b==2:
        print("你赢了")
if a==1:
    if b==1:
        print("平局")
    elif b==0:
        print("你赢了")
    elif b==2:
        print("你输了")
if a==2:
    if b==2:
        print("平局")
    elif b==0:
        print("你输了")
    elif b==1:
        print("你赢了")



