class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = sorted(nums)
        
        for i in range(len(temp))[::-1]:
            for j in range(i):
                result = temp[i] + temp[j]
                
                if result == target:
                    left = nums.index(temp[j])
                    right = nums.index(temp[i])
                    
                    if left == right:
                        right = nums.index(temp[i], left + 1)
                    
                    return [left, right]