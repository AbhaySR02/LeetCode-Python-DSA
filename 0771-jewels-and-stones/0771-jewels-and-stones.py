class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res=0
        jewels_set=set(jewels)
        for ch in stones:
            if ch in jewels_set:
                res += 1
        return res

        
        