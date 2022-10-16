class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        
        
        for i in range(len(nums)):
            n=nums[i]
            r=0
            while n!=0:
                temp=n%10
                r=r*10+temp
                n=n//10
            
            nums.append(r)
            
        return len(set(nums))