class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res=[]
        
        for i,a in enumerate(arr):
            
            if i>0 and a==arr[i-1]:
                continue
            left,right=i+1,len(arr)-1
            
            while left<right:
                threesum=a+arr[left]+arr[right]
                if threesum>0:
                    right-=1
                elif threesum<0:
                    left+=1
                else:
                    res.append([a,arr[left],arr[right]])
                    left+=1
                    right-=1
                    while(arr[left]==arr[left-1]) and left<right:
                        left+=1
                    while(arr[right]==arr[right+1]) and left<right:
                        right-=1
        return res