# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return (self.isValidBST(root.left) and 
                self.isValidBST(root.right) and
                self.dfs(root.left, root.val, True) and
                self.dfs(root.right, root.val, False))
    def dfs(self, node, rootVal, left):
        if not node:
            return True
        if left:
            if node.val >= rootVal:
                return False
        else:
            if node.val <= rootVal:
                return False
        return self.dfs(node.left, rootVal, left) and self.dfs(node.right, rootVal, left) 