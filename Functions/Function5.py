#Functions are objects in python
#We can pass function to another funtion

def square(a):
    return a*a

result=square(5)
print(result)

print("-------------------------------")
#Anonymus function
#If you want to use function only once and we dont want to declare it

f = lambda a,b: a+b #Lamda expression
#you can pass any number of variable but must return one expression

result=f(5,6)
print(result)

