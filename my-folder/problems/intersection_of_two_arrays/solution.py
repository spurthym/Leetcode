class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums=[]
        for each in nums2:
            if each in nums1:
                nums.append(each)
            else:
                continue
            
        return set(nums)
        