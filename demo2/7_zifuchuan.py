# -*- codeing = utf-8 -*-
# @Time : 2022/5/19 15:13
# @Author : keaihh
# @File : 7_zifuchuan.py
# @Software : PyCharm

'''
word='字符串'
sentence="这是一个句子"
paragraph="""
     这是一个段落
     可以由多行组成
"""
print(word)
print(sentence)
print(paragraph)

'''

'''
# my_str="I'm a student"
my_str='I\'m a student'
print(my_str)
'''

'''
my_str="Jason said \"I like you\""
my_str='Jason said \"I like you\"'
print(my_str)
'''

'''
str="chengdu"
print(str)         # chengdu
print(str[0:6])    #chengd
print(str[0])      #c
print(str[1:7:2])  #[起始位置:结束位置:步进值]   hnd
'''

str="chengdu"
print(str[5:])  # du
print(str[:5])  #cheng
print(str+"，你好")  #chengdu，你好
print(str*3)     #chengduchengduchengdu
print("hello\nchengdu")  #\n会换行
print(r"hello\nchengdu") #前面加r会直接输出