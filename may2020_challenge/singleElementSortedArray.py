"""
You are given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once. Find this single element that appears only once.

Note: Your solution should run in O(log n) time and O(1) space.
"""

class Solution:
    def singleNonDuplicate(self, nums: [int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single

class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.singleNonDuplicate([1,1,2,3,3,4,4,8,8]) == 2

    def test_two(self):
        assert self.answer.singleNonDuplicate([3,3,7,7,10,11,11]) == 10

    def test_three(self):
        assert self.answer.singleNonDuplicate([1]) == 1