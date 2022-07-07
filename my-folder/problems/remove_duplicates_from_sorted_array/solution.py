class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
          ptr2 = 1

          ptr1 = 0
          while(ptr1 < len(arr)):
            if arr[ptr2 - 1] != arr[ptr1]:
              arr[ptr2] = arr[ptr1]
              ptr2 += 1
            ptr1 += 1

          return ptr2
