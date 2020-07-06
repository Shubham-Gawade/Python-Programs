starter = ['Paneer tikka' , 'Manchurian' , 'SpringRoll']
starterprice = [299,250,275]
maincourse = ['Paneer Lababdar','Lasuni Palak','Veg Biryani']
maincourseprice = [350,300,450]
dessert = ['Litchi Phirni','Shahi Tukda','Mango Rasmalai']
dessertprice = [200,250,230]
menu=[1,2,3,0]
menuchoice=['Starter','Main Course','Dessert','Exit']
order=[]
orderprice=[]
total=0
#finalmenu=[menu,menuchoice]
while True:
    for i in range(4):
            print(menu[i],"\t",menuchoice[i])
    ch=int(input('Enter Choice'))
    if(ch==1):
        for i in range(3):
            print(menu[i],"\t ",starter[i], "\t", starterprice[i])
        ch1=int(input('enter starter choice'))
        if(ch1==1):
            total=total+starterprice[ch1-1]
            order.append(starter[ch1-1])
            orderprice.append(starterprice[ch1 - 1])
        elif(ch1==2):
            total=total+starterprice[ch1-1]
            order.append(starter[ch1-1])
            orderprice.append(starterprice[ch1 - 1])
        elif (ch1 == 3):
            total = total + starterprice[ch1 - 1]
            order.append(starter[ch1 - 1])
            orderprice.append(starterprice[ch1 - 1])
        else:
            print("Wrong Choice")
    elif(ch==2):
        for i in range(3):
            print(menu[i],"\t ",maincourse[i], "\t", maincourseprice[i])
        ch1=int(input('enter main course choice'))
        if(ch1==1):
            total=total+maincourseprice[ch1-1]
            order.append(maincourse[ch1-1])
            orderprice.append(maincourseprice[ch1 - 1])
        elif(ch1==2):
            total=total+maincourseprice[ch1-1]
            order.append(maincourse[ch1-1])
            orderprice.append(maincourseprice[ch1 - 1])
        elif (ch1 == 3):
            total = total + maincourseprice[ch1 - 1]
            order.append(maincourse[ch1 - 1])
            orderprice.append(maincourseprice[ch1 - 1])
        else:
            print("Wrong Choice")
    elif(ch==3):
        for i in range(3):
            print(menu[i],"\t ",dessert[i], "\t", dessertprice[i])
        ch1=int(input('enter dessert choice'))
        if(ch1==1):
            total=total+dessertprice[ch1-1]
            order.append(dessert[ch1-1])
            orderprice.append(dessertprice[ch1 - 1])
        elif(ch1==2):
            total=total+dessertprice[ch1-1]
            order.append(dessert[ch1-1])
            orderprice.append(dessertprice[ch1 - 1])
        elif (ch1 == 3):
            total = total + dessertprice[ch1 - 1]
            order.append(dessert[ch1 - 1])
            orderprice.append(dessertprice[ch1 - 1])
        else:
            print("Wrong Choice")
    else:
        break
print("--------------BILL----------------")
print("-------------YOUR--ORDER-----------")
for i in range(len(order)):
    print(i+1 , "\t ", order[i],"\t",orderprice[i])
gst=total*0.18
finaltotal=gst+total
print("-----------------------------------")
print('Total is : ',total)
print('Gst is (18%): ',gst)
print('Final Total is : ',finaltotal)
print("-----------------------------------")


