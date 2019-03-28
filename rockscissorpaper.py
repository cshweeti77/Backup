import random

listc =[]

list1 = [[0, 1], [2, 0], [1, 2]], [[0, 2], [2, 1], [1, 0]]

print("0. Rock \n 1. Scissor \n 2. Paper")
choice = int(input("enter a choice::")

listc.append(choice)

computer = random.randint(0, 2)

listc.append(computer)

print(choice, computer)

if (choice == computer):
	print("Draw")
else:
	if listc in list1[0]:
		print("user wins")
	else:
		print("computer wins")

