pcount = 0
ncount = 0
negation = 0

inp = input("Enter a text::")
inp = inp.split(" ")
data1 = open("pos.txt").read()
data1 = data1.split(",")
data2 = open("neg.txt").read()
data2 = data2.split(",")
data3 = open("negation.txt").read()
data3 = data3.split(",")
for count in inp:
	if count in data1:
		pcount += 1
	if count in data2:
		ncount += 1
	if count in data3:
		negation += 1

if  negation != 0:
	if pcount < ncount:	
		print("Positive sentence")
	elif ncount < pcount:
		print("Negative sentence")
	else:
		print("Neutral Sentence")
else:
	 if pcount > ncount:
                print("Positive sentence")
	 elif ncount > pcount:
                print("Negative sentence")   
	 else:
                print("Neutral Sentence")
