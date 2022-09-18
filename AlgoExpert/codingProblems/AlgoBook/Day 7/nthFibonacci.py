def getNthFib(n):
    # O(n) time | O(1) space
    if n == 1:
        return 0
    elif n == 2:
        return 1
    firstNumber = 0
    secondNumber = 1
    for i in range(2, n):
        temp = secondNumber
        secondNumber = firstNumber + secondNumber
        firstNumber = temp
        
    return secondNumber
