class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count={0:-1}
        maxlen=0
        curr_count=0

        for i in range(len(nums)):
            if nums[i]==0:
                curr_count-=1
            else:
                curr_count+=1
            

            if curr_count in count:
                maxlen=max(maxlen,i-count[curr_count])
            else:
                count[curr_count]=i
              

            
        return maxlen
