# if statements


n = 1

if n > 2:
	n -= 1
	print("n = ", n)

elif n == 2:
	n *= 2
	print("n = ", n)

else:
	n += 3
	print("n = ", n)

n, m = 3, 2
if ((n > 2) and
	(n != m) or (n == m)):
		n += 881
		print("n = ", n)