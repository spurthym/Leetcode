class Solution:
    def maximumSubarraySum(self, arr: List[int], k: int) -> int:
        max_sum=0
        s=0
        count={}
        start=0

        for end in range(len(arr)):
            rc=arr[end]
            s+=rc


            count[rc]=count.get(rc,0)+1

            while count[rc]>1:
                lc=arr[start]
                count[lc]-=1
                s-=lc
                start+=1
            if end-start+1==k:
                max_sum=max(max_sum,s)
                s-=arr[start]
                count[arr[start]]-=1
                start+=1
        return max_sum
        

    