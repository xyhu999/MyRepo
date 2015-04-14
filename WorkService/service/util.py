def getSplitChars(str):
    chars=[]
    for i in str:
        if not (i>='a'and i<='z' or i>='0' and i<='9' or i=='_' or i>='A' and i<='Z'):
            chars.append(i)
    return set(chars)

def my_split(str): 
    splitchars=getSplitChars(str)
#    print splitchars
    for i in splitchars:
        str = str.replace(i,' ')
    list1 = str.split()
    return list1
