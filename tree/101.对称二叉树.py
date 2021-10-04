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
        # helper就是每个节点要做的事情
        # 左右孩子都不存在, 对称
        # 左右孩子一个存在一个不存在, 不对称
        # 左右孩子都存在:
        #     1.  如果左右孩子的值不相等, 不对称
        #     2. 如果左右孩子的值相等, 这一层判断结束, 去下一层.
        # def helper(left, right):
        #     if not left and not right:
        #         return True
        #     if not left or not right:
        #         return False
        #     if left.val!=right.val:
        #         return False
        #     return helper(left.left, right.right) and helper(left.right, right.left)
        
        # if not root:
        #     return True
        # else:
        #     return helper(root.left, root.right)
        
        # iterative
        from collections import deque
        queue = deque([root])
        while queue:
            level_list = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    level_list.append('#')
                else:
                    level_list.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level_list[:] == level_list[::-1]:
                continue
            else:
                return False
        return True
        
# @lc code=end

