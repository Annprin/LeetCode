# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sym(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        if left.val == right.val:
            return self.sym(left.left, right.right) and self.sym(left.right, right.left)
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        return self.sym(root.left, root.right)
        