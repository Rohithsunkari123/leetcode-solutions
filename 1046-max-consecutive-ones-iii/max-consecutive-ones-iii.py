class Solution(object):
    def longestOnes(self, nums, k):
        l=0
        res=0
        numz=0
        for r in range(len(nums)):
            if nums[r]==0:
                numz+=1
                while numz>k:
                    if nums[l]==0:
                        numz-=1
                    l+=1
            res=max(res,r-l+1)
        return res
        