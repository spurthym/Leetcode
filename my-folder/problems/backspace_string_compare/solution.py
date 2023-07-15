class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def build(s1):
            res=[]

            for c in s1:
                if c!="#":
                    res.append(c)
                elif res:
                    res.pop()
                print(c)
            return res
       

        return build(s)==build(t)
