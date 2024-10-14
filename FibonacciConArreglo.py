#Programa que hace la serie de Fibonacci teniendo como entrada la posición n de la serie
# y como salida el enesimo numero de la serie, usando arreglos

def fibonacciConArreglo(n, fib_arreglo = None):
    if fib_arreglo is None:
        fib_arreglo = [0, 1, 1]  

    if n < len(fib_arreglo):  
        return fib_arreglo[n]
    else:
        fib_arreglo.append(fibonacciConArreglo(n - 1, fib_arreglo) + fibonacciConArreglo(n - 2, fib_arreglo))
        return fib_arreglo[n]
print(fibonacciConArreglo(15))

