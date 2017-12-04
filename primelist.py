#generate list of prime numbers 1-100

for num in range(1,100):
	if num > 1:
	   for i in range(2,num):
	       if (num % i) == 0:
	           break
	   else:
	       l = [num]
	       print(l)
	else:
	   print(num,"is not a prime number")