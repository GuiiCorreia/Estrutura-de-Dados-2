def is_operand(c):
    """
    Retorna True se o caractere c fornecido for um operando,
     por exemplo. é um número
    """
    return c.isdigit()
 
 
def evaluate(expression):
    """
    Avalie uma determinada expressão em notação de prefixo.
    Afirma que a expressão fornecida é válida.
    """
    stack = []
 
    # iterar sobre a string na ordem inversa
    for c in expression[::-1]:
 
        # push operando para empilhar
        if is_operand(c):
            stack.append(int(c))
 
        else:
            # valores pop da pilha podem calcular o resultado
            # coloca o resultado na pilha novamente
            o1 = stack.pop()
            o2 = stack.pop()
 
            if c == '+':
                stack.append(o1 + o2)
 
            elif c == '-':
                stack.append(o1 - o2)
 
            elif c == '*':
                stack.append(o1 * o2)
 
            elif c == '/':
                stack.append(o1 / o2)
 
    return stack.pop()
 
 
# main
if __name__ == "__main__":
    test_expression = "+9*26"
    print(evaluate(test_expression))
 