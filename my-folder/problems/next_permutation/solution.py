class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i,k):
            print("i",i,"k",k)
            while i<=k:
                nums[i],nums[k]=nums[k],nums[i]
                i=i+1
                k-=1
            print(nums)
  
                    

        i=len(nums)-1
        while(i>0 and nums[i]<=nums[i-1]):
            i-=1
        print("ere i",i)
        j=len(nums)-1

        if i>0:
            i-=1
            while nums[i]>=nums[j]:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        k=len(nums)-1
        reverse(i,k)

        

        
            # elif(i==0):
            #     reverse(0,len(nums)-1)
            # else:
            #     swap(i)
            #     print(nums)
            #     break
                
        
        

        

        



        


