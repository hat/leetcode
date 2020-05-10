# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

#     The town judge trusts nobody.
#     Everybody (except for the town judge) trusts the town judge.
#     There is exactly one person that satisfies properties 1 and 2.

# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

    # 1 <= N <= 1000
    # trust.length <= 10000
    # trust[i] are all different
    # trust[i][0] != trust[i][1]
    # 1 <= trust[i][0], trust[i][1] <= N

class Solution:
    def findJudge(self, N: int, trust: [[int]]) -> int:
        voted = []
        trustee = []
        judge = -1
        if N == 1 and len(trust) == 0:
            return 1
        for person in trust:
            voted.append(person[0])
            trustee.append(person[1])
        for num in set(trustee):
            if trustee.count(num) == N - 1:
                judge = num
        if judge in set(voted):
            judge = -1
        return judge

class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.findJudge(3, [[1,3],[2,3],[3,1]]) == -1
    
    def test_two(self):
        assert self.answer.findJudge(3, [[1,2],[2,3]]) == -1

    def test_three(self):
        assert self.answer.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]) == 3

    def test_four(self):
        assert self.answer.findJudge(1, []) == 1

    def test_five(self):
        assert self.answer.findJudge(2, [[1,2]]) == 2

    def test_five(self):
        assert self.answer.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]) == 3