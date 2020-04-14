# You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

#     direction can be 0 (for left shift) or 1 (for right shift). 
#     amount is the amount by which string s is to be shifted.
#     A left shift by 1 means remove the first character of s and append it to the end.
#     Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.

# Return the final string after all operations.

 

# Example 1:

# Input: s = "abc", shift = [[0,1],[1,2]]
# Output: "cab"
# Explanation: 
# [0,1] means shift to left by 1. "abc" -> "bca"
# [1,2] means shift to right by 2. "bca" -> "cab"

# Example 2:

# Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
# Output: "efgabcd"
# Explanation:  
# [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
# [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
# [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
# [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"

from collections import deque

class Solution:
    def stringShift(self, s: str, shift: [[int]]) -> str:
        total_left = 0
        total_right = 0
        shift_right = False
        for num in shift:
            if num[0] == 0:
                total_left += num[1]
            elif num[0] == 1:
                total_right += num[1]
        if total_right > total_left:
            shift_right = True

        total_shift = abs(total_left - total_right)
        d = deque(s)
        while total_shift > 0:
            if shift_right:
                d.rotate(1)
            else:
                d.rotate(-1)
            total_shift -= 1

        return ''.join(d)


answer = Solution()
answer.stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]])