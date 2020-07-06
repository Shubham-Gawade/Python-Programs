dictionary={
    "brand":"Ford",
    "model":"Mustang",
    "year":1965,
    "colour":"Red"
}

print(dictionary)

x=dictionary.get("brand")
print(x)

x=dictionary["model"]
print(x)

dictionary["year"]=1968
print(dictionary)

for i in dictionary:
    print(i)

for i in dictionary:
    print(dictionary[i])

print("--------------------------------------------")

for i in dictionary:
    print(i,"\t",dictionary[i])

print("--------------------------------------------")

for i in dictionary.values():
    print(i)

print("--------------------------------------------")

print(dictionary.items())

for x,y in dictionary.items():
    print(x,"\t",y)

print("---------------------------------------------")

if "model" in dictionary:
    print("yes")

print("--------------------------------------------")

print('pop',dictionary.pop("model"))
print('now',dictionary)

print("--------------------------------------------")

print('popitem',dictionary.popitem())
print('now',dictionary)

print("--------------------------------------------")

del dictionary["brand"]  #delete brand from dictionary
print(dictionary)

print("--------------------------------------------")

dictionary.clear()   #delete only data from dictionary
print(dictionary)

print("--------------------------------------------")

del dictionary   #delete complete dictiory
print(dictionary)

print("---------------------------------------------")