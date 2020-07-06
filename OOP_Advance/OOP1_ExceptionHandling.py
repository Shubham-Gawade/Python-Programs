#Exception Handling

a=5
b=2

try:
    print("Resource open")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("Divide by zero not possible....",e)

except ValueError as e:
    print("Invalid input....",e)

except Exception as e:
    print("Something went wrong..")

finally:
    print("Resource close")

print("--------------------------------------------------")

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B,C,D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")