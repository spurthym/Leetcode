class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n=len(nums)

        leftproducts=[0 for x in range(len(nums))]
        rightproducts=[0 for y in range(len(nums))]
        leftproducts[0]=1
        for x in range(1,len(nums)):
            leftproducts[x]=leftproducts[x-1]*nums[x-1]
        rightproducts[-1]=1
        print(leftproducts)
        for y in range(len(nums)-2,-1,-1):
            rightproducts[y]=rightproducts[y+1]*nums[y+1]
        
        res=[]
        for z in range(len(nums)):
            res.append(leftproducts[z]*rightproducts[z])
        return res




        
        



