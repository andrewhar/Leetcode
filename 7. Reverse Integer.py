class Solution:
    def reverse(self, x):
        def check( d: int):
            if (-2**31)<=d<=(2**31-1):
                return True
            else:
                return False
        if check(x):
            if x>=0:
                s1=str(x)
                l1=list(s1)
                tstr=""
                for a in range(0,len(l1),1):
                    tstr=tstr+l1[len(l1)-a-1]
                tint=int(tstr)
                if check(tint) ==False:
                    tint=0
            else:
                s2=str(x)
                l2=list(s2[1:])
                tstr=""
                for a in range(0,len(l2),1):
                    tstr=tstr+l2[len(l2)-a-1]
                tint=int(tstr)
                tint=tint*(-1)
                if check(tint)==False:
                    tint=0                
        else:
            tint=0        
        return tint