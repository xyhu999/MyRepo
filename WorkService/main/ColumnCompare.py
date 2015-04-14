#coding=utf-8 
from numpy import *
from Levenshtein import *

#分割字符
def getSplitChars(str):
    chars=[]
    for i in str:
        if not (i>='a'and i<='z' or i>='0' and i<='9' or i=='_' or i>='A' and i<='Z' or i=='.'):
            chars.append(i)
    return set(chars)

def my_split(str): 
    splitchars=getSplitChars(str)
#    print splitchars
    for i in splitchars:
        str = str.replace(i,' ')
    list1 = str.split()
    return list1

fr_source=open('../data/compareColumn1')
fr_des=open('../data/compareColumn2')
fr_res=open('../dataResult/compareColumn_r','w')
columns1=[]
columns2=[]

for line1 in fr_source.readlines(): 
    cur_line1=my_split(line1)
    for item1 in cur_line1:
        columns1.append(item1)

for line2 in fr_des.readlines():
    cur_line2=my_split(line2)
    for item2 in cur_line2:
        columns2.append(item2)

class columnsDis:
    columnA=''
    columnB=''
    dis=0

result=[]

cnt=40  #显示时的调整


for item1 in columns1:
    for item2 in columns2:
        temp=columnsDis()
        temp.columnA=item1
        temp.columnB=item2
        temp.dis=distance(item1,item2)
        result.append(temp)

result.sort(key=lambda x:x.dis, reverse=False)

for item in result:
    if item.columnA in columns1 and item.columnB in columns2:
        cnt_null_a=cnt-len(item.columnA)
        cnt_null_b=cnt-len(item.columnB)
        all_null_a=''
        all_null_b=''
        for i in range(cnt_null_a):
            all_null_a+=' '
        for i in range(cnt_null_b):
            all_null_b+=' '
        fr_res.writelines(item.columnA+all_null_a+item.columnB+all_null_b+str(item.dis)+'\n') 
        columns1.remove(item.columnA)
        columns2.remove(item.columnB)

if len(columns1)==0:
    for item in columns2:
        all_null=''
        for i in range(cnt):
            all_null+=' '
        fr_res.writelines(all_null+item+'\n')
        
if len(columns2)==0:
    for item in columns1:
        all_null=''
        for i in range(cnt):
            all_null+=' '
        fr_res.writelines(item+all_null+'\n')