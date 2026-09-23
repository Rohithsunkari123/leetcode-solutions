class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p==0: return 0
        
        def isvalid(t):
            i=0
            cnt=0
            while i<len(nums)-1:
                if abs(nums[i]-nums[i+1])<=t:
                    i+=2
                    cnt+=1
                else:
                    i+=1
            return cnt>=p

        l=0
        r=10**9
        res=r
        nums.sort()
        while l <= r:
            m=l+(r-l)//2
            if isvalid(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res
        