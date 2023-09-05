from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def makeList(arr):
    cur = Node(0)
    dummy = cur
    nodes = []
    for i in arr:
        cur.next = Node(i[0],None)
        nodes.append(cur.next)
        cur = cur.next
    cur = dummy
    for i in arr:
        if cur.random:
            cur.random = dummy

    return dummy.next

def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
        return None
    cur = head
    while cur:
        cur.next = Node(cur.val,cur.next)
        cur = cur.next.next
    cur = head
    while cur and cur.next:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next
    cur = head.next
    while cur.next:
        cur.next = cur.next.next
        cur = cur.next
    return head.next

if __name__ == "__main__":
    head = makeList([[7,None],[13,0],[11,4],[10,2],[1,0]])
    ansH = copyRandomList(head)
    while ansH:
        print(ansH.val, ansH.random)
        ansH = ansH.next
    