"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
"""

class Solution:
    def __isAnagram__(self, s, p_map):
        s_map = [0] * 26
        for char in s:
            s_map[ord(char) - 97] = s_map[ord(char) - 97] + 1
        if s_map == p_map:
            return True
        return False
        
    
    def findAnagrams(self, s: str, p: str) -> [int]:
        start_indexes = []
        p_map = [0] * 26
        for char in p:
            p_map[ord(char) - 97] = p_map[ord(char) - 97] + 1
        for i in range(0, len(s)):
            if self.__isAnagram__(s[i:i + len(p)], p_map):
                start_indexes.append(i)
        return start_indexes


class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.findAnagrams("cbaebabacd", "abc") == [0, 6]

    def test_two(self):
        assert self.answer.findAnagrams("abab", "ab") == [0, 1, 2]
