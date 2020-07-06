import math

print("1)Factorial of number")
print("2)Round off function")
print("3)Square root function")
print("4)Power function")
print("5)Factors of a number")
print("Enter your choice : ")
ch=int(input())
if ch == 1:
    print(math.factorial(int(input("Enter a number : "))));
if ch == 2:
    print(round(float(input("Enter a number : "))));
if ch == 3:
    print(math.sqrt(float(input("Enter a number : "))));
if ch == 4:
    print(math.pow(float(input("Enter 1st number : ")),float(input("Enter 2st number : "))));
if ch == 5:
    print()
else:
    print("invalid...")
