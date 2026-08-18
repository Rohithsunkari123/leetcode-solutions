class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        close_sum=float("inf")
        for i, a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l < r:
                curr=a+nums[l]+nums[r]
                if abs(curr-target)<abs(close_sum-target):
                    close_sum=curr
                if curr == target:
                    return curr
                elif curr<target:
                    l+=1
                else:
                    r-=1
        return close_sum

               
                
