from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def makeLinkedList(arr: List[int]) -> ListNode:
    head = ListNode(arr[0])
    prev = head
    for i in range(1, len(arr)):
        prev.next = ListNode(arr[i],None,prev)
        prev = prev.next
    return head
