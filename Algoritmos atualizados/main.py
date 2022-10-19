from algoritmosOrdenacao import *
import time

inicio = time.time()


def dados():
    arquivo = "dados5.txt"
    with open(arquivo, "r") as arquivos:
        organizar = arquivos.read().replace(" ", "").replace("[", "").replace("]", "").split(",")
        dados = list(map(int, organizar))
    return dados 

def salvarArquivo():
    nome = "Guilherme Correia"
    nomeAlgoritmo = "Insertion Sort"
    final = time.time()
    tempo = ("\nTempo total: "+ time.strftime("%H : %M : %S", time.gmtime(final-inicio))+":{0:.0f}\n".format((final-inicio)*1000))
    local = "ordenado.txt"
    comp = (f"\nComparacoes: {algoritmo.comparacoes}")
    troc = (f"\nTrocas: {algoritmo.trocas}")
    with open (local, "w") as arquivo:
        arquivo.write("{}\n{}\n{}\n{}\n{}\n{}".format(nome, nomeAlgoritmo, tempo, numeros, comp, troc))


if __name__ == "__main__":
    numeros = dados()
    algoritmo = InsertionSort()
    algoritmo.sort(numeros)
    salvar = salvarArquivo()

