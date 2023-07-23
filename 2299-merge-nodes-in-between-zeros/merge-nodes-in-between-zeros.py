# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        temp = head

        res = ListNode(-1)
        temp2 = res
        counter = 0
        flag = 0
        while(temp):
            print(counter)
            if temp.val == 0:
                if flag == 0:
                    flag = 1
                else:
                    temp2.next = ListNode(counter)
                    temp2 = temp2.next
                    counter = 0
            else:
                if flag == 1:
                    counter+=temp.val

            temp = temp.next

        return res.next
                
            

