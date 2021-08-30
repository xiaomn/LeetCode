## 二叉树的中序遍历
## 题目链接
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/submissions/
  
1. 递归法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def inorder(root: TreeNode) -> None:
            if root:
                inorder(root.left)
                ans.append(root.val)
                inorder(root.right)
        inorder(root)
        return ans
2.迭代法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
            if len(stack) > 0:
                root = stack.pop()
                ans.append(root.val)
                root = root.right
        return ans
