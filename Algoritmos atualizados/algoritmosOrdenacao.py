import abc
from main import inicio
import random


class SortingAlgorithm(abc.ABC):
    def __init__(self):
        self.movimentos = 0
        self.comparacoes = 0

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
                self.comparacoes += 2
                dados[j], dados[j - 1] = dados[j - 1], dados[j]
                j -= 1
            self.movimentos += 1
    
class SelectionSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()

    def sort(self, dados: list):
        for i in range(len(dados)):
            j = i
            aux = i
            while aux + 1 < len(dados):
                self.comparacoes += 1
                aux += 1
                x = aux
                if dados[j] > dados[x]:
                    self.comparacoes += 1
                    j = x
            if j != i:
                dados[j], dados[i] = dados[i], dados[j]
                self.movimentos += 1

class BubbleSort(SortingAlgorithm):   
    def __init__(self):
        super().__init__()

    def sort(self, dados: list):
        i = 0
        while i<len(dados):
            j = 0
            while j<len(dados)-1:
                self.comparacoes += 1
                if dados[j+1] < dados[j]:
                    dados[j], dados[j+1] = dados[j+1], dados[j]
                    self.movimentos += 1
                j += 1
            i += 1

class ComboSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()

    def sort(self, dados: list):

        gap=len(dados)
        swapped = True
        temp=0
        i = j = 0
        while gap!=1 or swapped == True:
            swapped=False
            gap = int(gap/1.3)
            if gap < 1:
                self.comparacoes += 1
                gap=1
            j += 1
            for i in range(0, len(dados)-gap): 
                if dados[i] > dados[i + gap]:
                    self.comparacoes += 1
                    temp=dados[i]
                    dados[i]=dados[i + gap]
                    self.movimentos += 1
                    dados[i + gap]=temp
                    swapped = True
                    j += 1
            
        i+=1

class ShellSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()

    def sort(self, dados: list):
        y = len(dados) // 2
        for i in range(y, len(dados)):
            self.comparacoes += 1
            d = dados[i]
            j = i
            while j >= y and dados[j - y] > d:
                self.comparacoes += 1
                self.movimentos += 1
                dados[j] = dados[j - y]
                j -= y

            dados[j] = d
        y = y // 2

class BogoSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()

    def sort(self, dados: list):
        i = j = 0
        random.shuffle(dados)
        while dados != sorted(dados):
            self.comparacoes += 1
            random.shuffle(dados)
            self.movimentos += 1
            i += 1
        j +=1
                
class QuickSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()
        
    def sort(self, dados: list):
        self._quick_sort(dados, 0, len(dados) - 1)
        
    @staticmethod    
    def _partition(dados, low, high):
        pivot = dados[high]
        i = low - 1
        for j in range(low, high):
            if dados[j] <= pivot:
                i = i + 1
                (dados[i], dados[j]) = (dados[j], dados[i])
        (dados[i + 1], dados[high]) = (dados[high], dados[i + 1])
        return i + 1
  
    def _quick_sort(self, dados, low, high):
        self.comparacoes += 1
        if low < high:
            pi = self._partition(dados, low, high)
            self._quick_sort(dados, low, pi - 1)
            self._quick_sort(dados, pi + 1, high)
            self.movimentos += 1

class MergeSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()
        
    def sort(self, dados: list):
        self._merge_sort(dados)
        
    def _merge_sort(self, dados):
        if len(dados) > 1:
            mid = len(dados) // 2
            left = dados[:mid]
            right = dados[mid:]
            self._merge_sort(left)
            self._merge_sort(right)
            i = 0
            j = 0
            k = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    dados[k] = left[i]
                    i += 1
                    self.comparacoes += 1
                else:
                    dados[k] = right[j]
                    j += 1
                    self.comparacoes += 1
                k += 1
            
            while i < len(left):
                dados[k] = left[i]
                self.movimentos += 1
                i += 1
                k += 1

            while j < len(right):
                self.movimentos += 1
                dados[k]=right[j]
                j += 1
                k += 1

class HeapSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()
        
    def sort(self, dados: list):
        self._heap_sort(dados)
    
    def _heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2
        self.comparacoes += 2
        if l < n and arr[i] < arr[l]:
            largest = l
        self.comparacoes += 2
        if r < n and arr[largest] < arr[r]:
            largest = r
        self.comparacoes += 1
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            self.movimentos += 1
            self._heapify(arr, n, largest)
    
    def _heap_sort(self, dados):
        for i in range(len(dados) // 2 - 1, -1, -1):
            self._heapify(dados, len(dados), i)
        for i in range(len(dados) - 1, 0, -1):
            dados[i], dados[0] = dados[0], dados[i]
            self._heapify(dados, i, 0)

class GnomeSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()
        
    def sort(self, dados: list):
        self._gnome_sort(self, dados)
        
    @staticmethod    
    def _gnome_sort(self, dados):
        index = 0
        while index < len(dados):
            if index == 0:
                index = index + 1
                self.comparacoes += 1
            if dados[index] >= dados[index - 1]:
                index = index + 1
                self.comparacoes += 1
            else:
                dados[index], dados[index-1] = dados[index-1], dados[index]
                self.movimentos += 1
                index = index - 1

class RadixSort(SortingAlgorithm):

    def __init__(self):
        super().__init__()
        
    def sort(self, dados: list):
        self._radix_sort(dados)
      
    def _counting_sort(self, dados, exp1):
        n = len(dados)
        output = [0] * (n)
        count = [0] * (10)
        for i in range(0, n):
            index = dados[i] // exp1
            count[index % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            index = dados[i] // exp1
            output[count[index % 10] - 1] = dados[i]
            self.movimentos += 1
            count[index % 10] -= 1
            i -= 1
        i = 0
        for i in range(0, len(dados)):
            dados[i] = output[i]

    
    def _radix_sort(self, dados):
        max1 = max(dados)
        exp = 1
        while max1 / exp >= 1:
            self._counting_sort(dados, exp)
            exp *= 10
        # Encontrar a posicao do primeiro numero negativo em dados.
        posicao_primeiro_negativo = 0
        for i in range(len(dados)):  # N
            if dados[i] < 0:
                posicao_primeiro_negativo = i
                break
        # Lista auxiliar.
        dados2 = list()
        # Copiar numeros negativos para dados2.
        for i in range(posicao_primeiro_negativo, len(dados)):  # N
            dados2.append(dados[i])
        # Copiar o restante dos numeros (os positivos) para dados2.
        for i in range(0, posicao_primeiro_negativo):  # N
            dados2.append(dados[i])
        # Dados recebe os numeros completamente ordenados.
        for i in range(0, len(dados)):  # N
            dados[i] = dados2[i]

class CountingSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()
        
    def sort(self, dados: list):
        self._counting_sort(dados)

    def _counting_sort(self, dados):
        counts = [0 for i in range(max(dados)+1)]
    
        # Finds the "counts" for each individual number
        for value in dados:
            counts[value] += 1  
    
        # Finds the cumulative sum counts
        for index in range(1, len(counts)):
            counts[index] = counts[index-1] + counts[index]
    
        # Sorting Phase
        dados = [0 for loop in range(len(dados))]
        for value in dados:
            index = counts[value] - 1
            dados[index] = value
            counts[value] -= 1
        return dados

class BucketSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()
        
    def sort(self, dados: list):
        self._bucket_sort(dados)

    def _bucket_sort(self, dados):
        for i in range(1, len(dados)):
            up = dados[i]
            j = i - 1
            while j >= 0 and dados[j] > up: 
                dados[j + 1] = dados[j]
                j -= 1
            dados[j + 1] = up         
                
    def bucketSort(self, x):
        arr = []
        slot_num = 10 # 10 means 10 slots, each
                    # slot's size is 0.1
        for i in range(slot_num):
            arr.append([])
            
        # Put dados elements in different buckets 
        for j in x:
            index_b = int(slot_num * j) 
            arr[index_b].append(j)
        
        # Sort individual buckets 
        for i in range(slot_num):
            arr[i] = self._bucket_sort(arr[i])
            
        # concatenate the result
        k = 0
        for i in range(slot_num):
            for j in range(len(arr[i])):
                x[k] = arr[i][j]
                k += 1

class CocktailSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()
        
    def sort(self, dados: list):
        self._cocktail_sort(dados)

    def _cocktail_sort(self, dados):
        n = len(dados)
        swapped = True
        start = 0
        end = n-1
        while (swapped==True):
            swapped = False

            for i in range (start, end):
                if (dados[i] > dados[i+1]) :
                    dados[i], dados[i+1]= dados[i+1], dados[i]
                    swapped=True
            if (swapped==False):
                break
            swapped = False
            end = end-1
            for i in range(end-1, start-1,-1):
                if (dados[i] > dados[i+1]):
                    dados[i], dados[i+1] = dados[i+1], dados[i]
                    swapped = True

            start = start+1

class TimSort(SortingAlgorithm):#
    def __init__(self):
        super().__init__()
        
    def sort(self, dados: list):
        self._tim_sort(dados)
        
    def _tim_sort(arr,start,end):    
        for i in range(start+1,end+1):
            elem = arr[i]
            j = i-1
            while j>=start and elem<arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = elem
        
        def merge(arr,start,mid,end):
            if mid==end:
                return arr
            first = arr[start:mid+1]
            last = arr[mid+1:end+1]
            len1 = mid-start+1
            len2 = end-mid
            ind1 = 0
            ind2 = 0
            ind  = start
            
            while ind1<len1 and ind2<len2:
                if first[ind1]<last[ind2]:
                    arr[ind] = first[ind1]
                    ind1 += 1
                else:
                    arr[ind] = last[ind2]
                    ind2 += 1
                ind += 1
            
            while ind1<len1:
                arr[ind] = first[ind1]
                ind1 += 1
                ind += 1
                    
            while ind2<len2:
                arr[ind] = last[ind2]
                ind2 += 1
                ind += 1   
                    
            return arr
                    
        def TimSort(self, arr):
            n = len(arr)
            
            for start in range(0,n,self.minrun):
                end = min(start+self.minrun-1,n-1)
                arr = self.InsSort(arr,start,end)
                
            curr_size = self.minrun
            while curr_size<n:    
                for start in range(0,n,curr_size*2):
                    mid = min(n-1,start+curr_size-1)
                    end = min(n-1,mid+curr_size)
                    arr = merge(arr,start,mid,end)
                curr_size *= 2
            return arr