class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[0 for _ in range(n)]
        l[0]=1
        for i in range(1,n):
            l[i]=l[i-1]*nums[i-1]
        r=[0 for _ in range(n)]
        r[-1]=1
        for j in range(n-2,-1,-1):
            print(j)

            r[j]=r[j+1]*nums[j+1]
        print(r)     

        res=[]

        for k in range(n):
            res.append(l[k]*r[k])
        return res