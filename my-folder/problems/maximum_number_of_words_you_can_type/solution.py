class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s=text.split(' ')
        count=0
        for x in s:
            for y in brokenLetters:
                if y in x:
             
                    count+=1
                    break
                    
        return len(s)-count
           
        
 