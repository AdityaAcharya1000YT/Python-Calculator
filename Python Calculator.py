import random

x = int(input('First Number: '))
y = int(input('Second Number: '))

Addition = x+y
Subtraction = x-y
Multiplication = x*y
Division = x/y

z = input('Operation Type: ')

if (z=='Addition'):
    print('Output:',Addition)
elif (z=='Subtraction'):
    print('Output:',Subtraction)
elif (z=='Multiplication'):
    print('Output:',Multiplication)
elif (z=='Division'):
    print('Output:',Division)

eo = int(input('Enter the output to find out whether the number is even or odd: '))

if (eo%2==0):
    print(eo,'is even')
else:
    print(eo,'is odd')