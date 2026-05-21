import random
from typing import Optional
  
# implementation of ListNode for testing
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head: Optional[ListNode] = None

    def create_random(self, size: int):
        """Create linked list with random values"""
        if size <= 0:
            return
        
        self.nums = [random.randint(1, 5) for _ in range(size)]
        self.nums.sort()  # sort to ensure duplicates are adjacent

        self.head = ListNode(self.nums[0])
        curr = self.head

        for num in self.nums[1:]:
            curr.next = ListNode(num)
            curr = curr.next

    def print_list(self):
        curr = self.head

        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next

        print("None")

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head

ll = LinkedList()

# create list of size 8
ll.create_random(8)

print("Original list:")
ll.print_list()

ll.head = Solution().deleteDuplicates(ll.head)

print("\nAfter deleting duplicates:")
ll.print_list()
