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
    def isHappy(self, n: int) -> bool:
        all_nums = []
        while n != 1:
            string_num = str(n)
            new_answer = 0
            for num in string_num:
                #print(f"cur: {num}")
                new_answer += int(num) ** 2
            if n in all_nums:
                return False
            all_nums.append(n)
            n = new_answer
            #print(f"answer: {n}")
        return bool(n)
    
solution = Solution()
print(solution.isHappy(12))