from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def splitListToParts(head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    heads = [head] * k
    n = 0
    while head:
        n+=1
        head = head.next
    limit = n//k
    head = heads[0]
    i = 0
    curhead = 1
    while head:
        i+=1
        if i == limit:
            heads[curhead % k] = head
            curhead+=1
            i = 0
        head = head.next
    return heads

if __name__ == "__main__":
    splitListToParts()