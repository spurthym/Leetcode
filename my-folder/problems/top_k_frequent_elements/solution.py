class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for each in range(len(nums)):
            if nums[each] not in d:
                d[nums[each]]=0
            d[nums[each]]+=1
        res=[]

        l=sorted(d.values(),reverse=True)
        for i in range(k):
            for key,v in d.items():
                if l[i]==v:
                    res.append(key)
                    d[key] = -1
        return res
