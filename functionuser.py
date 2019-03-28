def username():
	uname=input("USERNAME::")
	if not uname.isalnum():
		print("Invalid Username")
		username()

def number():
	num=input("Mobile Number:");
	if not num.isdigit() or (len(num)!=10):
		print("Invalid number")
		number()

def main()		
