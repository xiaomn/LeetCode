# 二叉树的后序遍历 左右根
## 题目链接
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/

1. 递归法：
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def postorder(root: TreeNode) -> None:
            if root:
                postorder(root.left)
                postorder(root.right)
                ans.append(root.val)
        postorder(root)
        return ans
2. 迭代法
二叉树的前序遍历是根左右， 后序遍历是左右根，可以先进行根右左遍历得到二叉树后序遍历的逆序列
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        while root or len(stack) > 0:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.right
            if len(stack) > 0:
                root = stack.pop()
                root = root.left
        return ans[::-1]
      
      
3. 迭代法,直接进行迭代
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        pre = None
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == pre:
                pre = root
                ans.append(root.val)
                root = None
            else:
                stack.append(root)
                root = root.right
        return ans
