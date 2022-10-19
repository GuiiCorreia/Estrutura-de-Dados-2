import abc
from main import inicio
#from main import *
import random


class SortingAlgorithm(abc.ABC):
    def __init__(self):
        self.comparacoes = 0
        self.trocas = 0

    @abc.abstractmethod
    def sort(self, dados: list):
        pass

class InsertionSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()

    def sort(self, dados: list):
        for i in range(1, len(dados)):
            j = i
            while j > 0 and dados[j] < dados[j - 1]:
                dados[j], dados[j - 1] = dados[j - 1], dados[j]
                j -= 1
                self.trocas += 1
        self.comparacoes += 1

class SelectionSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()

    def sort(self, dados: list):
        for i in range(len(dados)):
            j = i
            aux = i
            while aux + 1 < len(dados):
                aux += 1
                x = aux
                if dados[j] > dados[x]:
                    j = x
            if j != i:
                dados[j], dados[i] = dados[i], dados[j]
            self.trocas += 1
        self.comparacoes += 1

class BubbleSort(SortingAlgorithm):   
    def __init__(self):
        super().__init__()

    def sort(self, dados: list):
        i = 0
        while i<len(dados):
            j = 0
            while j<len(dados)-1:
                if dados[j+1] < dados[j]:
                    dados[j], dados[j+1] = dados[j+1], dados[j]
                j += 1
                self.trocas = j
            i += 1
            self.comparacoes = i
"""
def comboSort(dados):
    gap=len(dados)
    swapped = True
    temp=0
    i = j = 0
    while gap!=1 or swapped == True:
        swapped=False
        gap = int(gap/1.3)
        if gap < 1:
            gap=1
        j += 1
        for i in range(0, len(dados)-gap): 
            if dados[i] > dados[i + gap]:
                temp=dados[i]
                dados[i]=dados[i + gap]
                dados[i + gap]=temp
                swapped = True
                j += 1
        #i+=1
    i+=1
    ordenacoes = (f"Numero de Comparacoes: {j} e Numeros de Trocas: {i}")
    return dados, ordenacoes

def shellSort(dados):
    y = len(dados) // 2
    for i in range(y, len(dados)):
        d = dados[i]
        j = i
        while j >= y and dados[j - y] > d:
            dados[j] = dados[j - y]
            j -= y

        dados[j] = d
    y = y // 2
    ordenacoes = (f"Numero de Comparacoes: {j} e Numeros de Trocas: {i}")
    
    return dados, ordenacoes

def bogoSort(dados):
    i = j = 0
    random.shuffle(dados)
    while dados != sorted(dados):
        random.shuffle(dados)
        i += 1
    j +=1
    ordenacoes = (f"Numero de Comparacoes: {j} e Numeros de Trocas: {i}")
    return dados,ordenacoes

def quickSort(dados):
    menor = []
    igual = []
    maior = []

    if len(dados) > 1:
        pivo = dados[0]
        for j in dados:
            if j < pivo:
                menor.append(j)
            elif j == pivo:
                igual.append(j)
            elif j > pivo:
                maior.append(j)
        return quickSort(menor)+igual+quickSort(maior)
    else:  
        return dados

def mergeSort(dados):
    if len(dados)>1:
        meio = len(dados)//2
        esquerda = dados[:meio]
        direita = dados[meio:]

        mergeSort(esquerda)
        mergeSort(direita)
        i=j=k=0       
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                dados[k]=esquerda[i]
                i=i+1
            else:
                dados[k]=direita[j]
                j=j+1
            k=k+1

        while i < len(esquerda):
            dados[k]=esquerda[i]
            i=i+1
            k=k+1

        while j < len(direita):
            dados[k]=direita[j]
            j=j+1
            k=k+1
    return dados

def heapSort(dados):                                 
    def montar(dados):                                       
        inicio = (len(dados) - 2) / 2                          
        inicio -= 1                                        

    def filtros(dados, inicio, final):                         
        j = inicio                                      
        while j * 2 + 1 <= final:                        
            k = j * 2 + 1                          
            if k + 1 <= final and dados[k] < dados[k+1]:
                k += 1                                
            if k <= final and dados[j] < dados[k]:       
                dados[j], dados[k] = dados[k], dados[j]     
                j = k                              
            else:                                         
                return                                    

    montar(dados)                                            
    final = len(dados) - 1                                      
    while final > 0:                                        
        dados[final], dados[0] = dados[0], dados[final]                       
        filtros(dados, 0, final-1)                            
        final -= 1             
    return dados

def gnomeSort(dados):
    i = 0
    while i < len(dados):
        if i == 0 or dados[i-1] <= dados[i]:
            i += 1
        else:
            dados[i], dados[i-1] = dados[i-1], dados[i]
            i -= 1
    return dados

def radixSort(dados):
    base=10
    resultado = []
    inicio = 0
    while dados:
        bins = [[] for _ in range(base)]
        for x in dados:
            bins[x // base**inicio % base].append(x)
        dados = []
        for bin in bins:
            for x in bin:
                if x < base**(inicio+1):
                    resultado.append(x)
                else:
                    dados.append(x)
        inicio += 1
    return resultado

def countingSort(dados):
    elementos= max(dados)
    tamanho = elementos+1
    contador = [0] * tamanho

    for i in dados: 
        contador[i] += 1

    for i in range(1, tamanho):
        contador[i] += contador[i-1] 

    resultado = [0] * len(dados)
    i = len(dados) - 1
    
    while i >= 0:
        atual = dados[i]
        contador[atual] -= 1
        posicao = contador[atual]
        resultado[posicao] = atual
        i -= 1

    return resultado

def bucketSort(dados):
    maior = max(dados)
    tamanho= len(dados)
    calculo = maior/tamanho
 
    buckets = [[] for i in range(tamanho)]
    
    for i in range(tamanho):
        index = int(dados[i]/calculo)
        if index != tamanho:
            buckets[index].append(dados[i])
        else:
            buckets[tamanho - 1].append(dados[i])

    for i in range(len(dados)):
        buckets[i] = sorted(buckets[i])
 
    resultado = []
    for i in range(tamanho):
        resultado = resultado + buckets[i]
             
    return resultado

def cocktailSort(dados):
    n = len(dados)
    trocador = True
    comeco = 0
    final = n-1
    while (trocador==True):
        trocador = False
 
        for i in range (comeco, final):
            if (dados[i] > dados[i+1]) :
                dados[i], dados[i+1]= dados[i+1], dados[i]
                trocador=True
 
        if (trocador==False):
            break
 
        trocador = False
        final = final-1

        for i in range(final-1, comeco-1,-1):
            if (dados[i] > dados[i+1]):
                dados[i], dados[i+1] = dados[i+1], dados[i]
                trocador = True

        comeco = comeco+1
        return dados

"""