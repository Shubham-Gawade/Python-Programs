def sumofdigit(n):
    rev = 0
    sum = 0
    while n > 0:
        rev = n % 10
        sum = int(sum + rev)
        n = n /10
    print("Sum of Digit is : ",sum)

def perfect(n):
    temp = n
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
    if temp == sum:
        print("Its a perfect number")
    else:
        print("Its not a perfect number")


def perfect(n):
    temp = n
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
    if temp == sum:
        print("Its a perfect number")
    else:
        print("Its not a perfect number")

def neon(n):
    sqr = n * n
    temp = n
    sum = 0
    while sqr > 0:
        rev = sqr % 10
        sum = int(sum + rev)
        sqr = sqr /10

    if temp == sum:
        print("Its a neon number")
    else:
        print("Its not a neon number")

def palindrome(n):
    temp = n
    rev1 = 0
    while n > 0:
        d = int(n % 10)
        rev1 = int((rev1 * 10)+d)
        n = int(n / 10)
    if temp == rev1:
        print("Number is palindrome")
    else:
        print("Number is not palindrome")


def fibonacci(n):
    a = 0
    b = 1
    print(a,"\t")
    print(b,"\t")
    for i in range(1,n-1):
        c = a + b
        a = b
        b = c
        print(b,"\t")
