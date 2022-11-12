class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()

        ptr1=0
        ptr2=len(nums)-1
        print(ptr2)
        res=[]
        while ptr1<ptr2:
        
            x=(nums[ptr1]+nums[ptr2])/2
            print(x)
            if x not in res:
                
                res.append(x)
            ptr1+=1
            ptr2-=1
        return len(res)
            
        