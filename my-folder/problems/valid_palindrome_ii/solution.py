class Solution:
    def validPalindrome(self, s: str) -> bool:
        print(len(s))
        ptr1=0
        ptr2=len(s)-1
        used=False
        count=0

        while ptr1<ptr2:
            count+=1

            if s[ptr1]==s[ptr2]:
                ptr1+=1
                ptr2-=1
       
            else:
                
                if s[ptr1+1:ptr2+1] == s[ptr1+1:ptr2+1][::-1]:
                    return True
                elif s[ptr1:ptr2] == s[ptr1:ptr2][::-1]:
                    return True
                else:
                    return False
            
        return True


            
            
