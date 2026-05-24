# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        cache = {}
        def dfs(root,isSafe):
            if (root,isSafe) in cache:
                return cache[(root,isSafe)]
            if not root:
                return 0
            maxi=0
            if isSafe:
                maxi= root.val+dfs(root.left,False)+dfs(root.right,False)
            cache[(root,isSafe)]= max(maxi,dfs(root.left,True)+dfs(root.right,True))
            return cache[(root,isSafe)]
        return dfs(root,True)