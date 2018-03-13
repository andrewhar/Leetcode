class Solution(object):
    def twoSum(self, nums, target):
    	temp= sorted(nums)

    	import numpy
    	index= nums.argsort(nums)

    	print(temp)
    	print(index)
    	a=0	
    	b=a+1
    	#compare nums[a] with other nums[] greater than it
    	while b<=(len(temp)-1):
    		if temp[a]+temp[b]==target:
    			return[a,b]
    			break;
    		if temp[a]+temp[b]>target:
    			break;
    		b=b+1

    print(twoSum(0,[2, 11, 7, 15],9))