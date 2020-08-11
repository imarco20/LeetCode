"""
5. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        lefty = "({["
        righty = ")}]"

        stack = Stack()

        for c in s:
            if c in lefty:
                stack.push(c)
            elif c in righty:
                if stack.is_empty():
                    return False
                if righty.index(c) != lefty.index(stack.pop()):
                    return False

        return stack.is_empty()


class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0
