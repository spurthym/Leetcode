class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        start=0
        max_len=0
        for end in range(len(s)):
            rc=s[end]

            if rc not in d:
                d[rc]=0
            d[rc]+=1
            while d[rc]>1:
                d[s[start]]-=1
                if d[s[start]]==0:
                    del d[s[start]]
                start+=1
            if end-start+1>max_len:
                    max_len=end-start+1
        return max_len

            


