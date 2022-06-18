class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        arr.sort()
        min_diff=math.inf
        min_diff_sum=0
        for i,a in enumerate(arr):
            if arr[i]==arr[i-1] and i>0:
                continue
            left=i+1
            right=len(arr)-1
            while left<right:
                threesum=a+arr[right]+arr[left]
                diff=abs(targetsum-threesum)
                if diff<min_diff:
                    min_diff=diff
                    min_diff_sum=threesum
                    
            if threesum<targetsum:
                left+=1
            elif threesum>targetsum:
                right-=1
            else:
                left+=1
                while left<right and arr[left]==arr[left-1]:
                    left+=1
                

        
        return min_diff_sum
        '''
        nums.sort()
        min_diff = 10001
        min_diff_sum=0

        for i in range(len(nums)-2):

            if i>0 and nums[i]==nums[i-1]:
                continue

            l=i+1
            r=len(nums)-1

            while l<r:

                three_sum = nums[i]+nums[l]+nums[r]
                diff = abs(target-three_sum)

                if diff<min_diff:
                    min_diff = diff
                    min_diff_sum = three_sum

                if three_sum<target:
                    l+=1
                elif three_sum>target:
                    r-=1
                else:
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1


        return min_diff_sum

    