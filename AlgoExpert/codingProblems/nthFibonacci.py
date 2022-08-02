def getNthFib(n):
    # O(n) time | O(1) space
    firstNumber = 0
    secondNumber = 1

    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    for i in range(n):
        temp = firstNumber
        firstNumber = firstNumber + secondNumber
        secondNumber = temp
    
    return secondNumber