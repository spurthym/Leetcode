class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        res=""
        for each in l[::-1]:
            res+=each+" "
        return res[:-1]
        
        