class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        l = 1
        r = sum(candies) // k
        res = 0

        while l <= r:
            m = (l + r) // 2

            count = 0

            for c in candies:
                count += c // m

            if count >= k:
                res = m
                l = m + 1
            else:
                r = m - 1

        return res