# 5 -> 5 * 4 * 3 * 2 * 1
# n -> n * factorial_number(n-1)

def factorial_number(n):
    if n == 0:
        return 1

    return n * factorial_number(n-1)


n = int(input("Enter number: "))
print(factorial_number(n))
