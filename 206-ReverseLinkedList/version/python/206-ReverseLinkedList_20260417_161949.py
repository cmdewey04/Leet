# Last updated: 4/17/2026, 4:19:49 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        
9        curr = head
10        prev = None
11        while curr:
12            tmp = curr.next
13            curr.next = prev
14            prev = curr
15            curr = tmp
16        return prev
17           
18
19