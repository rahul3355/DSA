def isValidSubsequence(array, sequence):
    # Write your code here.
    newArray = []

    # O(m * n^2) Time | O(n) Space
    
    # -loop through the sequence
    for element in array:
        # -for each element, check if the element is present in array
        if element in sequence:
            # -if element is also present in sequence
            # -for each element, count of element in subsequence should be >= to count of element in array
            if array.count(element) >= sequence.count(element):
                # -append element into newArray
                newArray.append(element)
            # -newArray length should not exceed sequence length
            if len(newArray) == len(sequence):
                break
    # -check if newArray == sequence? return True; else: return False;    
    if newArray == sequence:
        return True
    else:
        return False

# Algorithm:
# -loop through the sequence
# -for each element, check if the element is present in array
# -if element is also present in sequence
# -for each element, count of element in subsequence should be >= to count of element in array
# -append element into newArray
# -newArray length should not exceed sequence length
# -if sequence == newArray? return True; else False

