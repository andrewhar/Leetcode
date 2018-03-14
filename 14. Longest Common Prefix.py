class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def findcommon(st1,st2):
            if len(st1)>len(st2):
                min=len(st2)
            else:
                min=len(st1)
            temp=""
            for a in range(0,min,1):
                if st1[a]==st2[a]:
                    temp=temp+st1[a]
                else:
                    break
            return temp
                
        empty=False
        if len(strs)==0:
            empty=True
            return ""
            
        only1=False
        if len(strs)==1:
            only1=True
            return strs[0]
        
        only2=False
        if len(strs)==2:
            only2=True
            return findcommon(strs[0],strs[1])
        

        if (empty==False) and (only1==False):
            common=findcommon(strs[0],strs[1])
            for a in range(2,len(strs),1):
                common=findcommon(common,strs[a])
            return common
                
            