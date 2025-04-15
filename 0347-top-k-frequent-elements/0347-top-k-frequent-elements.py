class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        keys = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        
        return [i[0] for i in keys[:k]]