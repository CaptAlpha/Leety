# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        counter = 0
        temp = head
        li = []
        while(temp is not None):
        
            li.append(temp.val)
            counter+=1
            temp = temp.next
        
        m = 0
        print(li)
        for i in range(counter//2):
            m = max(m, li[i]+li[counter-i-1])

        return m
            

