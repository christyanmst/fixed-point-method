from numpy import *

print("Método do Ponto Fixo")
a = float(input("Informe o primeiro intervalo:\n"))
b = float(input("Informe o segundo intervalo:\n"))
e=float(input("Entre com o numero real e:\n"))
y1 = input("Informe a função f(x):\n")
y2 = input("Informe a função g(x):\n")
funcao = str(y1).replace("**", "^").replace("*","")

def f(x):
    y = eval(y1)
    return y 
def g(x):
    z = eval(y2)
    return z 

def fixedPointIteration():
    if( b>a):
        x0=(a+b)/2
        i=1
        while True:
            x1=g(x0)
            print('Iteração-%d, x= %0.6f e f(x) = %0.6f' % (i, x1, f(x1)))
            
            if abs(f(x1)) < e or abs(abs(x1)-abs(x0)) <e:
                print("\nFunção : %s , Número de iterações = %d, x = %0.6f e f(x) = %0.6f" % (funcao, i, x1, f(x1)))
                break   
            i+=1
            x0=x1
fixedPointIteration()