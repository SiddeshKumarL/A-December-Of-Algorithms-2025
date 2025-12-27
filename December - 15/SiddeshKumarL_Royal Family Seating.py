from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values:
        return None
    nodes = []
    for v in values:
        if v is None:
            nodes.append(None)
        else:
            nodes.append(TreeNode(v))
    i = 0
    j = 1
    while j < len(nodes):
        if nodes[i] is not None:
            if j < len(nodes):
                nodes[i].left = nodes[j]
                j += 1
            if j < len(nodes):
                nodes[i].right = nodes[j]
                j += 1
        i += 1
    return nodes[0]

def is_complete_tree(root):
    if not root:
        return True
    q = deque([root])
    seen_null = False
    while q:
        node = q.popleft()
        if node is None:
            seen_null = True
        else:
            if seen_null:
                return False
            q.append(node.left)
            q.append(node.right)
    return True

tokens = input().split()
vals = []
for t in tokens:
    if t == "null":
        vals.append(None)
    else:
        vals.append(int(t))

root = build_tree(vals)
print("true" if is_complete_tree(root) else "false")
