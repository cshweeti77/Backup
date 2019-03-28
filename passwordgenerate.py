import string
from random import *
char = string.ascii_letters + string.digits + string.punctuation
for x in range(0,9):
	password = "".join(choice(char))
	print(password, end ="")

print()
