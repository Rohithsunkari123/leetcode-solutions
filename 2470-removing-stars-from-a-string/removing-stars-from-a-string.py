class Solution(object):
    def removeStars(self, s):
        stack=[]
        for i in s:
            if stack and i == "*":
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
        """
        :type s: str
        :rtype: str
        """
        