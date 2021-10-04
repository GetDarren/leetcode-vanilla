#
# @lc app=leetcode.cn id=144 lang=python
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder(root, res):
            if not root:
                return []
            res.append(root.val)
            preorder(root.left, res)
            preorder(root.right, res)
            return res
        return preorder(root, [])
# @lc code=end
'''
iteration
'''
def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    stack, res = [], []
    while root or stack:
        while root:
            res.append(root.val)
            stack.append(root)
            root = root.left
        root = stack.pop()
        root = root.right
    return res

