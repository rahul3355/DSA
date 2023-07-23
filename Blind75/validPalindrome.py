class Solution(object):
    def isPalindrome(self, s):
        properString = self.getProperString(s)
        reverseString = self.getReverseString(properString)

        if properString == reverseString:
            return True
        else:
            return False

    def getProperString(self, sentence):
        sentence = list(sentence)
        properSentence = []
        for i in range(len(sentence)):
            if sentence[i].isalpha() or sentence[i].isdigit():
                character = sentence[i].lower()
                properSentence.append(character)
        
        properString = ''.join(properSentence)
        return properString

    def getReverseString(self, word):
        word = word[::-1]
        return word
