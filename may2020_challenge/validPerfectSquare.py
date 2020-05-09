# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Output: true

# Example 2:

# Input: 14
# Output: false

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num // 2
        if num == 1 or num == 2:
            return True
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == num:
                return True
            elif mid * mid >= num:
                high = mid - 1
            else:
                low = mid + 1
        return False

class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.isPerfectSquare(16) == True
    
    def test_two(self):
        assert self.answer.isPerfectSquare(14) == False

    def test_three(self):
        assert self.answer.isPerfectSquare(2) == True

    def test_four(self):
        assert self.answer.isPerfectSquare(1) == True