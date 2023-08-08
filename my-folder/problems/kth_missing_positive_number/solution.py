class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:

        n = len(nums)
    
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:
                i += 1

        missingNumbers = []
        extraNumbers = set()

        for i in range(n):
            if len(missingNumbers) < k:
                if nums[i] != i + 1:
                    missingNumbers.append(i + 1)
                extraNumbers.add(nums[i])

        # add the remaining missing numbers
        i = 1
        while len(missingNumbers) < k:
            candidateNumber = i + n
            # ignore if the array contains the candidate number
            if candidateNumber not in extraNumbers:
                missingNumbers.append(candidateNumber)
            i += 1

        return missingNumbers[-1]