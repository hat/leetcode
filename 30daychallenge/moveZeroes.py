# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Note:

#     You must do this in-place without making a copy of the array.
#     Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zeros = nums.count(0)
        ind = 0

        while ind < len(nums):
            # if nums at index ind is 0, remove and move back an index
            if nums[ind] == 0:
                nums.pop(ind)
                ind -= 1
            ind += 1
        # append zeros back into list
        while num_zeros > 0:
            nums.append(0)
            num_zeros -= 1

answer = Solution()
arr = [0,1,0,3,12]
answer.moveZeroes(arr)
print(arr)

