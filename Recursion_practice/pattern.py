# 1
# 1 2
# 1 2 3
# .
# .
# .
# 1 2 3... (n-1) n




def pattern_number(n):
    if n == 0:
        return
    pattern_number(n-1)
    for i in range(1, n+1):
        print(i,  " ", end=" ")
    print()
    



n = int(input("Enter number: "))
pattern_number(n)