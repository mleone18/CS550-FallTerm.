import sys

m = int(input('Month by number: '))
d = int(input('Day: '))
y = int(input('Year: '))
a = int(y - (14 - m)/12)
b = int(a + a/4 - a/100 + a/400)
c = int(m + 12*((14 - m)/12)- 5)
e = int(d + b + (31 * c)/12)%7



if e == 0:
 	print('Sunday')
if e == 1: 
	print('Monday')
if e == 2: 
	print('Tuesday')
if e == 3: 
	print('Wednesday')
if e == 4: 
	print('Thursday')
if e == 5: 
	print('Friday')
if e == 6: 
	print('Saturday')




