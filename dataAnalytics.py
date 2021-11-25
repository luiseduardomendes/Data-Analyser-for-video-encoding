#teste classes

class DataStruct:
    def __init__(self, percentageTime=0, cumulativeTime=0, selfTime=0, calls=0, selfSCall=0, totalSCall=0, name=0):
        self.percentageTime = percentageTime
        self.cumulativeTime = cumulativeTime
        self.selfTime = selfTime
        self.calls = calls
        self.selfSCall = selfSCall
        self.totalSCall = totalSCall
        self.name = name
dados = DataStruct()
listaDados = list()

dados.calls = 15
dados.cumulativeTime = 253.5
dados.percentageTime = 5.4
dados.selfSCall = 23.2
dados.totalSCall = 123.2
dados.name = "RealizaCadastro"


listaDados.append(dados)

dados.calls = 21
dados.cumulativeTime = 212.5
dados.percentageTime = 7.4
dados.selfSCall = 12.2
dados.totalSCall = 153.2
dados.name = "excluiCadastro"

listaDados.append(dados[:])

for i in listaDados:
    print(i.calls)
    print(i.cumulativeTime)
    print(i.percentageTime)
    print(i.selfSCall)
    print(i.totalSCall)
    print(i.name)