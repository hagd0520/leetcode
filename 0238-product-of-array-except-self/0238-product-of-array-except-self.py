class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        accum = 1
        
        for i in range(len(nums)):
            answer.append(accum)
            accum *= nums[i]
        
        accum = 1
        
        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * accum
            accum *= nums[i]
            
        return answer