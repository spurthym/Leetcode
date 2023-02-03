class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        r=len(nums)-1

        while l<=r:
            while l<r and nums[r-1]==nums[r]:
                r-=1
            while l<r and nums[l+1]==nums[l]:
                l+=1
            
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>=nums[l]:
                if target<nums[l] or target>nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if target>nums[r] or target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
                    
        return False