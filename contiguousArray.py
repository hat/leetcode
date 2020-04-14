# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:

# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Example 2:

# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        count_0 = 0
        count_1 = 0
        cur_max = 0
        # need to loop starting at each index
        for ind, num in enumerate(nums):
            if num == 0 or num == 1:
                if num == 0:
                    count_0 += 1
                elif num == 1:
                    count_1 += 1
                if count_0 == count_1:
                    cur_max = max(cur_max, min(count_0, count_1) +  min(count_0, count_1))
            else:
                count_0 = 0
                count_1 = 0
            if ind == len(nums) - 1 and count_0 == count_1:
                cur_max = max(cur_max, min(count_0, count_1) +  min(count_0, count_1))
        return cur_max

answer = Solution()
print(answer.findMaxLength([0,1,1,0,1,1,1,0]))
print(answer.findMaxLength([0,0,1,0,0,0,1,1]))

