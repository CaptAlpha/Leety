class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_head = ListNode()  # Dummy node for the smaller values
        smaller_tail = smaller_head
        greater_head = ListNode()  # Dummy node for the greater values
        greater_tail = greater_head

        current = head

        while current:
            if current.val < x:
                smaller_tail.next = current
                smaller_tail = smaller_tail.next
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next
            
            current = current.next

        smaller_tail.next = greater_head.next  # Connect the smaller list to the greater list
        greater_tail.next = None  # Set the end of the greater list
        
        return smaller_head.next  # Return the head of the merged list
