# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def path(self, root, output):
        if root is None:
            return
        
        self.path(root.left, output)
        output.append(root.val)
        self.path(root.right, output)

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        output = []
        self.path(root, output)
        if not output:
            return True
        ans = True
        first = output[0]
        for second in output[1:]:
            if first >= second:
                ans = False
                break
            first = second
        return ans