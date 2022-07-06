class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m_r_l_c=0
        freq={}
        start=0
        max_length=0
        for end in range(len(s)):
            rc=s[end]
            if rc not in freq:
                freq[rc]=0
            freq[rc]+=1
            m_r_l_c=max(m_r_l_c,freq[rc])
            if end-start+1-m_r_l_c>k:
                lc=s[start]
                freq[lc]-=1
                start=start+1
            max_length=max(max_length, end-start+1)
        return max_length