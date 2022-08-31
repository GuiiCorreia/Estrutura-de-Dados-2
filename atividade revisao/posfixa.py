from collections import deque
 
 
# Função para avaliar uma determinada expressão pós-fixada
def evalPostfix(exp):
 
    # caso base
    if not exp:
        exit(-1)
 
    # criar uma pilha vazia
    stack = deque()
 
    # percorra a expressão dada
    for ch in exp:
 
        # se a corrente for um operando, empurre-o para a pilha
        if ch.isdigit():
            stack.append(int(ch))
 
        # se a corrente é um operador
        else:
            # remova os dois primeiros elementos da pilha
            x = stack.pop()
            y = stack.pop()
 
            # avalia a expressão 'x op y' e empurra o

            # resultado de volta para a pilha
            if ch == '+':
                stack.append(y + x)
            elif ch == '-':
                stack.append(y - x)
            elif ch == '*':
                stack.append(y * x)
            elif ch == '/':
                stack.append(y // x)
 
    # Neste ponto, a pilha fica com apenas um elemento, ou seja,
    # resultado da expressão
    return stack.pop()
 
 
if __name__ == '__main__':
 
    exp = '138*+'
    print(evalPostfix(exp))