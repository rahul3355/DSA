n = int(input())
word_list = []

def replaceWord(str):
	if len(str) <= 10:
		print("".join(str.split()))
	else:
		s = list(str)
		sum = len(s)
		#sum2 = sum -2
		#sumTo = f'{sum2}'
		#str2 = s[0]+sumTo+s[sum-1]
		#print("".join(str2.split()))
		#print(s[0], sum-2 ,s[sum-1])
		print("{s1}{s2}{s3}".format(s1=s[0],s2=sum-2,s3=s[sum-1]))



for i in range(n):
	x = input()
	word_list.append(x)

for i in range(n):
	replaceWord(word_list[i])	 