def Digitsum(n):
	n = int(n)
	if n >= 0 and n < 10:
		return n
	elif n < 0:# wanted to try challenge and see if I could find sum negative number digits. 
		return -(abs(n)%10 + Digitsum(abs(n)//10))
	else: #basically taking any integer and dividing by 10 until it is less than 10. Then it returns that digit, then adds up the numerical value of each of the remainders that were returned from each division.  
		return n%10 + Digitsum(n//10)

print(Digitsum(0))
print(Digitsum(25))
print(Digitsum(8))
print(Digitsum(47888))
print(Digitsum(3689))
print(Digitsum(-25))


def cleaned(a): 
	if len(a) == 1:
		return a[0]
	else:
		if a[0] == a[1]:
			return cleaned(a[1:])
		else:
			return a[0] + cleaned(a[1:])

print(cleaned('y'))
print(cleaned('yz'))
print(cleaned('yyz'))
print(cleaned('yzxzz'))
print(cleaned('yyxzz'))
print(cleaned('matthew'))
print(cleaned('aaaaaaaaaaaaaaaaaaaaaaab'))