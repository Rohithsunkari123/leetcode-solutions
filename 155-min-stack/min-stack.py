class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, value):
        self.stack.append(value)
        
        if self.mins:
            self.mins.append(min(value, self.mins[-1]))
        else:
            self.mins.append(value)

    def pop(self):
        self.stack.pop()
        self.mins.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.mins[-1]
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()