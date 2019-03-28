#!usr/bin/python3
#version 3
#program to demonstrate usage of function to print upto n  fibonacci number

def fibo(n):
	a, b = 1, 1
	while(a < n):
		print(a)
		a, b =b, a+b

a = int(input("Enter a number::"))
fibo(a)


