class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        h=len(s)-1
        s=list(s)
        vowels=list("aeiouAEIOU")
        while l<h:
            while l<h and s[l] not in vowels:
                l=l+1
            while h>l and s[h] not in vowels:
                h=h-1
            s[h],s[l]=s[l],s[h]
            l=l+1
            h-=1
            
            
        return "".join(s)
        '''


        n = len(s)
        l, r = 0, n - 1
        s = list(s)
        vowels = list("aeiouAEIOU")
        # `l` is the left pointer to track the vowel character
        # `r` is the right pointer to track the vowel character
        while l < r:
            # find the index of the first vowel in the given range
            while l < r and s[l] not in vowels:
                l += 1
            # find the index of last vowel in the given range
            while r > l and s[r] not in vowels:
                r -= 1
            # swap s[l] and s[r]
            print(s[l],s[r])
            s[l], s[r] = s[r], s[l]
            # since we've processed the character s[l],
            # we move the left pointer to the right
            l += 1
            # since we've processed the character s[r],
            # we move the right pointer to the left
            r -= 1
            
        return "".join(s)'''
                