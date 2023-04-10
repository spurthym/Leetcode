class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:

        res=""
        for each in words:
            res=res+each
            if res ==s:
                return True
        return False