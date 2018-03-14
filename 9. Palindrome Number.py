class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        try:
            s=str(x)
            check=True
            if len(s)!=1:
                for a in range(0,len(s)//2,1):
                    if s[a]!=s[len(s)-a-1]:
                        check =False
        except:
            print('except')
            check = False
        return check
        