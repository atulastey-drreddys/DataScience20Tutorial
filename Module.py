def Counter(n):
    if n <= 1:
        return 1
    else:
        return n + Counter(n-1)
Counter(5)

def Fact(n):
    if n <= 1:
        return 1
    else:
        return n * Fact(n-1)
Fact(5)

def Fabonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        a,b = b, a + b
Fabonacci(10)

def PrimeNumber(n):
    if n <= 1:
        return 1
    else:
        for i in range(2,n):
            if n % i == 0:
                print('Not prime number')
                break
        else:
            print("Prime Number")
PrimeNumber(9)

def Addition(a,b,c):
    Add = a + b + c
    return Add
Addition()

def Multiplication(a,b,c):
    Multi = a + b + c
    return Multi
Multiplication()