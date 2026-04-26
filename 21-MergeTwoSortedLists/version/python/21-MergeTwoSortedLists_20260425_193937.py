# Last updated: 4/25/2026, 7:39:37 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        head = ListNode()
9        current = head
10
11        while list1 and list2:
12            if list1.val < list2.val:
13                current.next = list1
14                list1 = list1.next
15            else:
16                current.next = list2
17                list2 = list2.next
18            current = current.next
19        
20        current.next = list1 or list2
21        return head.next
22        
23        
24        