print(2**80)

print(5/2)

print(divmod(10,3))

print(abs(-5.9))

print(divmod(3,10))

print(True+True-False+True-True)

print(False==0)

print(complex(3,1)*3)

print(complex(3,1)*complex(3,2))

#integer character complex boolean float function modules everything is an object

x=complex(3,1)
print(x.real)
print(x.imag)
print(x.conjugate())

y=1
if y==0:
    fraction=1
    print(fraction)
else:
    fraction=None
    print(fraction)

str1="abc"
str2=str1+"def"
print(str2)

for i in str1:   #iterative
    print(i)

if "a" in str1:   #searching
    print("Found")

str3="hello there"
print(str3.replace("h","j"))
print(str3.capitalize())
print(str3.title())
print(str3.upper())
print(str3.count("e"))
print(str3.index("l"))
print(str3.startswith("hel"))
print(str3.endswith("er"))

joiner="and"
names=["abc "," xyz"]
joined=joiner.join(names)
print(joined)
print(joined.split("and"))

x="a"
print(ord(x))
print(chr(97))

word='Help'+'A'  #sub scripting
print(word)
print('<'+word*5+'>')
print(word[4])
print(word[0:2])
print(word[2:4])
print(word[0:-1])
print(word[-1])