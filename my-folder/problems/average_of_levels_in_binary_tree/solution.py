# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        d=defaultdict(list)
        curr=root
        maxl=0
 


        def avg(curr,level):
            if curr==None:
                return 0
            if level not in d:
                d[level].append(0)
                d[level].append(0)
            d[level][0]=d[level][0]+curr.val
            d[level][1]=d[level][1]+1



            avg(curr.left,level+1)
            avg(curr.right,level+1)
        
        avg(curr,0)

        


        print(d)
        res=[d[0][0]]
        for i in range(1,len(d)):
            res.append(d[i][0]/d[i][1])
        return res


            
            
