def longestBalancedSubstring(string):
    # Write your code here.
    maxLength = 0

    opening = 0
    closing = 0

    for char in string:
        if char == "(":
            opening += 1
        else:
            closing += 1

        if opening == closing:
            maxLength = max(maxLength, closing * 2)
        elif opening < closing:
            opening = 0
            closing = 0

    opening = 0
    closing = 0

    for i in reversed(range(len(string))):
        char = string[i]
        if char == "(":
            opening += 1
        elif char == ")":
            closing += 1

        if opening == closing:
            maxLength = max(maxLength, opening * 2)
        elif opening > closing:
            opening = 0
            closing = 0

    return maxLength
    