class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack=[]
        j=0
        for i in  pushed:
            stack.append(i)
            while j<len(popped) and stack and stack[-1]==popped[j]:
                stack.pop()
                j+=1
        return not stack

        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        