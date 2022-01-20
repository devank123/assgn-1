
# ASSIGNMENT-1



#Answer-1

print('Answer-1')
a=int(input('enter first number: '))
b=int(input('enter second number: '))
c=int(input('enter third number: '))
average=(a+b+c)/3
print('the average of the numbers is: ',average)
#Question-1 finished
print()

#**************************************************************************************************

#Answer-2

print('Answer-2')
income=int(input('enter gross income: '))
dependent=int(input('enter number of dependent: '))
ti=income-1000-(dependent*3000)  # ti is taxable income 
tr=0.2  #tr is tax rate 
print('annual tax is: ',ti*tr)
#Question-2 finished
print()

 #**************************************************************************************************

#Answer-3

print('Answer-3')
name=input('Enter name: ')
sid=int(input('enter sid: '))   #sid is student id
gender=input('enter gender: ')   #M(male),F(female),U(unknown)
course=input('enter course: ')
CGPA=float(input('enter CGPA: '))
student=[sid,name,gender,course,CGPA]
print(student)   
#Question-3 finished
print()

#****************************************************************************************************

#Answer-4

print('Answer-4')
S1=int(input('enter marks of student 1: '))
S2=int(input('enter marks of student 2: '))     
S3=int(input('enter marks of student 3: '))
S4=int(input('enter marks of student 4: '))         
S5=int(input('enter marks of student 5: '))
Marks=[S1,S2,S3,S4,S5]
Marks.sort()              #markes are sorted in ascending order
print(Marks)
#Question-4 finished
print()

#*****************************************************************************************************

#Answer-5

#Part-a
colour=['red', 'green', 'whilte', 'black','pink', 'yellow']
print('Answer 5-a')
print('list is:',colour)
del colour[3]
print('new list:',colour)   #answer of 5-a

#Part-b
print('Answer 5-b')
colour=['red', 'green', 'whilte', 'black','pink', 'yellow']
del colour[3:5]         
colour.insert(3,'purple')         #removing black and pink and replacing them with purple
print('new list:',colour)   #answer of 5-b
#question-5 finished
print()

#****************************************************************************************************

#name-devank garg
#SID-21104098
#branch-EE






