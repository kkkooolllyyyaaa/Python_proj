import re
s = open('D:\other\ITMO\Informatics\Labs\lab4\input21.txt', 'r', encoding = 'utf8')
text = s.read().split('\n')
pattern = r'[A-Z][^?!.\n;]*!'
patternzap = r'\,'
for i in range(len(text)):
    if(re.search(pattern,text[i])):
        dops=list()
        dops=re.findall(pattern,text[i])
        for j in range(len(dops)):
            if(re.search(patternzap,dops[j])):
                helper=re.search(pattern,dops[j])
                helper=helper.group()
                print(helper+' ', end='')
            if(j==(len(dops)-1)):
                print()
s.close()
