print('1.Area of Circle')
print('2.Area of Triangle')
print('3.Area of Rectangle')

choice=int(input('Enter your choice : '))
if choice==1:
    radius=int(input('Enter radius of circle :'))
    area=3.14*radius*radius
    print('Area of circle is : '+str(area))
elif choice==2:
    height = int(input('Enter Height of Triangle :'))
    base = int(input('Enter base of Triangle :'))
    area=0.5*height*base
    print('Area of circle is : ' + str(area))
else:

    length = int(input('Enter length of Rectangle :'))
    width=int(input('Enter width of Rectangle : '))
    area=length*width
    print('Area of Rectangle is : ' + str(area))

