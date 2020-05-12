#  An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

# At the end, return the modified image. 

# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# The value of each color in image[i][j] and newColor will be an integer in [0, 65535].


# Check top and bottom
class Solution:
    def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image


answer = Solution()
print(answer.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))

class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2) == [[2,2,2],[2,2,0],[2,0,1]]

    def test_two(self):
        assert self.answer.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]

    def test_three(self):
        assert self.answer.floodFill([[0,0,0],[0,0,0]], 0, 0, 2) == [[2,2,2],[2,2,2]]
    
    def test_four(self):
        assert self.answer.floodFill([[0,0,0],[0,1,0]], 0, 0, 2) == [[2,2,2],[2,1,2]]