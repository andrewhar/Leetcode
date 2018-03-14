class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        st=haystack
        n=needle
        for a in range(len(st)-len(n)+1):
            if st[a:(a+len(n))]==n:
                return a
        return -1
                
        