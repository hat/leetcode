# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = answer = ListNode(-1)
        while l1 and l2:
            print(f"{l1.val} + {l2.val} = {l1.val + l2.val % 10} + {carry}")
            answer.next = ListNode(((l1.val + l2.val) % 10) + carry)
            if l1.val + l2.val >= 10:
                carry = 1
            else:
                carry = 0
            print(carry)
            l1 = l1.next
            l2 = l2.next
            answer = answer.next
        return head.next