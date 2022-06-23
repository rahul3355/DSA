n = int(input())

strNum = str(n)
strNumRev = strNum[::-1]

if strNum == strNumRev:
	print("Palindrome")
else:
	print("Not a Palindrome")