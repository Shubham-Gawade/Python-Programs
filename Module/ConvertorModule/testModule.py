from ConvertorModule import moduleConvertor
from ConvertorModule.moduleConvertor import lbs_to_kg

#now we can directly use function in our program without module name

while True:
    print("1)Convert kg to lbs")
    print("2)Convert lbs to kg")
    print("3)Exit")
    ch = int(input("Enter your choice : "))
    if ch==1:
        print(moduleConvertor.kg_to_lbs(int(input("Enter weight in kg : "))))
    elif ch==2:
        print(lbs_to_kg(int(input("Enter weight in lbs : "))))

    else:
        break