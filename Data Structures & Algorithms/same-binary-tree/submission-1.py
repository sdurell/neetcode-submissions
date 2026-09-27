# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((p, q))
        while queue:
            Np, Nq = queue.popleft()
            if (not Np and Nq) or (Np and not Nq):
                return False
            elif not Np and not Nq:
                continue
            if Np.val != Nq.val:
                return False
            queue.append((Np.left, Nq.left))
            queue.append((Np.right, Nq.right))
        return True
