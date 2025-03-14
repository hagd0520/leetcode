class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        return nums[len(nums) - 4] + nums[len(nums) - 2]