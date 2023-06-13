from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = []
        
        for i in range(len(nums)):
            # Remove elements outside the current window from the front of the window
            if window and window[0] <= i - k:
                window.pop(0)
            
            # Remove elements smaller than the current number from the end of the window
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            # Add the current number to the window
            window.append(i)
            
            # Add the maximum element in the current window to the result
            if i >= k - 1:
                res.append(nums[window[0]])
        
        return res
