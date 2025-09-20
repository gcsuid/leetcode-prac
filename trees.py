#dfsrecursion

'''def preorder(node):
    if not node:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)
preorder(root)

#iterative
def preorder_iterative(root):
    stk = [node]
    while stk:
        node = stk.pop()
        if node:
            print(node.val)
            stk.append(node.right)
            stk.append(node.left)
preorder_iterative(root)


def bfs(node):
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        if node:
            print(node.val)
            q.append(node.left)
            q.append(node.right)
bfs(root)


#value in tree
def search(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    return search(node.left, target) or search(node.right, target )'''


#duplicates in array without hashmap
nums = [4,5,6,1,3,1,3,7,6,2,2]
nums.sort()
res = []
for i  in range(len(nums)):
    if nums[i] == nums[i-1]:
        res.append(nums[i])
print(res)