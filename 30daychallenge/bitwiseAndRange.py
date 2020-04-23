# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

# Example 1:

# Input: [5,7]
# Output: 4

# Example 2:

# Input: [0,1]
# Output: 0

import math

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        solution = m
        
        if m == 0:
            return 0
        if int(math.log(m, 2)) != int(math.log(n, 2)):
            return 0
        for num in range(m + 1, n + 1):
            solution &= num
        return solution