
def pattern2(n):
    if n == 0:
        return
    for i in range(1, n+1):
        print(i, end=" ")
    print()
    pattern2(n-1)

n = int(input("Enter a number: "))
pattern2(n)