class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=nums
        a=0
        while a<(len(l)+10):
            try:
                if l[a]==l[a+1]:
                    l.pop(a)
                    continue
            except:
                print('except')
            a+=1
        print(l)
        nums=l
        print(nums)
        return len(l)