class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0 for x in range(n)]
        res_arr_idx=n-1
        ptr1=0
        ptr2=n-1
        
        while ptr1<=ptr2:
            if abs(nums[ptr2])>abs(nums[ptr1]):
                res[res_arr_idx]=nums[ptr2]*nums[ptr2]
                ptr2-=1
            else:
                res[res_arr_idx]=nums[ptr1]*nums[ptr1]
                ptr1+=1
                
            res_arr_idx-=1
        return res