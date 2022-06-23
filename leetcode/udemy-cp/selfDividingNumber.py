left = int(input("Enter left: "))
right = int(input("Enter right: "))
sdnList = []

for number in range(left, right+1):
	strnum = str(number)
	listnum = list(strnum)
	for digit in listnum:
		if int(digit) == 0:
			isSDN = False
			break
		elif number % int(digit) == 0:
			isSDN = True
		else:
			isSDN = False
			break
	if isSDN == True:
		sdnList.append(number)

print(sdnList)


