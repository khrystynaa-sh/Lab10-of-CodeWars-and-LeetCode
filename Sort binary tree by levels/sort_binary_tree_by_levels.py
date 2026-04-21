from collections import deque

def tree_by_levels(node):
    if node is None: 
        return []
    queue = deque([node])
    result = []
    while queue:
        cur = queue.popleft()
        result.append(cur.value)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return result
