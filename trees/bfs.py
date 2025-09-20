def bfs(root):
    if not root:
        return[]
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


#level wise defined

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        levelsize = len(queue)
        level = []
        for _ in range(levelsize):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result