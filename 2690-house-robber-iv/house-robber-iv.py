class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l=min(nums)
        r=max(nums)
        res=0
        def is_valid(cap):
            i=0
            count=0
            while i < len(nums):
                if nums[i] <= cap:
                    count+=1
                    i+=2
                else:
                    i+=1
                if count==k:
                    break
            return count == k
            

        while l <= r:
            m=(l+r)//2
            if is_valid(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res
        