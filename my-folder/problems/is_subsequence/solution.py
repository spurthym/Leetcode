class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        ptr1=0
        ptr2=0


        while ptr2<len(t) and (ptr1)<len(s):
            if s[ptr1]==t[ptr2]:
                ptr1+=1
            ptr2+=1
        if ptr1==len(s):
            return True
        return False
                
                