class Solution(object):
    def twoSum(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums=[]
        for i,v in enumerate(num):
            nums.append([v,i])

        nums=sorted(nums, key=lambda x: x[0])
        print(nums)

        ptr1=0
        ptr2=len(nums)-1

        while ptr1<ptr2:

            if nums[ptr1][0]+nums[ptr2][0]>target:
                ptr2-=1
            elif nums[ptr1][0]+nums[ptr2][0]<target:
                ptr1+=1
            else:
                return [nums[ptr1][1],nums[ptr2][1]]