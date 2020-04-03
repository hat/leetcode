# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5, 4, 5, -4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        # set to first num in array ## can't set to 0 in case all are < 0 in array
        max_possible = nums[0]
        max_current = nums[0]
        
        # go through each number in array and see if adding next number increases max
        for i in nums[1:]:
            max_possible = max(i, max_possible + i)
            max_current = max(max_current, max_possible)

        return max_current

solve = Solution()
print(solve.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))