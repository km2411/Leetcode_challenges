# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # The idea is that every node(apart from the leaf) can have 3 types of path which
    # has to be propogated up to get the maximum at the root.
    # a: half path - max of node and (node with max of both children's half path)
    # b: full path - max of half path and (node with both children's half path)
    # c: max of full path of both the children ->excluding the node -->this would essentially
    # be there in max_seen, can be removed
    
    def mfp(self, root, max_seen):
        #nonlocal max_seen;
        if root == None:
            return (0, 0, max_seen)
        
        (al, bl, max_seenl) = self.mfp(root.left, max_seen)
        (ar, br, max_seenr) = self.mfp(root.right, max_seen)
        
        a = max(root.val, root.val + max(al,ar));
        b = max(a, root.val + al + ar);
        #c = max(root.val, bl, br);
        
        max_seen = max(max_seenl, max_seenr, b)
        print(root.val, a, b, max_seen)
        
        return (a,b, max_seen)
        
    def maxPathSum(self, root: 'TreeNode') -> 'int':
        
        max_seen = float("-inf")
        (a,b, max_seen) = self.mfp(root, max_seen)     
        
        return max_seen
