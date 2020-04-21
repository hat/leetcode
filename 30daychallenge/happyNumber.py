# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example: 

# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# TODO look into using walrus operator
# TODO take return False out of main loop - only one return statement in a function

class Solution:

    def isHappyFromMemory(self, n: int) -> bool:
        squares = []
        solution = 0
        while solution != 1:
            solution = 0
            for num in str(n):
                solution += int(num) ** 2
            if solution in squares:
                return False
            squares.append(solution)
            n = solution
        return True

    def isHappy(self, n: int) -> bool:
        loop_list = []
        while n != 1:
            new_num = 0
            for num in str(n):
                new_num += int(num) ** 2
            n = new_num
            if new_num in loop_list:
                return False
            loop_list.append(new_num)

        return True
    
solution = Solution()
print(solution.isHappyFromMemory(19))


# ans = Solution().isHappy(7)
# print(ans)