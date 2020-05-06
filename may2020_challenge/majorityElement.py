# Majority Element

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3

# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = [0, 0]
        for num in set(nums):
            if nums.count(num) > majority[0]:
                majority[0] = nums.count(num)
                majority[1] = num
        return majority[1]


class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.majorityElement([3,2,3]) == 3

    def test_two(self):
        assert self.answer.majorityElement([2,2,1,1,1,2,2]) == 2
    
    def test_three(self):
        assert self.answer.majorityElement([0,1,2,3,3]) == 3