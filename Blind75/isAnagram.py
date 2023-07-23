class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        s = list(s)
        s.sort()

        t = list(t)
        t.sort()

        if s == t:
            return True
        else:
            return False