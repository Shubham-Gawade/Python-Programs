string = "Hello friends , I am shubham"
print(string[0])  #first character
print(string[-1])  #last character
print(string[-2])   #second last character
print(string[0:3])  #start from index till 2
print(string[0:])   #python returns all value
print(string[1:])   #python returns all value except 1
print(string[:5])   #python has default index
print(string[:])
print(len(string))
print(string.upper())
print(string.lower())
print(string.find('l'))
print(string.find('am'))
string1 = string[:]
print(string1)
print(string1.replace('shubham','shubham gawade'))
print('gawade' in string)
print('shubham' in string1)
print(string[1:-1])