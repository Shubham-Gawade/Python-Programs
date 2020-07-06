#Pass list to function

def count(lst):
    p=0
    n=0
    for i in lst:
        if int(i)%2==0:
            p+=1
        else:
            n+=1
    return p,n

lst=["1","2","3","4","5","6","7"]
even,odd=count(lst)

print("Even: {} and Odd: {}".format(even,odd))