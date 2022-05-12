# -*- codeing = utf-8 -*-
# @Time : 2022/5/12 21:33
# @Author : keaihh
# @File : 6_for_while.py
# @Software : PyCharm

'''
for i in range(5):
    print(i)
'''

'''
for i in range(0, 11,3):   #从0开始到11结束,一次加3
    print(i)
'''
'''
for i in range(-10,-100,-30):
    print(i)
'''
'''
name="chengdu"
for x in name:
    print(x,end="\t")
    # print(x)
'''
'''
a=["aa","bb","cc","dd"]
for i in range(len(a)):
    print(i,a[i])
'''





'''
i=0
while i<5:
    print("当前是第%d次执行循环"%(i+1))
    print("i=%d"%i)
    i+=1
'''

'''
# 打印一到一百的和
i=1
a=0
while i<101:
    print("i=%d"%i)
    a=i+a
    i+=1
print(a)
'''

'''
count = 0
while count<5:
    print(count,"小于5")
    count+=1
else:
    print(count,"大于或等于5")
'''
'''
i=0
while i<10:
    i=i+1
    print("-"*30)
    if i==5:
        break
    print(i)
'''

i=0
while i<10:
    i=i+1
    print("-"*30)
    if i==5:
        continue
    print(i)


