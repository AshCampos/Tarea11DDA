#Programa que hace la serie de fibonacci teniendo como entrada n la posición de la serie y de salida el enesimo número de la serie, usando diccionarios

def fibonacciConDic(n, fib_dict={1: 1, 2: 1}):
    if n in fib_dict:  
        return fib_dict[n]  
    else:
        fib_dict[n] = fibonacciConDic(n - 1, fib_dict) + fibonacciConDic(n - 2, fib_dict)
        return fib_dict[n]
print(fibonacciConDic(7))
