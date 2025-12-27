from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_parent_map_and_find_target(root, target):
    parent = {}
    target_node = None
    q = deque([root])

    while q:
        node = q.popleft()
        if node.val == target:
            target_node = node
        if node.left:
            parent[node.left] = node
            q.append(node.left)
        if node.right:
            parent[node.right] = node
            q.append(node.right)

    return parent, target_node

def burn_tree(root, target):
   
    if not root:
        return

    parent, target_node = build_parent_map_and_find_target(root, target)
    if not target_node:
        return  

    visited = set()
    q = deque()

    q.append(target_node)
    visited.add(target_node)

    while q:
        level_size = len(q)
        current_level_vals = []

        for _ in range(level_size):
            node = q.popleft()
            current_level_vals.append(node.val)

            if node.left and node.left not in visited:
                visited.add(node.left)
                q.append(node.left)

            if node.right and node.right not in visited:
                visited.add(node.right)
                q.append(node.right)

            if node in parent and parent[node] not in visited:
                visited.add(parent[node])
                q.append(parent[node])

        print(", ".join(str(x) for x in current_level_vals))



if __name__ == "__main__":
   
   

    pass
