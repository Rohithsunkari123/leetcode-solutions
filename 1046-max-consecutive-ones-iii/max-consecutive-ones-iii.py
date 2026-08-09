class Solution(object):
    def longestOnes(self, nums, k):
        l=0
        res=0
        cz=0
        for r in range(len(nums)):
            if nums[r]==0:
                cz+=1
                while cz>k:
                    if nums[l]==0:
                        cz-=1
                    l+=1
            res=max(res,r-l+1)
        return res

            

