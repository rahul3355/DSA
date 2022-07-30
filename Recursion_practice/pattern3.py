
def pattern3(n):
    if n == 1:
        print(1)
        return
    for i in range(1, n+1):
        print(i, end=" ")
    print()
    pattern3(n-1)
    for i in range(1, n+1):
        print(i, end=" ")
    print()


n = int(input("Enter a number: "))
pattern3(n)