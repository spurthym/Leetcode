class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        returnlist,l,r=[0]*length,[0]*length,[0]*length
        l[0]=1
        for i in range(1,len(nums)):
            l[i]=l[i-1]*nums[i-1]
            
        r[-1]=1
        for i in reversed(range(len(nums)-1)):
            r[i]=r[i+1]*nums[i+1]
            
        for i in range(length):
            returnlist[i]=l[i]*r[i]
        
        
            
        return returnlist