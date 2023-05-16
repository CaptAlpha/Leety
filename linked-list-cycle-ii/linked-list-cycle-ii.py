# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = {}
        temp  = head
        counter = 0
        while(temp is not None):
            if temp not in dic:
                dic[temp] = counter
            else:
                return temp

            counter+=1
            temp  = temp.next

        
