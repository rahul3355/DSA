n = int(input("Enter number of days: "))

shared = 5
liked = 2
cumulative = 2

print("day: ",1, " shared: ",shared, " liked: ", liked, " cumulative: ",cumulative)

for i in range(2,n+1):
	shared = (shared//2) * 3 
	liked = shared // 2
	cumulative = cumulative + liked
	print("day: ",i, " shared: ",shared, " liked: ", liked, " cumulative: ",cumulative)

	print(cumulative)