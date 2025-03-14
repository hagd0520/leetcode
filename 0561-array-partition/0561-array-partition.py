class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
        
        # nums.sort()
        # answer = 0
        
        # for i, num in enumerate(nums):
        #     if i % 2 == 0:
        #         answer += num
        
        # return answer