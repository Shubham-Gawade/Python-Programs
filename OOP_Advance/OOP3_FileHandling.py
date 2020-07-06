#File Handling

fhandle=open("MyData","r")

#print(fhandle)

#print(fhandle.read())    #Printing all data

#print(fhandle.readline())  #Printing single line

#print("-----------------------------------------------------------------------------------------------")

#fhandle1=open("MyFile","w")  #If file is not present then it will create a file for us

fhandle1=open("MyFile","a") # a-> append  it will not override the data
#fhandle1.write("Something")
#fhandle1.write("People")

fhandle1.write("Laptop")

#print("-----------------------------------------------------------------------------------------------")
#Copy data from one file to another

for data in fhandle:
     fhandle1.write(data)
