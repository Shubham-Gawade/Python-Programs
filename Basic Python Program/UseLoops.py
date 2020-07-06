i=1
while(i<=5):
    j=1
    while(j<=i):
        print("*",end='')
        j=j+1
    print()
    i=i+1

i=1
while(i<=10):
    j=1
    while(j<=10):
        print(i*j,end=' ')
        j=j+1
    print()
    i=i+1

i = 1
while i <= 5:
    print("*"*i)
    i = i+1

i=1
while(i>=5):
    j=1
    while(j<=i):
        print("*",end='')
        j=j+1
    print()
    i=i+1

j = 10
for i in range(1,11):
    if(i%2!=0):
        print(" " * j," *"*i)
    j=j-1

i = 0
a = 65
while i < 5:
    j = 0
    #a = 65
    while j <= i:
        print(chr(a),end=" ")
        j+=1
        a+=1
    print()
    i+=1

j = 5
a = 65
for i in range(1,6):
    print(" " * j,chr(a)*i)
    a+=1
    j=j-1

i = 1
cnt =1
while i <= 5:
    j = 1
    while j <= i:
        print(cnt,end=" ")
        j+=1
        cnt+=1
    print()
    i+=1
i = 4
while i > 0:
    j = 1
    while j <= i:
        print(cnt,end=" ")
        j+=1
        cnt+=1
    print()
    i-=1