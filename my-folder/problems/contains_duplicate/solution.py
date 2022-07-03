
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        
        for i in nums:
            if i not in d:
                d[i]=1
            
            if len(nums)==len(d):
                return False
        return True
        