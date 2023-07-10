class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start=0
        num_fruits=0
        max_f=0
        d={}


        for end in range(len(fruits)):
            rc=fruits[end]
            if rc not in d:
                d[rc]=0
            d[rc]+=1
            
            
            print(d)
            while len(d)>2:
                d[fruits[start]]-=1
                if d[fruits[start]]==0:
                    del d[fruits[start]]
                start+=1
            if end-start+1>max_f:
                max_f=end-start+1
        return max_f
        