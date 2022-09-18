def isPalindrome(string):
    # O(n) time | O(n) space
    string_list = list(string)
    string_list_reversed = string_list[::-1]

    string_reversed = "".join(string_list_reversed)
    
    if string == string_reversed:
        return True
    else:
        return False
