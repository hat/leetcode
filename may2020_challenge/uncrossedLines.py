"""
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

    A[i] == B[j];
    The line we draw does not intersect any other connecting (non-horizontal) line.

Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

Note:

    1 <= A.length <= 500
    1 <= B.length <= 500
    1 <= A[i], B[i] <= 2000
"""

class Solution:
    def maxUncrossedLines(self, A: [int], B: [int]) -> int:
        
        dp = [[-1] * (len(B) + 1) for _ in range(len(A) + 1)]
        calculated = [[False] * (len(B) + 1) for _ in range(len(A) + 1)]
        
        def getMax(ind_A, ind_B):
            if ind_A == len(A) or ind_B == len(B):
                return 0
            if calculated[ind_A][ind_B]:
                return dp[ind_A][ind_B]
            
            best = 0
            best = max(best, getMax(ind_A+1, ind_B))
            best = max(best, getMax(ind_A, ind_B+1))
            
            if A[ind_A] == B[ind_B]:
                best = max(best, getMax(ind_A+1,ind_B+1) + 1)
            
            calculated[ind_A][ind_B] = True
            dp[ind_A][ind_B] = best
            return best
            
        return getMax(0,0)

class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.maxUncrossedLines([1,4,2], [1,2,4]) == 2

    def test_two(self):
        assert self.answer.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]) == 3

    def test_three(self):
        assert self.answer.maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1]) == 2

