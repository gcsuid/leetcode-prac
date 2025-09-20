def preorder(root):
    result = []
    def dfs(node):
        if not node:
            return 
        else:
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
    dfs(root)
    return result


def inorder(root):
    result = []
    def dfs(node):
        if not node:
            return 
        else:
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
    dfs(root) 
    return result



def postorder(root):
    result = []
    def dfs(node):
        if not node:
            return 
        else:
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
    dfs(root) 
    return result