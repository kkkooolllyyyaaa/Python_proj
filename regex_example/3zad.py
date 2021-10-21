import re
s = open('D:\other\ITMO\Informatics\Labs\lab4\input31.txt', 'r', encoding = 'utf8')
text = s.read().split('\n')
group='P000'
pattern21=r'[А-Я][а-я]+\s[А-Я]\.[А-Я]\. '+group
pattern22=r'[А-Я]\.'
for i in range(len(text)):
    if(re.search(pattern21,text[i])):
        dops=list()
        dops=re.findall(pattern22,text[i])
        check=re.findall(pattern21,text[i])
        if(dops[0][0]==dops[1][0]==check[0][0]):
            continue
        else:
            print(text[i])
        
    else:
        print(text[i])
s.close()
