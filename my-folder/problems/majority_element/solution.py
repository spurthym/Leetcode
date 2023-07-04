class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize count and candidate variables
        '''
        d=Counter(nums)
        for key, value in d.items():
            if value>len(nums)//2:
                return key


        '''
        count = 0
        candidate = None
        
        for num in nums:
            
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1 
            else:
                count+= -1
            
        return candidate
