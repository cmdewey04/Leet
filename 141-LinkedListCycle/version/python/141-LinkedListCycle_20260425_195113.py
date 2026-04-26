# Last updated: 4/25/2026, 7:51:13 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        if not head:
10            return False
11        t = head
12        h = head.next
13        while t != h:
14            if not h or not h.next:
15                return False
16            t = t.next
17            h = h.next.next
18        return True
19        