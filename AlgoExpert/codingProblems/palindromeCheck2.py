def isPalindrome(string):
    # O(n) time | O(1) space
    start = 0
    end = len(string) - 1
    while end > start:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            return False
    return True