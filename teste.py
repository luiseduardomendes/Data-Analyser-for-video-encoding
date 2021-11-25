dataStruct1 = dict()
dataStruct1['percentageTime'] = 4325
dataStruct1['cumulativeTime'] = 2345
dataStruct1['selfTime'] = 234
dataStruct1['calls'] = 243
dataStruct1['selfSCall'] = 4357
dataStruct1['totalSCall'] = 432623
dataStruct1['name'] = "function"

print(dataStruct1[1])

listaDados = list()

listaDados.append(dataStruct1.copy())

dataStruct1['percentageTime'] = 4325.865
dataStruct1['cumulativeTime'] = 2345.547
dataStruct1['selfTime'] = 234.235
dataStruct1['calls'] = 243.324
dataStruct1['selfSCall'] = 4357.42
dataStruct1['totalSCall'] = 42135
dataStruct1['name'] = "function2"

listaDados.append(dataStruct1.copy())

print(listaDados)