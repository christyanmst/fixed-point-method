import math

def f(x):
    return pow(x,2) - math.exp(x)

def g(x):
    return -math.sqrt(math.exp(x))

def fixedPoint():
    x0 = float(input("Digite a aproximação inicial x0: "))
    quantidadeIteracoes = int(input("Digite a quantidade de iterações: "))
    iteracao = 0
    x1 = 0
    while iteracao <= quantidadeIteracoes:
        x1 = g(x0)
        x0 = x1
        iteracao += 1
    print("A raiz encontrada foi x = ", x1)
    print("f(x) = ", f(x1))
    print("g(x) = ",x1)

fixedPoint()
