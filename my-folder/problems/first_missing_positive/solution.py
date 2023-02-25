class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        adder=0
        
        while 1+adder in s:
            adder+=1
        return 1+adder