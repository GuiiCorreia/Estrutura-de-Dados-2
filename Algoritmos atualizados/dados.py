#from algoritmosOrdenacao import insertionSort
#from videotest import movimentos, trocas
import random
import time

arquivo = "dados5.txt"
with open(arquivo, "r") as arquivos:
    organizar = arquivos.read().replace(" ", "")
y = organizar.replace("[", "").replace("]", "").split(",")

dados = list(map(int, y))
#inicio = time.time()
#print(dados)
troca = 0
movi = 0
def insertionSort(dados):
    for i in range(1, len(dados)):
        j = i
        while j > 0 and dados[j] < dados[j - 1]:
            dados[j], dados[j - 1] = dados[j - 1], dados[j]
            j -= 1
            troca += 1
    movi += 1
    return dados, troca, movi

z = insertionSort(dados)
print(z)
    



"""if __name__ == "__main__":
    lista = dados
    print(lista)
    insertionSort(lista)
    print("\nOrdenado: ")"""