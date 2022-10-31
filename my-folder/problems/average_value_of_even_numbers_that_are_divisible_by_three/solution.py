class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s=0
        c=0
        
        for each in nums:
            if each%2==0 and each%3==0:
                s+=each
                c+=1
        if c==0:
            return 0
        return s//c
        