class Solution(object):
    def threeSum(self, nums):
        """
        Find all unique triplets in the array whose sum equals zero.

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            a = i + 1
            b = len(nums) - 1

            while a < b:
                s = nums[i] + nums[a] + nums[b]

                if s < 0:
                    a += 1
                elif s > 0:
                    b -= 1
                else:
                    res.append([nums[i], nums[a], nums[b]])

                    # Skip duplicates for the second and third elements
                    while a < b and nums[a] == nums[a + 1]:
                        a += 1
                    while a < b and nums[b] == nums[b - 1]:
                        b -= 1

                    # Move both pointers to explore other potential triplets
                    a += 1
                    b -= 1

        return res
