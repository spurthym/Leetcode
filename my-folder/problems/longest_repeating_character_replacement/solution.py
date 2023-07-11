class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        d={}
        max_len=0
        start=0
        max_repeat_letter_count=0
        for end in range(len(s)):
            rc=s[end]

            if rc not in d:
                d[rc]=0
            d[rc]+=1
            if d[rc]>max_repeat_letter_count:
                max_repeat_letter_count=d[rc]
            if end-start+1-max_repeat_letter_count > k :
                d[s[start]]-=1
                start+=1
            if end-start+1>max_len:
                max_len=end-start+1
        return max_len
            


        