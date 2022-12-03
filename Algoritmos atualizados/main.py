from algoritmosOrdenacao import *
import time

inicio = time.time()

def dados():
    arquivo = "dados10_mil.txt"
    with open(arquivo, "r") as arquivos:
        organizar = arquivos.read().replace(" ", "").replace("[", "").replace("]", "").split(",")
        dados = list(map(int, organizar))
    return dados 

def salvarArquivo():
    nome = "Guilherme Correia"
    nomeAlgoritmo = "Algoritmo Cocktail"
    final = time.time()
    tempo = ("\nTempo total: "+ time.strftime("%H : %M : %S", time.gmtime(final-inicio))+":{0:.0f}\n".format((final-inicio)*1000))
    local = "ordenado.txt"
    movi = (f"\nMovimentos: {algoritmo.movimentos}")
    comp = (f"\nComparações: {algoritmo.comparacoes}")
    with open (local, "w") as arquivo:
        arquivo.write("{}\n{}\n{}\n{}\n{}\n{}".format(nome, nomeAlgoritmo, tempo, numeros, movi, comp))

def get_decreasing_numbers_list(size):
    numbers = list()
    for i in range(size, 0, -1):
        numbers.append(i)
    return numbers

if __name__ == "__main__":
    numeros = dados()
    #numeros = get_decreasing_numbers_list(200)
    algoritmo = CocktailSort()
    algoritmo.sort(numeros)
    #print(numeros)
    salvar = salvarArquivo()