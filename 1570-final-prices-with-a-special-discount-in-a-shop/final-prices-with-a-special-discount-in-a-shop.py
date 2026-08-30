class Solution(object):
    def finalPrices(self, prices):
        res = prices[:]
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                res[j] -= prices[i]

            stack.append(i)

        return res
        