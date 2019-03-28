#!cd/usr/bin/python
#version3
#Program::Python as a calculator using Functions
#Author::Sweeti Chauhan

def calculate():
	ch = input ('''
Please select an operator::
+ for Addition
- for Subtraction
* for Multiply
\ for Division
''')
	a = int(input("Enter a number::"))
	b = int(input("enter another number::"))
	if (ch == '+'):
		print('{} + {}= ' .format(a, b))
        	print(a+b)	
	elif (ch == '-'):
		print('{} - {}= ' .format(a, b))
	        print(a-b)
	elif (ch == '*'):
		print('{} * {}= ' .format(a, b))
        	print(a*b)
	elif (ch == '/'):
		print('{} / {}= ' .format(a, b))
        	print(a/b)
	else:
		print("Invalid choice. Please enter valid choice")
	#Add again function to the calculate function
	again()


def again():
	ag = input('''
Do you want to calculate again:::
Type Y for yes N for no
''')
	if(ag.upper() == 'Y'):
		calculate()
	elif(ag.upper() == 'N'):
		print("See you later")
	else:
		again()


def welcome():
	print("Welcome to Calculator")
#call calculate function outside the def
welcome()
calculate()

