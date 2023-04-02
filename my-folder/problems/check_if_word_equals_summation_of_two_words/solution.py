class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        def ret(s):
            val=0
            for c in s:
                val=val*10+(ord(c)-97)
            return val
        
        return (ret(firstWord)+ret(secondWord)==ret(targetWord))