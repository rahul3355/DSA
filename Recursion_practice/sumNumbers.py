# 1 + 2 + 3 + ... + (n-1) + n


def sumNumbers(n):
    if n == 1:
        return 1
    return sumNumbers(n-1) + n



n = int(input("Enter number: "))
print(sumNumbers(n))