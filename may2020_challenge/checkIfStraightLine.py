#You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# Constraints:

#     2 <= coordinates.length <= 1000
#     coordinates[i].length == 2
#     -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
#     coordinates contains no duplicate point.

class Solution:
    def checkStraightLine(self, coordinates: [[int]]) -> bool:
        if len(coordinates) == 1:
            return True
        change_x = coordinates[0][0] - coordinates[1][0]
        change_y = coordinates[0][1] - coordinates[1][1]
        for ind in range(2,len(coordinates)):
            if (coordinates[ind][0] - coordinates[0][0]) * change_y != (coordinates[ind][1] - coordinates[0][1]) * change_x:
                return False
        return True


class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]) == True

    def test_two(self):
        assert self.answer.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) == False

    def test_three(self):
        assert self.answer.checkStraightLine([[1,4]]) == True
    
    def test_four(self):
        assert self.answer.checkStraightLine([[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]) == True

answer = Solution()
# print(answer.checkStraightLine([[0,1],[1,3],[-4,-7],[5,11]]))
print(answer.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))