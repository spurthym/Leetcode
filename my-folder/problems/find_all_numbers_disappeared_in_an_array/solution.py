class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        f=collections.Counter(nums)
        op=[]
        for i in range(1,len(nums)+1):
            if i not in f:
                op.append(i)
        
        return op