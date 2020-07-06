rollno=input('Enter roll no of student : ')
name=input('Enter name of student : ')
sub1=int(input('Enter marks of subject 1 : '))
sub2=int(input('Enter marks of subject 2 : '))
sub3=int(input('Enter marks of subject 3 : '))
total=sub1+sub2+sub3
per=total/3

print('\tRoll no of student : '+rollno)
print('\tName of Student : '+name)
print('\tMarks of subject 1 : '+str(sub1))
print('\tMarks of subject 2 : '+str(sub2))
print('\tMarks of subject 3 : '+str(sub3))
print('\tTotal : '+str(total))
print('\tPercentage : '+str(per))

if per >= 60:
    print('Grade A')
elif per <= 59 and per >= 40:
    print('Grade B')
else:
    print('Fail')