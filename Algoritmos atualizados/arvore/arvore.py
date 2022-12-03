import random
 
 
def gerarNumeros():
    numeros = [random.randrange(20, 100) for i in range(100)]
    print ("Random number list is : " +  str(numeros))
    
    
def numeros():
    numeros = [random.randrange(20, 100)]
    for i in range(100):
        nume = str(numeros)
    return nume


if __name__ == "__main__":
    number = numeros()
    aula = gerarNumeros()
    print(number)