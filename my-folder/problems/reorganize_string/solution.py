class Solution:
    def reorganizeString(self, s: str) -> str:

        res=""
        d=Counter(s)
        max_count=max(d.values())
        print(max_count)
        print(((len(s)-max_count)+1))

        if max_count>((len(s)-max_count)+1):
            return ""
        h=[(-1*value,key) for key,value in d.items()]
        heapq.heapify(h)
        prev_value,prev_char=0,""
        while h:
            curr_value,curr_char=heappop(h)
            res+=curr_char
            curr_value+=1
            if prev_value<0:
                heapq.heappush(h,(prev_value,prev_char))
            prev_value,prev_char=curr_value,curr_char
        return res
            


