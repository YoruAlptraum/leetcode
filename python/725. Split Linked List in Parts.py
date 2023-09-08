from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def makeList(arr: List[Optional[int]]):
    head = ListNode()
    dummy = head
    for i in arr:
        head.next = ListNode(i)
        head = head.next
    return dummy.next
            

def splitListToParts(head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    n = 0
    cur = head
    while cur:
        n+=1
        cur = cur.next
    extra = n%k

    heads = [head]
    
    for i in range(k-1):
        j = 0
        while head and (j < n//k-1 or (i<extra and j < n//k)):
            j+=1
            head = head.next
        if head:
            head.next, head = None, head.next
        heads.append(head)
    return heads

if __name__ == "__main__":
    head = makeList([1,2,3,4,5,6,7,8,9,10]) # expected [[1,2,3,4],[5,6,7],[8,9,10]]
    ans = splitListToParts(head, k = 3)
    final = []
    for i in ans:
        arr = []
        while i:
            arr.append(i.val)
            i = i.next
        final.append(arr)
    print(final)
    print([[1,2,3,4],[5,6,7],[8,9,10]])
