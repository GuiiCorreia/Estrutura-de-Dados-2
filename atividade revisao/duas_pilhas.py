import math  
  
class twoStacks:
      
    def __init__(self, n):     # construtor
        self.size = n
        self.arr = [None] * n
        self.top1 = math.floor(n/2) + 1
        self.top2 = math.floor(n/2)
  
  
    # Método para enviar um elemento x para stack1
    def push1(self, x):
          
        # Existe pelo menos um espaço vazio para novo elemento
        if self.top1 > 0:
            self.top1 = self.top1 - 1 
            self.arr[self.top1] = x
        else:
            print("Stack Overflow by element : ", x)
  
  
   # Método para enviar um elemento x para stack2
    def push2(self, x):
  
        # Existe pelo menos um espaço vazio para novo elemento
        if self.top2 < self.size - 1: 
            self.top2 = self.top2 + 1
            self.arr[self.top2] = x
        else :
            print("Stack Overflow by element : ", x)
  
  
    # Método para remover um elemento da primeira pilha
    def pop1(self):
        if self.top1 <= self.size/2:
            x = self.arr[self.top1]
            self.top1 = self.top1 +1
            return x
        else:
            print("Stack Underflow ")
            exit(1)
  
  
    # Método para remover um elemento da segunda pilha
    def pop2(self):
        if self.top2 >= math.floor(self.size/2) + 1: 
            x = self.arr[self.top2]
            self.top2 = self.top2 - 1
            return x
        else:
            print("Stack Underflow ")
            exit(1)
  
  
# Programa de driver para testar a classe twoStacks
ts = twoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)
  
print("Estourado da pilha1 é : " + str(ts.pop1()))
ts.push2(40)
print("Estourado da pilha2 é : " + str(ts.pop2()))