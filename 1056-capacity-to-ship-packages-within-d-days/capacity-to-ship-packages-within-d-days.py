class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        def canship(can):
            ships=1
            currcap=can
            for w in weights:
                if currcap-w<0:
                    ships+=1
                    currcap=can
                currcap-=w
            return ships<=days
        while l <= r:
            can=(l+r)//2
            if canship(can):
                res=min(res,can)
                r=can-1
            else:
                l=can+1
        return res
        