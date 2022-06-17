class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        '''  
        left=0
        right=len(n)-1
        
        while left<right:
            curr_sum=n[left]+n[right]
            if curr_sum<target:
                left=left+1
            elif curr_sum>target:
                right=right-1
            else:
                return [left+1,right+1]
        return [-1,-1]
            
        
        
        '''
        lookup={}
        
        for i in range(len(n)):
            
            if n[i] in lookup and i>lookup[n[i]]:
                return [lookup[n[i]]+1,i+1]
                
            else:
                lookup[target-n[i]]=i
                print(lookup)
                
    
        """
        Runtime: 309 ms, faster than 6.42% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
        Memory Usage: 14.8 MB, less than 88.27% of Python3 online submissions for Two Sum II - Input Array Is Sorted.

        """