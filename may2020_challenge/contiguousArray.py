"""
Given a binary array, find the maximum length of a contiguous subarray
with equal number of 0 and 1. 

Note: The length of the given binary array will not exceed 50,000. 
"""

class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        dp = {}
        count = 0
        longest = 0
        
        dp[0] = -1
        for index, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
                
            if count not in dp:
                dp[count] = index
            
            longest = max(index - dp[count], longest)
            
        return longest


answer = Solution()
print(answer.findMaxLength([0,1,0,1,1,1,0,1,0,1,0,1,0,1]))

class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.findMaxLength([0,1]) == 2
    
    def test_two(self):
        assert self.answer.findMaxLength([0,1,0]) == 2

    def test_three(self):
        assert self.answer.findMaxLength([]) == 0

    def test_four(self):
        assert self.answer.findMaxLength([0,1,0,1,1,1,0,1,0,1,0,1,0,1]) == 8

    def test_five(self):
        assert self.answer.findMaxLength([0,0,0,1,1,1,0]) == 6