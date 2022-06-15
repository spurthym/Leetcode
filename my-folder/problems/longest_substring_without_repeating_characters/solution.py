class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
      start=0
      freq={}
      max_length=0

      for end in range(len(s)):
        rc=s[end]
        if rc in freq:
          start=max(start,freq[rc]+1)


        freq[rc]=end
        max_length=max(max_length,end-start+1)

      return max_length