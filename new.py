#!usr/bin/python
#this program imports functions from script.py to perform arithmetic operations
#Author::Sweeti Chauhan

from script import *                    # import * to import all functions from script.py whereas import fn_name to import specific function
num1 = int(input("enter 1st number::"))
num2 = int(input("enter 2nd number::"))
sum = add(num1,num2)
print("Sum::", sum)


