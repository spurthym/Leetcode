class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s=set()
        

        for each in emails:
            cleaned=""
            i=0
            while i<=len(each):

                if each[i]==".":
                    i+=1
                    continue
                elif each[i]=="+":
                    while each[i]!="@":
                        i+=1
                    
                    continue
                elif(each[i]=="@"):
                    cleaned+=each[i:]
                    break
                else:
                    


                
                    cleaned+=each[i]
                    i+=1
                

            s.add(cleaned)
            

                
        return len(s)

