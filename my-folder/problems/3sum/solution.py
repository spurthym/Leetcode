class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res=[]
        
        for i,a in enumerate(arr):
            if i>0 and a==arr[i-1]:
                continue
            
            left=i+1
            right=len(arr)-1
            
            while left<right:
                s=a+arr[left]+arr[right]
                if s<0:
                    left+=1
                elif s>0:
                    right-=1
                else:
                    res.append([a,arr[left],arr[right]])
                    left+=1
                    right-=1
                    while left<right and arr[left]==arr[left-1]:
                        left+=1
                    while left<right and arr[right]==arr[right+1]:
                        right-=1
        return res
                    
                    