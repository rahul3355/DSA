# 12143
# sum(1214) + 3
# sum (121) + 4
def sumOfDigits(n):
    if n == 0:
        return 0
    lastDigit = n % 10
    remainingNumbers = n // 10
    return sumOfDigits(remainingNumbers) + lastDigit


n = int(input("Enter number: "))
print(sumOfDigits(n))