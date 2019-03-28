#!usr/bin/python
#Author::Sweeti Chauhan
#this program calculates the area of scalar Triangle

import math

def calculate(a,b,c):
	assert a+b >= c or a+c >= b or b+c >= a
	s = (a+b+c)/2
	A = s * (s - a) * (s - b) * (s - c)
	return math.sqrt(A)

def main():
	print("Enter three sides of triangle:")
	x = int(input("1st side::"))
	y = int(input("2nd side::"))
	z = int(input("3rd side::"))
	s = calculate(x,y,z)
	print("The Area of triangle::", s)

if __name__=='__main__':
	main()
	
