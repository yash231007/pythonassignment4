print('QUESTION-1')

marks = float(input("Enter marks: "))
grade = None
if marks < 25:
    grade = 'F'
elif marks >= 25 and marks < 45:
    grade = 'E'
elif marks >= 45 and marks < 50:
    grade = 'D'
elif marks >= 50 and marks < 60:
    grade = 'C'
elif marks >= 60 and marks < 80:
    grade = 'B'
else:
    grade = 'A'
print('Grade is :', grade)

print('------------------------------------------------------------------------------------------------------------------------------------')
print('QUESTION-2')

year=int(input('Enter year : '))
if year%400==0:
    print(True)
elif year%4==0 and year%100!=0:
    print(True)
else:
    print(False)

print('------------------------------------------------------------------------------------------------------------------------------------')
print('QUESTION-3')

import random

for i in range(10):
    num1=random.randrange(1,11)
    num2=random.randrange(1,11)
    print(str(num1)+' x '+str(num2))
    ans=int(input("Enter your answer : "))
    if ans==num1*num2:
        print('Right!')
    else:
        print('Wrong. The answer is',str(num1*num2)+'.')

print('------------------------------------------------------------------------------------------------------------------------------------')
print('QUESTION-4')

for n_candy in range(1, 200):
    if n_candy % 5 == 2 and n_candy % 6 == 3 and n_candy % 7 == 2:
        print('Number of candies in bowl :', n_candy)
