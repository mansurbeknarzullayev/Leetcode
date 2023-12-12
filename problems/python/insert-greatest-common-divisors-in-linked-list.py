# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(sefl, a, b):
        return a if b == 0 else gcd(b, a % b)
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        while head:
            if head.next:
                mid = ListNode(self.gcd(head.val, head.next.val), head.next)
                head.next = mid
                head = head.next.next
            else:
                head = head.next
        return ans
