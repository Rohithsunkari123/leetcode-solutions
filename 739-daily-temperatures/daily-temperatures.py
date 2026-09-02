class Solution(object):
    def dailyTemperatures(self, temperatures):
        res=[0]*len(temperatures)
        stack=[]
        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stat,stai=stack.pop()
                res[stai]=(i-stai)
            stack.append([t,i])
        return res
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        