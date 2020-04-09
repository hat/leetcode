import re
class Solution:
    def _helper(self, S):
        S = list(S)
        ind = 0
        while ind < len(S):
            if S[ind] == '#':
                S.pop(ind)
                if ind > 0:
                    S.pop(ind - 1)
                ind = -1
            ind += 1
        return ''.join(S)

    def backspaceCompare(self, S: str, T: str) -> bool:
        return self._helper(S) == self._helper(T)

answer = Solution()
#print(answer.backspaceCompare("a##c", "#a#c"))
print(answer.backspaceCompare("y#fo##f", "y#f#o##f"))