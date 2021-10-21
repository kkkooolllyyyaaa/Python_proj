import re
s = open('D:\other\ITMO\Informatics\Labs\lab4\input11.txt', 'r', encoding = 'utf8')
text = s.read().split('\n')
pattern = r'([01]\d:([0-5]\d:?){1,2})|(2[0-3]:([0-5]\d:?){1,2})'
for i in range(len(text)):
    print(re.sub(pattern,r'(TBD)',text[i]))
s.close()
