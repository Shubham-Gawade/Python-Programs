#Binary search

#The value must be in sorted order

pos=-1

def search(list,n):

    l=0
    u=len(list)-1

    while l <= u:
        mid=(l+u)//2  #Integer division

        if(list[mid]==n):
            global pos
            pos=mid
            return True
        else:
            if list[mid] < n:
                l=mid
            else:
                u=mid

arr=[2,4,8,12,56,67]

n=int(input("Enter number to be searched : "))

if search(arr,n):
    print("Found at position ",pos+1)
else:
    print("Not Found")