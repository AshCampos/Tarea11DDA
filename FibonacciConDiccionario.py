def fibonacciConDic(n, fib_dict={1: 1, 2: 1}):
    if n in fib_dict:  
        return fib_dict[n]  
    else:
        fib_dict[n] = fibonacciConDic(n - 1, fib_dict) + fibonacciConDic(n - 2, fib_dict)
        return fib_dict[n]
print(fibonacciConDic(7))
