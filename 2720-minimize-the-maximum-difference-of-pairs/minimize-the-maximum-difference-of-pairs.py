class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        if p==0: return 0
        def isvalid(t):
            i,cnt=0,0
            while i < len(nums)-1:
                if abs(nums[i]-nums[i+1])<=t:
                    cnt+=1
                    i+=2
                else:
                    i+=1
                if cnt==p:
                    return True
            return False
        l=0
        r=10**9
        res=r
        while l <= r:
            m=l+(r-l)//2
            if isvalid(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res
