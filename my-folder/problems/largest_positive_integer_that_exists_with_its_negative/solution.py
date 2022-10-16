class Solution:
	def findMaxK(self, nums: List[int]) -> int:
		nums = sorted(nums)
		index = len(nums)-1
		while index > -1:
			num = nums[index]
			if -num in nums:
				return num
			index = index - 1

		return -1
        
        
            
            
            
            