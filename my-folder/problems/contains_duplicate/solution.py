class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for each in nums:

            if each in d:
                return True
            d[each]=1
        return False
        