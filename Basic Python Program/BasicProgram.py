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

def reverse(n):
    rev1 = 0
    while n > 0:
        d = int(n % 10)
        rev1 = int((rev1 * 10)+d)
        n = int(n / 10)
    print("Reverse no : ",rev1)

def sumofdigit(n):
    rev = 0
    sum = 0
    while n > 0:
        rev = n % 10
        sum = int(sum + rev)
        n = n /10
    print("Sum of Digit is : ",sum)

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

print("1)Factors of number")
print("2)Factorial of number")
print("3)Prime of number")
print("4)Reverse of number")
print("5)Sum of digit")
print("6)Armstrong number")
print("7)Perfect number")
print("8)Neon number")
print("9)Palindrome number")
print("10)Fibonnaci series")
print("Enter your choice : ")
ch=int(input())
if ch == 1:
    factor(int(input("Enter number : ")))
elif ch == 2:
    print("Factorial is : ",factorial(int(input("Enter number : "))))
elif ch == 3:
    prime(int(input("Enter number : ")))
elif ch == 4:
    reverse(int(input("Enter number : ")))
elif ch == 5:
    sumofdigit(int(input("Enter number : ")))
elif ch == 6:
    armstrong(int(input("Enter number : ")))
elif ch == 7:
    perfect(int(input("Enter number : ")))
elif ch == 8:
    neon(int(input("Enter number : ")))
elif ch == 9:
    palindrome(int(input("Enter number : ")))
elif ch == 10:
    fibonacci(int(input("Enter number : ")))
else:
    print("invalid...")