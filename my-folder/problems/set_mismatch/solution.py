class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # Swap
                
            else:
                i += 1
        
        # After cyclic sort, find the missing number
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]