"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.

Note:

    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        if len(s1) > len(s2):
            return False
        
        while i < len(s2):
            if s2[i] in s1:
                temp_arr = [char for char in s1]
                j = i
                while j < len(s2):
                    if s2[j] not in temp_arr:
                        break
                    temp_arr.pop(temp_arr.index(s2[j]))
                    if len(temp_arr) == 0:
                        return True
                    j = j + 1
            i = i + 1
        return False

    def checkInclusionOptimized(self, s1: str, s2: str) -> bool:
        
        s1_map = [0] * 26
        s2_map = [0] * 26

        for char in s1:
            s1_map[ord(char) - 97] += 1 # s1_map[ord(char) - 97] + 1

        for index, char in enumerate(s2):
            s2_map[ord(char) - 97] += 1
            if index >= len(s1):
                s2_map[ord(s2[index - len(s1)]) - 97] -= 1
            if index >= len(s1) - 1 and s1_map == s2_map:
                return True
        return False

answer = Solution()
print(answer.checkInclusion("adc", "dcda"))


class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.checkInclusionOptimized("hello", "ooolleoooleh") == False
    
    def test_two(self):
        assert self.answer.checkInclusionOptimized(s1 = "ab", s2 = "eidbaooo") == True
    
    def test_three(self):
        assert self.answer.checkInclusionOptimized("adc", "dcda") == True