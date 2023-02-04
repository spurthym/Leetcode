class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        if target<letters[0] or target >=letters[-1] :
            return letters[0]
        
        l=0
        h=len(letters)-1

        while l<=h:
            mid=l+(h-l)//2

            if target>=letters[mid]:
                l=mid+1
            else:
                h=mid-1
        return letters[l]        