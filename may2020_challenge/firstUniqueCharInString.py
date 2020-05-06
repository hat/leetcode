# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/
# First Unique Character in a String

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

# Note: You may assume the string contain only lowercase letters. 

class Solution:
    def firstUniqeChar(self, s: str) -> int:
        for char in s:
            if s.count(char) == 1:
                return s.find(char)
        return -1

    def hashMap(self, s: str) -> int:
        chars = {}
        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        for i, char in enumerate(chars):
            if chars[char] == 1:
                return i
        return -1

class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.firstUniqeChar("leetcode") == 0

    def test_two(self):
        assert self.answer.firstUniqeChar("loveleetcode") == 2

    def test_three(self):
        assert self.answer.firstUniqeChar("") == -1

    def test_one_hashmap(self):
        assert self.answer.hashMap("leetcode") == 0

    def test_two_hashmap(self):
        assert self.answer.hashMap("loveleetcode") == 2

    def test_three_hashmap(self):
        assert self.answer.hashMap("") == -1