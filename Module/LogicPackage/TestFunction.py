from LogicPackage import BasicFunction
from LogicPackage.MainFunction import sumofdigit,perfect,neon,fibonacci,palindrome

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
    BasicFunction.factor(int(input("Enter number : ")))
elif ch == 2:
    print("Factorial is : ",BasicFunction.factorial(int(input("Enter number : "))))
elif ch == 3:
    BasicFunction.prime(int(input("Enter number : ")))
elif ch == 4:
    BasicFunction.reverse(int(input("Enter number : ")))
elif ch == 5:
    sumofdigit(int(input("Enter number : ")))
elif ch == 6:
    BasicFunction.armstrong(int(input("Enter number : ")))
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
