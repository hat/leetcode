# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:

# Input:nums = [1,1,1], k = 2
# Output: 2

# Note:

#     The length of the array is in range [1, 20,000].
#     The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        for i, num in enumerate(nums):
            for num in nums[i:]:
                if total == k and total <= k:
                    total = 0
                    count += 1
                total += num
        return count