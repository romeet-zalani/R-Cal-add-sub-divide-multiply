#!/bin/python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select Operation :-")
print("1. To Add ")
print("2. To Subtract ")
print("3. To Multiply ")
print("4. To Divide")

choice = input("Enter choice :- 1,2,3,4 :-\n")
print("You choose to have %s" % choice)

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

if choice == 1:
    print( add(num1,num2))
elif choice == 2:
    print( subtract(num1,num2))
elif choice == 3:
    print( multiply(num1,num2))
elif choice == 4:
    print( divide(num1,num2))
else:
   print("Select from 1,2,3,4 Only.")
