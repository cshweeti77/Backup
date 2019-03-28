ch = input("Enter a string::")
vowelcount = 0
vowel = 'AEIOUaeiou'
for i in vowel:	
	vowelcount += ch.count(i)

print(vowelcount)
