# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head 
        t = {}
        pos = 0
        while(temp is not None):
            if temp not in t:
                t[temp] = 1
            else:
                return True
            temp = temp.next

        return False



