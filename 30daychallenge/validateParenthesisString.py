#  Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

#     Any left parenthesis '(' must have a corresponding right parenthesis ')'.
#     Any right parenthesis ')' must have a corresponding left parenthesis '('.
#     Left parenthesis '(' must go before the corresponding right parenthesis ')'.
#     '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
#     An empty string is also valid.

# Example 1:

# Input: "()"
# Output: True

# Example 2:

# Input: "(*)"
# Output: True

# Example 3:

# Input: "(*))"
# Output: True

class Solution:
    def checkValidString(self, s: str) -> bool:
        paren_stack = []
        for char in s:
            if char == '(':
                paren_stack.insert(0,char)
            elif char == ')':
                if paren_stack.count('(') > 0:
                    paren_stack.pop(paren_stack.index('('))
                elif paren_stack.count(' ') > 0:
                    paren_stack.pop(paren_stack.index(' '))
                else:
                    return False
            elif char == '*':
                paren_stack.insert(0,' ')
        if paren_stack.count(' ') == 0 and len(paren_stack) > 0:
            return False
        return True if len(paren_stack) == s.count('*')\
            or len(paren_stack) == 0\
            or paren_stack.count(' ') == paren_stack.count(')') + paren_stack.count('(')\
            else False

answer = Solution()
# ans = answer.checkValidString("(*))") # True
# print(ans)
# ans = answer.checkValidString("(*)") # True
# print(ans)
# ans = answer.checkValidString("(*()") # True
# print(ans)
# ans = answer.checkValidString("(")# False
# print(ans)
# ans = answer.checkValidString("*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)")# False
# print(ans)
ans = answer.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*")
print(ans)