class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ptr2=0
        ptr1=0
        while True:
            ptr1=nums[ptr1]
            ptr2=nums[nums[ptr2]]
            if ptr1==ptr2:
                break
        ptr3=0
        while True:
            ptr3=nums[ptr3]
            ptr1=nums[ptr1]
            
            if ptr1==ptr3:
                break
            
            
        return ptr1
                
                
            
        