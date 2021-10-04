#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    recursive
    '''
    # def isSymmetric(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     def helper(left, right):
    #         if not left and not right:
    #             return True
    #         if not left or not right:
    #             return False
    #         if left.val!=right.val:
    #             return False
    #         return helper(left.left, right.right) and helper(left.right, right.left)
        
    #     if not root:
    #         return True
    #     else:
    #         return helper(root.left, root.right)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val!=right.val:
                return False
            return helper(left.left, right.right) and helper(left.right, right.left)
        
        if not root:
            return True
        else:
            return helper(root.left, root.right)
# @lc code=end

