class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        u={}
        max_l=0
        start=0
        for end in range(len(s)):
            rc=s[end]
            if rc in u:
                start=max(start,u[rc]+1)
            u[rc]=end
            max_l=max(max_l,end-start+1)
        return max_l