class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(4)
# obj.pop(x)
# param_3 = obj.top()
# param_4 = obj.getMin()


import code
code.interact(local=locals())

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()#   --> Returns -3.
minStack.pop()
minStack.top()#      --> Returns 0.
minStack.getMin()