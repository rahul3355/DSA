n = int(input("Enter a number: "))
primeList = []
boolPrime = False

if n == 0:
	print(0)
elif n == 1:
	print(0)
elif n == 2:
	print(2)
else:
	primeList.append(2)
	for i in range(2, n):
		
		for j in range(2,i):
			if i % j == 0:
				boolPrime = False
				break
			else:
				boolPrime = True

		if boolPrime == True:
			primeList.append(i)

	print(primeList)

