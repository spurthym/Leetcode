class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        
        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                substr=""
                while stack[-1]!="[":
                    substr=stack.pop()+substr
                stack.pop()
                k=""
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k
                stack.append(int(k)*substr)
                
        return "".join(stack)
                
            
        """
        list_s=list(s)
        start=0
        f=""
        def helper(start,list_s,f):
            leng=len(list_s)
            
            
            
            if start==leng:
                print("im here")
                return f
            if list_s[start]=="[":
                return helper(start+1,list_s,f)
            if list_s[start].isdigit:
                m_s=""
                n=int(list_s[start])
                start=start+2
                while list_s[start]!="]":
                    m_s+=list_s[start]
                    start=start+1
                f+=m_s*n
                print(f)
                return helper(start+1,list_s,f)
        f=helper(start,list_s,f)
        return f"""