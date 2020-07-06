def factor(n):
    print("Factors are : ")
    for i in range(2,n):
        if n%i == 0:
            print(i)

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

def prime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("Number is prime")
    else:
        print("Number is not prime")

def armstrong(n):
    rev = 0
    temp1 = n
    temp = n
    count = 0
    while temp1 > 0:
        rev = int(temp1 % 10)
        count +=1
        temp1 = int(temp1 / 10)

    sum = 0
    while n > 0:
        rev = int(n % 10)
        sum = int(sum + pow(rev,count))
        n = int(n/10)

    if sum == temp:
        print("Number is armstrong")
    else:
        print("Number is not armstrong")

def reverse(n):
    rev1 = 0
    while n > 0:
        d = int(n % 10)
        rev1 = int((rev1 * 10)+d)
        n = int(n / 10)
    print("Reverse no : ",rev1)