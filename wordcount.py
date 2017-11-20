#coding=utf-8
import re
import collections

'''''
从文件中读取内容，统计词频
'''
def count_word(path):
    result = {}
    stri = "我你他太她跟着那会让都吗得一刚这就地的了是和至下也们有从上和还在当来为要新123456789\
      与中对以一把不所其而到，。“”（）：、；《》"
    with open(path) as file_obj:
        all_the_text = file_obj.read()
        #正则表达式替换特殊字符
        for word in all_the_text.split():
            #print(word)
            if word not in stri and len(word)!=0:
                if word not in result:
                    result[word] = 0
                result[word] += 1
        return result
'''''
以词频倒序
'''
def sort_by_count(d):
    #字典排序
    d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))
    return d

if __name__ == '__main__':
    file_name = "data/zhwiki-20150301.txt"
    f=open("result/bigcount.csv","w")
    dword = count_word(file_name)
    print ("Count Finished!")
    dword = sort_by_count(dword)
    print ("Sort Finished!")
    f.writelines("Word"",Freq\n")
    for key,value in dword.items():
        try:
            outkey = key.decode('utf-8','ignore').encode('gbk')
            f.write(outkey + ",%d\n" % value)
        except:
            pass
    f.close()
    #慧慧最可爱了
