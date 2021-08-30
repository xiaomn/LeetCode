## 二叉树的前序遍历

## 题目链接：
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

1. 递归法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        while root or len(stack) > 0:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.left 
            if len(stack) > 0:
                root = stack.pop()
                root = root.right
        return ans
      
2. 迭代法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        while root or len(stack) > 0:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.left 
            if len(stack) > 0:
                root = stack.pop()
                root = root.right
        return ans
