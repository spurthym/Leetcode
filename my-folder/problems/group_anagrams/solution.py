class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[]
        d=defaultdict(list)
        for each in strs:
            key="".join(sorted(each))
            d[key].append(each)

        return (list(d.values()))

