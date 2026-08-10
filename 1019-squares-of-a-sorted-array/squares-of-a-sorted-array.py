class Solution(object):
    def sortedSquares(self, nums):
        l=0
        r=len(nums)-1
        p=len(nums)-1
        res=[0]*len(nums)
        while l<=r:
            left_sq=nums[l]**2
            right_sq=nums[r]**2
            if left_sq>right_sq:
                res[p]=left_sq
                l+=1
            else:
                res[p]=right_sq
                r-=1
            p-=1
        return res
