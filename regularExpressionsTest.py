from os import name
import re
from matplotlib import pyplot as plt

data = open('akiyo.txt')
stringList = data.read()

pattern = re.compile(r'([\d]+\.[\d]+)[ ]+([\d]+\.[\d]+)[ ]+([\d]+\.[\d]+|[ ]+)[ ]+([\d]+|[ ]+)[ ]+([\d]+\.[\d]+|[ ]+)[ ]+([\d]+\.[\d]+|[ ]+)[ ]+(.+)')
check = pattern.findall(stringList)

namePatternFunction = re.compile(r'.+\(')

structBuffer = dict()
dataList = list()

for i in check:
    
    structBuffer['percentage time'] = i[0]
    structBuffer['cumulative time'] = i[1]
    structBuffer['self seconds'] = i[2]
    
    if i[3] != ' ':
        structBuffer['calls'] = int(i[3])
    else:
        structBuffer['calls'] = -1
    
    if i[4] != ' ':
        structBuffer['self ms/call'] = float(i[4])
    else:
        structBuffer['self ms/call'] = -1.00
    
    if i[5] != ' ':
        structBuffer['total ms/call'] = float(i[5])
    else:
        structBuffer['total ms/call'] = -1.00

    structBuffer['name'] = i[6]    

    dataList.append(structBuffer.copy())


for i in range(0,20):
    print(f"{dataList[i]['percentage time']:8}{dataList[i]['cumulative time']:8}{dataList[i]['self seconds']:8}{dataList[i]['calls']:12}{dataList[i]['self ms/call']:8}{dataList[i]['total ms/call']:8}\t{dataList[i]['name']}")

percentageTime = list()
nameFunctions = list()

for i in range(0,20):
	percentageTime.append(dataList[i]['percentage time'][:])
	nameFunctions.append(namePatternFunction.findall(dataList[i]['name'])[0][:])

percentageTime.reverse()
nameFunctions.reverse()

	
plt.style.use('ggplot')
plt.title('Functions')
plt.xlabel('Percentage time')

plt.tight_layout()

plt.barh(nameFunctions, percentageTime)

plt.show()

