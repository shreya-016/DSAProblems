class Solution(object):
    
    def maxDepthTree(self, root):
        if root is none:
            return 0
        else:
            return 1 + max((self.maxDepthTree(root.left)) and (self.maxDepthTree(root.right)))
