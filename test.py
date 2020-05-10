import re

f = open("Dictionary.txt","r")
line = f.readline()               # 调用文件的 readline()方法 
a = []
while line:   
    if len(line)==5 and re.search('^[a-f]+$',line):     # 4位单词加上末尾的换行符共5位
        a.append(line)                    
    line = f.readline()   
   
f.close()
dic = open("Output.txt","w")
dic.writelines(a)
dic.close()