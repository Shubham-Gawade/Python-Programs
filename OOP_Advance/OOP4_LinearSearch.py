# Linear Serach

pos=-1

def search(list,n):
    # i=0
    #
    # while i<len(list):
    #     if list[i]==n:
    #         global pos
    #         pos=i
    #         return True
    #     i+=1

    for i in range(len(list)):
        if list[i]==n:
            global pos
            pos=i
            return True
    return False

arr=[5,8,4,6,9,2]

n=int(input("Enter number to be searched : "))

if search(arr,n):
    print("Found at position ",pos+1)
else:
    print("Not Found")