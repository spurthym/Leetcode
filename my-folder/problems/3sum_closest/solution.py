class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        s=0
        finalans=0
        diff = math.inf

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1

            while j<k:

                s=nums[i]+nums[j]+nums[k]
                if abs(target-s) <diff:
                    diff=abs(target-s)
                    finalans=s
                if s<target:
                    j+=1
                elif s>target:
                    k-=1
                else:
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                

        return finalans
