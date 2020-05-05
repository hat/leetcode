# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]

# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        products = []
        nums = list(dict((num, 0) for num in nums).keys())
        for num_one in nums:
            product = 1
            for num_two in nums[0:]:
                if num_two != num_one:
                    product *= num_two
                if product not in products and product not in nums:
                    products.append(product)
        return products

answer = Solution()
print(answer.productExceptSelf([0,0]))