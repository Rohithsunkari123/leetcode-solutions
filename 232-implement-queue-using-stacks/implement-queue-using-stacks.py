class MyQueue(object):

    def __init__(self):
        self.s1=[]
        self.s2=[]
        

    def push(self, x):
        self.s1.append(x)

        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

        """
        :rtype: int
        """
        

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]
        """
        :rtype: int
        """
        

    def empty(self):
        return len(self.s1)==0 and len(self.s2)==0 
        """
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()