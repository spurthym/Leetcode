class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        
        resLen=0
        res=""
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1

                l-=1
                r+=1

            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1

                l-=1
                r+=1
        return res
    
        '''list=[]
        for i in range(len(s)):
            string=""
            for j in range(i,len(s)):
                string+=s[j]
                list.append(string)
        print(list)
        
        def palindrome(list):
            maxi_l=0
            retstr=""
            for i in range(len(list)):
                if list[i]==list[i][::-1] and len(list[i])>maxi_l:
                    maxi_l=len(list[i])
                    retstr=list[i]
            
            return retstr
        return palindrome(list)'''
        
        
            
            
            
        