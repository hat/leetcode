"""
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Note:

    The relative order inside both the even and odd groups should remain as it was in the input.
    The first node is considered odd, the second node even and so on ...
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # create odd list
        # create even list
        # add them together
        oddHead = ListNode()
        oddTail = oddHead
        evenHead = ListNode()
        evenTail = evenHead
        
        curNode = head
        curParity = 1
        
        while curNode:
            if curParity == 1:
                oddTail.next = curNode
                oddTail = oddTail.next
            else:
                evenTail.next = curNode
                evenTail = evenTail.next
                
            curParity = (curParity + 1) % 2
            lastNode = curNode
            curNode = curNode.next
            lastNode.next = None
            
            
        oddTail.next = evenHead.next
        return oddHead.next

class TestSolution:

    def setup(self):
        self.answer = Solution()

    def test_one(self):
        assert self.answer.oddEvenList([1,2,3,4,5]) == [1,3,5,2,4]