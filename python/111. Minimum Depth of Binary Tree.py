from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    if not root.left:
        return minDepth(root.right)+1
    if not root.right:
        return minDepth(root.left)+1
    return min(minDepth(root.right), minDepth(root.left)) +1

def buildTree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while i < len(nodes):
        current_node = queue.pop(0)
        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)
        i += 1

    return root

root = buildTree([2, None, 3, None, 4, None, 5, None, 6])
print(minDepth(root))
root = buildTree([3,9,20,None,None,15,7])
print(minDepth(root))