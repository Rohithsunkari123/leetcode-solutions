class Solution(object):
    def longestOnes(self, nums, k):
        numz=0
        l=0
        wmax=0
        for r in range(len(nums)):
            if nums[r]==0:
                numz+=1
            while numz>k:
                if nums[l]==0:
                    numz-=1
                l+=1
            wmax=max(wmax,r-l+1)
        return wmax