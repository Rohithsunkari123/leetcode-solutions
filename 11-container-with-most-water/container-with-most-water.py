class Solution(object):
    def maxArea(self, height):
        res=0
        l=0
        r=len(height)-1
        while l < r:
            area=min(height[l],height[r])*(r-l)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            res=max(res,area)
        return res
        