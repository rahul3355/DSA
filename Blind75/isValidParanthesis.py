class Solution(object):
    def isValid(self, s):
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        stack = []

        for character in s:
            if character in closeToOpen:
                if stack and stack[-1] == closeToOpen[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)

        return True if not stack else False