#program to generate numbers RANDOMLY by importing random functions

import random
if random.random() < 0.5:  #random.random generates ramndom number from [0.0,1.0)
	print('Player A can choose to bat')
else:
	print('Player B can choose to bat')

