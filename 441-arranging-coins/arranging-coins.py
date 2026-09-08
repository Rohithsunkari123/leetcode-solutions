class Solution:
    def arrangeCoins(self, n: int) -> int:
        res=0
        l=1
        r=n
        while l<=r:
            mid=(l+r)//2
            coin=(mid/2)*(mid+1)
            if coin > n:
                r=mid-1
            else:
                l=mid+1
                res=max(mid,res)
        return res