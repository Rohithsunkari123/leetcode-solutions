class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        def isvalid(m):
            ops=0
            for n in nums:
                ops+=ceil(n/m)-1
                if ops>maxOperations:
                    return False
            return True

        l=1
        r=max(nums)
        res=0

        while l <= r:
            m=l+(r-l)//2
        
            if isvalid(m):
                r=m-1
                res=m
            else:
                l=m+1
        return res
        