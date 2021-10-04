"""
For a give binary tree, return the inorder traversal as a list
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
recursive
'''
class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    def inorder(root, res):
      if not root:
        return []
      inorder(root.left, res)
      res.append(root.val)
      inorder(root.right, res)
      return res
    return inorder(root, [])
  
'''
iterative
'''
def inorder(root, res):
  if not root:
    return []
  stack = []
  res = []
  while (root or stack):
    while root:
      stack.append(root)
      root = root.left
    root = stack.pop()
    res.append(root.val)
    root = root.right
  return res