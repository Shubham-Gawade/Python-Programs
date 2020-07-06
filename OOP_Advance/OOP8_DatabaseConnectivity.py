import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="shubham")

mycursor=mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)

print("-----------------------------------")

mycursor.execute("select * from student")

result=mycursor.fetchall()

for i in result:
    print(i)

print("-----------------------------------")

mycursor.execute("insert into student values('sanket','mescoe')")

mycursor.execute("select * from student")

result=mycursor.fetchall()

for i in result:
    print(i)

print("-----------------------------------")