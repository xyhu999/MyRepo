#coding=utf-8 
fr = open('../data/multiline2oneline','r+')
resultline=''
splitchar=','
for line in fr.readlines():
    curLine = line.strip()
    resultline+=splitchar+curLine
fr.writelines('\n'+"运行结果如下：\n"+resultline)