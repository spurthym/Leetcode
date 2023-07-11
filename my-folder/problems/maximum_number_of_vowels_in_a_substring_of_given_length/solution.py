class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        max_count=0
        count=0
        start=0

        for end in range(len(s)):
            rc=s[end]
            if end>k-1:
                if s[start] in "aeiou":
                    count-=1
                start+=1
            if rc in "aeiou":
                count+=1
            if count>max_count:
                max_count=count
            
        return max_count