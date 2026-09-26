class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        def can_distro(x):
            stores=0
            for q in quantities:
                stores+=math.ceil(q/x)
            return stores<=n
        l=1
        r=max(quantities)
        res=0
        while l <= r:
            x=(l+r)//2
            if can_distro(x):
                res=x
                r=x-1
            else:
                l=x+1
        return res
                
        