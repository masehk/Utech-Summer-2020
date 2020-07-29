def Fib(n): 

    if n <= 0: 
        print("Run Again")
    elif n == 1: 
        return 1
    elif n == 2: 
        return 1
    else: 
        return Fib(n-1)+Fib(n-2)

def Fibo(n):
    Fibonacci = []
    if n <= 0:
        print('Wrong !')
    elif n == 1:
        return Fibonacci + [1]
    elif n == 2:
        return Fibo(1) + [1]
    else:
        Num = Fibo(n-1)[-1] + Fibo(n-1)[-2]
        return Fibo(n-1) + [Num]

n = int(input('For N th Fibo Please Enter n: '))  
print(Fib(n))

n = int(input('For Fibo till N th Please Enter n: '))  
print(Fibo(n))


