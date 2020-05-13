"""
Given a non-negative integer num represented as a string,
remove k digits from the number so that the new number is
the smallest possible. 

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
"""

from collections import deque

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            # if last digit appended to stack is greater than current digit, pop before appending
            while k > 0 and len(stack) > 0 and stack[-1] > digit:
                k -= 1
                stack.pop()  
            stack.append(digit)
        if k > 0:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"

answer = Solution()
print(answer.removeKdigits("1432219", 5))

class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.removeKdigits("1432219", 3) == "1219"

    def test_two(self):
        assert self.answer.removeKdigits("10200", 1) == "200"

    def test_three(self):
        assert self.answer.removeKdigits("10", 2) == "0"