# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return
        q=[]
        ans=0
        q.append([root,0])
        while len(q)!=0:
            size=len(q)
            minn=q[0][1]
            print(minn)
            for i in range(size):
                curindex=q[0][1]-minn
                node=q[0][0]
                q.pop(0)
                if i==0:
                    first=curindex
                if i==size-1:
                    last=curindex
                if node.left:
                    q.append([node.left,curindex*2+1])
                if node.right:
                    q.append([node.right,curindex*2+2])
            ans=max(ans,last-first+1)
        return ans
        
