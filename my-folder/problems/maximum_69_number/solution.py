class Solution:
    def maximum69Number (self, num: int) -> int:
        s=list(str(num))
        print(s)
        for i in range(len(s)):
            if s[i]=="6":
                s[i]="9"
                print(s)
                break
        return int("".join(s))
        
        