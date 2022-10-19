import random
import time


arquivo = "dados5.txt"
with open(arquivo, "r") as arquivos:
    organizar = arquivos.read().replace(" ", "")
y = organizar.replace("[", "").replace("]", "").split(",")

dados = list(map(int, y))
inicio = time.time()
#print(dados)
def bubbleSort(dados):
    i  = 0
    while i<len(dados):
        j = 0
        while j<len(dados)-1:
            if dados[j+1] < dados[j]:
                dados[j], dados[j+1] = dados[j+1], dados[j]
            j += 1
        i += 1
    return dados
    
z = bubbleSort(dados)
final = time.time()
tempo = ("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(final-inicio))+":{0:.0f}".format((final-inicio)*1000))
print(z, tempo)
    