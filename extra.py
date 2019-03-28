#!usr/bin/python
#Author::Sweeti Chauhan

import math

def findroot(a,b,c):
	d = pow(b,2) - 4*a*c
	if (d < 0):
		print ("\nImaginary Roots")
		d = abs(d) ; d = math.sqrt(d)
		real = -b / (2 * a)
		img = d / (2 * a)
		print ("\nRoot = ",str(real) + ' + ' +  str(img) + 'j')
	else:
		print ("\nReal Roots")
		d = math.sqrt(d)
		root1 = (-b + d) / (2 * a)
		root2 = (-b - d) / (2 * a)
		print ("\nRoot1 =", root1) ; print ("\nRoot2 =", root2) 
		


def main():
	print("Enter the values of a,b,c of Quadratic Equation::")
	a = float(input()) ; b = float(input()) ; c = float(input())
	findroot(a,b,c)
	

if __name__ == '__main__':
	main() 
	
	
