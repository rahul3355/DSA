def caesarCipherEncryptor(string, key):
    # O(n) time | O(n) space
    string_list = list(string)
    key = key % 26
    new_list = []
    for i in range(len(string_list)):
        currChar = string_list[i]
        ascii_currChar = ord(currChar)
        new_ascii = (ascii_currChar + key)
        if new_ascii <= 122:
            new_list.append(chr(new_ascii))
        else:
            newChar = 96 + new_ascii % 122
            new_list.append(chr(newChar))
    newString = "".join(new_list)
    return newString
            
        



# Algorithm:
# 1. Iterate over each character of string and append key to its ascii code
# 2. Append this new character to new string
# 3. Join new string and return