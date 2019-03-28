from random import *

from collections import Counter

list = ['mango', 'orange', 'apple', 'pear', 'papaya', 'banana']

word = random.choice(list)

letterguessed = ''

print("HANGMAN")
print("HINT::THIS IS THE NAME OF FRUIT")

for i in range(len(word)):
	print('-', end='')
print()

count = len(word) + 2

if __name__ == '__main__':
	while(count != 0):
	
		count -= 1	
		ch = input("ENTER YOUR GUESS::")
	
		if ch in letterguessed:
			print ("Letter already guessed.")
			continue

		if ch in word:
			letterguessed += ch

		for char in word:
			if char in letterguessed:
				print(char, end=' ')
			else:
				print('-', end =' ')

			if(Counter(letterguessed) == Counter(word)):
				print("You won")
				break
	

	if(count == 0):
		print("You lost. The word was ", word)
	
	


