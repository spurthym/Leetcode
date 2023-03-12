class Solution:
    def letterCombinations(self, digits: str) -> List[str]:


        d2c={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res=[]


        def btrk(i,curstr):
            if len(digits)==len(curstr):
                res.append(curstr)
                return
            for c in d2c[digits[i]]:
                btrk(i+1,curstr+c)
        if digits:
            btrk(0,"")
        return res