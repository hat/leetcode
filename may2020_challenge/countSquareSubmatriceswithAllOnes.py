"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Constraints:

    1 <= arr.length <= 300
    1 <= arr[0].length <= 300
    0 <= arr[i][j] <= 1
"""

class Solution:
    def countSquares(self, matrix: [[int]]) -> int:
        # left neightbor
        # right neighbor
        # diagonal neighbor
        count = 0
        
        for col in range(0, len(matrix[0])):
            # handle top row edge case
            if matrix[0][col] == 1:
                count += 1
        for row in range(1, len(matrix)):
            # handle left column edge case
            if matrix[row][0] == 1:
                count += 1
        # handle the rest
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                # minimum of left top and diagonal if current is 1
                if matrix[row][col] != 0:
                    squares = 1 + min(matrix[row-1][col], matrix[row][col-1], matrix[row-1][col-1])
                    count += squares
                    matrix[row][col] = squares
        return count

class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]) == 15

    def test_two(self):
        assert self.answer.countSquares([[1,0,1],[1,1,0],[1,1,0]]) == 7