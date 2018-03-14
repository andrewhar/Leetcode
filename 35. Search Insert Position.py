class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for a in range(0,len(nums),1):
            if nums[a]==target:
                return a
                break
            elif target<nums[a]:
                return a
                break
            elif a==(len(nums)-1) and target>nums[a]:
                return (a+1)
                break
            