class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        l=1
        r=max(ranks)*cars*cars
        def isvalid(m):
            c=0
            for n in ranks:
                c+=math.isqrt(m//n)
                if c>=cars:
                    return True
            return False
        while l<=r:
            m=l+(r-l)//2
            if isvalid(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res
        