class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        w_s=0
        max_sum=-math.inf

        for each in nums:
            if w_s<0:
                w_s=0
            w_s+=each
            if w_s>max_sum:
                max_sum=w_s
        return max_sum