import time
start_time = time.clock()
inputf = open('Вторник.yml', 'r', encoding = "utf-8")
outputf = open('Вторник.json','a', encoding = "utf-8")
newline = inputf.readline()
data = list()
dopstring = list()
linecnt = 0
while newline:
    data.append(newline)
    linecnt +=1
    newline = inputf.readline()
inputf.close()
start_k = len(data[0]) - len(data[0].lstrip())
outputf.write("{\n")
gap=0
count=0
for i in range(0, linecnt-1):
    if(i!=(linecnt-1)):
        dopstring = data[i].lstrip().split(':', maxsplit = 1)
        outputf.write((gap)*"    "+'    "' + dopstring[0].lstrip() + '":')
        if len(dopstring[1][:-1])!=0 :
            count+=1
            if(count==7) :
                outputf.write(dopstring[1][:-1].lstrip()+"\n")
                count=0
            else :
                outputf.write(dopstring[1][:-1].lstrip()+','+"\n")
        else : outputf.write(dopstring[1][:-1].lstrip()+"\n")
    end_k = len(data[i+1]) - len(data[i+1].lstrip())
    if end_k < start_k:
        outputf.write((gap-1)*"    "+"    },"'\n')
        gap=gap-1
    if end_k > start_k:
        outputf.write('\n')
        outputf.write((gap)*"    "+"    {"'\n')
        gap=gap+1
    start_k = end_k
dopstring = data[linecnt-1].lstrip().split(':', maxsplit = 1)
outputf.write("                "+'"'+dopstring[0].lstrip() + '":'+dopstring[1][:-1].lstrip()+'"'+"\n")
for i in range(0,gap+1):
    outputf.write((+gap-i)*"    "+'}'+'\n')
outputf.close()
print(time.clock()-start_time)
