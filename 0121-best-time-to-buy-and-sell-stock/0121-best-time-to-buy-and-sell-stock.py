class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        min = 10000
        
        for i in prices:
            if i < min:
                min = i
            
            if i - min > answer:
                answer = i - min
                
        return answer