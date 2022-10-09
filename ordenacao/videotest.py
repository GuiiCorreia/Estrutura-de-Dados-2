from algoritmosOrdenacao import *
import time
inicio = time.time()
 #temp_inicial = time.time()

def dados():
    arquivo = "dados1000.txt"
    with open(arquivo, "r") as arquivos:
        organizar = arquivos.read().replace(" ", "")
        y = organizar.replace("[", "").replace("]", "").split(",")

        dados = list(map(int, y))
    return dados 

def salvarArquivo():
    nome = "Guilherme Correia"
    nomeAlgoritmo = "\nInsertion Sort"
    final = time.time()
    tempo = ("\nTempo total: "+ time.strftime("%H : %M : %S", time.gmtime(final-inicio))+":{0:.0f}\n".format((final-inicio)*1000))
    local = "ordenado.txt"
    with open (local, "w") as arquivo:
        arquivo.write("{}\n{}\n{}\n{}".format(nome, nomeAlgoritmo, tempo, algoritmo))


if __name__ == "__main__":
    numeros = dados()
    algoritmo = selectionSort(numeros)
    salvar = salvarArquivo()
    #final = time.time()
    #tempo = ("\nTempo total: "+ time.strftime("%H : %M : %S", time.gmtime(final-inicio))+":{0:.0f}".format((final-inicio)*1000))
    #print (tempo)
