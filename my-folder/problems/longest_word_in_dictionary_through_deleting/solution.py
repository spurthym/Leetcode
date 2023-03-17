class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x:(-len(x),x))
        i=0
        for each in dictionary:
            i=0
            for c in s:
             
                if c==each[i]:
                    i+=1
                if i==len(each):
                    return each
        return ""
        