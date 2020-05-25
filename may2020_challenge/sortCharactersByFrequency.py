"""
Given a string, sort it in decreasing order based on the frequency of characters.
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        letters = {}
        frequency_string = ""
        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
        # import code
        # code.interact(local=locals())
        for char in sorted(letters.items(), key=lambda letters: letters[1], reverse=True):
            for i in range(0, char[1]):
                frequency_string += char[0]

        return frequency_string

answer = Solution()
print(answer.frequencySort("tree"))

class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.frequencySort("tree") == "eetr"

    def test_two(self):
        assert self.answer.frequencySort("cccaaa") == "cccaaa"

    def test_three(self):
        assert self.answer.frequencySort("Aabb") == "bbAa"