def Fib(n): 

    if n <= 0: 
        print("Run Again")
    elif n == 1: 
        return 1
    elif n == 2: 
        return 1
    else: 
        return Fib(n-1)+Fib(n-2) 

n = int(input('Please Enter n: '))  
print(Fib(n)) 

