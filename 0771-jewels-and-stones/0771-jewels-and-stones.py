class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        return len([i for i in stones if i in jewels_set])
                
        return answer