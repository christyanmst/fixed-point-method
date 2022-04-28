from numpy import*
import math

print("Método do Ponto Fixo!")
a   = float(input("Informe o primeiro intervalo:\n"))
b   = float(input("Informe o segundo intervalo:\n"))
err = float(input("Informe o valor do erro em decimal:\n"))
y1  = input("Informe a função f(x):\n")
y2  = input("Informe a função g(x):\n")
funcao = str(y1).replace("**", "^").replace("*","")

def f(x):
    y = eval(y1)
    return y 
def g(x):
    z = eval(y2)
    return z 

X_m = (a+b)/2
k = 0

while abs(f(X_m))>err:
    k = k+1
    X_m = g(X_m)
print("\nA raiz para a função: ",funcao," é aprox. x=",X_m,'com',k,' iterações' )

# 1° exemplo 
# f(x)= x^2 -6x +3
# g(x) = raiz(6x -3)
# E=0.01
# [5,6]
# 6 iterações, raiz 5,4505

# 2º Exemplo 
# f(x)= x^3-9x+5 
# g(x)= (x^3+5)\9 
# [0,5 ; 1] 
# E=10^-2 
# 3 iterações, raiz 0,5772

# 3° Exemplo 
# f(x)=x^3+8x-7
# g(x)=(7-x^3)/8
# E=0,1 
# [0,1]
# 3 iterações, raiz 0,812

# 4º exemplo
# f(x) = x^2 - x -2
# g(x) = raix(2+x)
# E= 0,00001
# x0 = 2.5 ou [2,3]
# 9 iterações, raiz 2.0000

# 5º exemplo
# f(x) = x^3 + x^2 - 1
# g(x) = 1/raiz(1+x)
# E= 0,00001
# x0= 2 ou [0,2]
# 8 iterações, raiz 0,7548

