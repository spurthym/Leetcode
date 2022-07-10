class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        arr.sort()
        res=[]        
        for i in range(0,len(arr)-3):
            if i>0 and arr[i]==arr[i-1]:
                continue
            for j in range(i+1, len(arr)-2):
                if j>i+1 and arr[j]==arr[j-1]:
                    continue
                left=j+1
                right=len(arr)-1
                
                while left<right:
                    
                    qsum=arr[i]+arr[j]+arr[left]+arr[right]
                    
                    if qsum< target:
                        left+=1
                    elif qsum>target:
                        right-=1
                    else:
                        res.append([arr[i],arr[j],arr[left],arr[right]])
                        left+=1
                        right-=1
                        while left<right and arr[left]==arr[left-1]:
                            left+=1
                        while left<right and arr[right]==arr[right+1]:
                            right-=1
        return res