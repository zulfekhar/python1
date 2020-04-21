import math

# Square Root

print ("math.sqrt(4) : ", math.sqrt(4))





# Calculator
def addition(a,b):
    print(a+b)


def substraction(a,b):
    print(a-b)    


def multiplication(a,b):
    print(a*b)


def division(a,b):
    print(a/b)  


def reminder(a,b):
    print(a%b)  

print('welcome to calculator')

print('enter first number:')
n1 = int(input())

print('enter second number:')
n2 = int(input())

addition(n1, n2)
substraction(n1, n2)
multiplication(n1, n2)
division(n1, n2)
reminder(n1, n2)


# Sum Of Natural No.s
num_ = int(input())
Sum_ = num_*(num_+1)/2
print(Sum_)




# Multiplication  Table

i =1
n =2
while i<=10:
     print(n , " * ",i, " = " , n * i)
     i = i + 1



# Generating Random No.

import random
print(random.randint(10,50))



# area Of Triangle

x = 4
y = 5
z = 6

s = (x + y + z)/2

area = (s*(s-x)*(s-y)*(s-z)) ** 0.5
print(area)

# Swapping Variables
n = 4
o = 8

swap = n
n=o
o= swap

print( 'The Value of n after Swapping:', n)
print( 'The Value of o after Swapping:', o)



# Convert Kilometers to Miles

k_m = float(input("Enter kilometer value : ") )

conersion_factor = 0.621371

miles = k_m * conersion_factor
print(k_m ,'Kilometer equals to' , miles, 'miles')


