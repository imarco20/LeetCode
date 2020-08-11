"""
2. Min Stack
https://leetcode.com/problems/min-stack/
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = None

    def push(self, x: int) -> None:
        self.data.append(x)
        if self.min is None:
            self.min = x
        elif x < self.min:
            self.data.append(2*x - self.min)
            self.min = x

    def pop(self) -> None:
        print(self.min)
        if self.data[-1] < self.min:
            print("true")
            self.min = (2*self.min) - self.data[-1]
            print(self.data[-1])
            print(self.min)
        del self.data[-1]

    def top(self) -> int:
        print(self.data)
        return self.data[-1]

    def getMin(self) -> int:
        return self.min
