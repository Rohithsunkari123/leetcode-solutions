import collections

class Solution(object):
    def totalFruit(self, fruits):
        l = 0
        total = 0
        res = 0
        count = collections.defaultdict(int)

        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1

            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1
                total -= 1

                if count[f] == 0:
                    count.pop(f)

                l += 1

            res = max(res, total)

        return res