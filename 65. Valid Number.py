class Solution:
    def isNumber(self, s):
        try:
            k = float(s)
            return True
        except ValueError:
            return False