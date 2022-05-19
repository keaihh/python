# -*- codeing = utf-8 -*-
# @Time : 2022/5/19 16:26
# @Author : keaihh
# @File : 8_1_2_list.py
# @Software : PyCharm

# nameList=[]  #定义一个空列表

'''
nameList=["小张","小李","小王"]

testList=[1,"测试"]

print(nameList[0])
print(nameList[1])
print(nameList[2])

for name in nameList:
    print(name)

print(len(nameList))


length=len(nameList)
i=0
while i<length:
    print(nameList[i])
    i+=1

'''
import random

nameList=["小张","小李","小王"]

# 增：  【append】
'''
print("-----增加前-----")
for name in nameList:
    print(name)

nameTemp=input("请输入添加学生的信息：")
nameList.append(nameTemp)

print("-----增加后-----")
for name in nameList:
    print(name)
'''


'''
a=[1,2]
b=[3,4]
a.append(b)
print(a)  # [1, 2, [3, 4]]

a.extend(b)
print(a)  # [1, 2, [3, 4], 3, 4]

'''

#增  【insert】
'''
a=[0,1,2]
a.insert(1,3)
print(a)  # [0, 3, 1, 2]
'''

# 删 【del】 【pop】【remove】
'''
moveName=["加比勒海盗","骇客帝国","第一滴血","指环王","速度与激情"]
print("-----删除前-----")
for name in moveName:
    print(name)

del moveName[0]  #在指定位置删除一个元素
moveName.pop()   #弹出最后一个
moveName.remove("指环王") #直接删除指定内容的元素，内容重复删除第一个


print("-----删除后-----")
for name in moveName:
    print(name)
'''

# 改
'''
print("----修改前，名单列表数据----")
for name in nameList:
    print(name)
nameList[1]="小红"   #修改指定下标元素内容
print("-----修改后-----")
for name in  nameList:
    print(name)
'''

'''
# 变  【in】【not in】
findName=input("请输入要查找的学生姓名：")
if findName in nameList:
    print("找到了")
else:print("找不到")
'''

'''
myList=["a","b","c","a","b"]
print(myList.index("a",1,4))   #可以查找指定下标范围元素，并且返回找到对应元素的下标
print(myList.index("a",1,3))   #范围区间 左闭右开 [1 ,3)
                               #找不到会报错

print(myList.count("c"))       #统计某个元素出现几次
'''

# 反转和排序
'''
a=[1,4,2,3]
print(a)
a.reverse()  # 将列表所有元素反转
print(a)

a.sort()  #升序
print(a)
a.sort(reverse=True) #降序
print(a)
'''

schoolNames=[[],[],[]]  #三个空列表
schoolName=[["北京","清华"],["南开","天津","天津师范"],["山东","中国海洋"]]
print(schoolName[0])  #打印第一个列表内容
print(schoolName[0][0]) #打印第一个列表内容

offices=[[],[],[]]

names=["A","B","C","D","E","F","G","H"]
for name in names:
    index=random.randint(0,2)
    offices[index].append(name)
i=1
for office in offices:
    print("办公室%d的人数为：%d"%(i,len(office)))
    i+=1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*20)








