def pertenceFibonacci(num):
    # Função para verificar se um número é quadrado perfeito
    def verificaQuadradoPerfeito(x):
        s = int(x**0.5)
        return s*s == x

    # Um número pertence à sequência de Fibonacci se e somente se
    # um dos dois valores abaixo for um quadrado perfeito
    if verificaQuadradoPerfeito(5*num*num + 4) or verificaQuadradoPerfeito(5*num*num - 4):
        return True
    else:
        return False

# Entrada do número
num = int(input("Informe um número: "))

# Calcula a sequência e verifica se o número pertence
if pertenceFibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
