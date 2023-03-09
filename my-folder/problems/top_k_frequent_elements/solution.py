class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]
        for n in nums:
            if n not in count:
                count[n]=0
            count[n]+=1
        print(count)
        print(freq)
        
        for key,val in count.items():
            freq[val].append(key)
        print(freq)
        res=[]

        for i in range(len(freq)-1,0,-1):
            print(i)
            for n in freq[i]:
                res.append(n)
                print("len",len(res))
                print("k",k)
                if len(res)==k:
                    return res
         