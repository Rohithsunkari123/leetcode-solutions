class Solution:
    def findMin(self, nums: list[int]) -> int:
        l=0
        r=len(nums)-1
        res=max(nums)
        while l <= r:
            m=(l+r)//2
            if nums[l] < nums[r]:
                res=min(nums[l],res)
                break
            res=min(res,nums[m])
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r=m-1
        return res