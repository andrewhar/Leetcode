class Solution(object):
    def lengthOfLongestSubstring(self, s):
    	max=0
    	index=0
    	i=0
    	while i<len(s)-max:
    		nonrepeat={}
    		length=0
    		index=0
	    	for a in range(i,len(s)):
		    	if not((s[a]) in nonrepeat):
		    		key=str(s[a])
		    		nonrepeat[key]=a
		    		length=length+1
		    		print(nonrepeat)
		    	else:
		    		key=str(s[a])
		    		nonrepeat[key]=a
		    		print(nonrepeat)
		    		index=int(nonrepeat.get(key))
		    		i=index+1
		    		print("i: ")
		    		print(i)
		    		break;
    		if length>max:
    			max=length
    			print(max)
    		if i==(len(s)-max) and max==1 and a+1<len(s):
		    	if not((s[a+1]) in nonrepeat):
		    		max=2
		    		return max
    	return max


