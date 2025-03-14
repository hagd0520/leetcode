class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        all_mul = 1
        zeros = []
        
        for i, value in enumerate(nums):
            answer.append(0)
            
            if value == 0:
                zeros.append(i)
            else:
                all_mul *= value
                
        if len(zeros) == 1:
            answer[zeros[0]] = all_mul
            
        if not zeros:
            for i, value in enumerate(nums):
                answer[i] = all_mul // value
            
        return answer