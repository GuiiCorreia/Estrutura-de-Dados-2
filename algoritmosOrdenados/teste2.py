import random
import time


arquivo = "dados10_mil.txt"
with open(arquivo, "r") as arquivos:
    organizar = arquivos.read().replace(" ", "")
y = organizar.replace("[", "").replace("]", "").split(",")

dados = list(map(int, y))
inicio = time.time()
#print(dados)
def insertionSort(dados):
    for i in range(1, len(dados)):
        j = i
        while j > 0 and dados[j] < dados[j - 1]:
            dados[j], dados[j - 1] = dados[j - 1], dados[j]
            j -= 1
    return dados
    
z = insertionSort(dados)
final = time.time()
tempo = ("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(final-inicio))+":{0:.0f}".format((final-inicio)*1000))
print(z, tempo)
    