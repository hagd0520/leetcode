class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        
        for i, v in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < v:
                index = stack.pop()
                temperatures[index] = i - index
                
            stack.append(i)
            
        for i in stack:
            temperatures[i] = 0
                
        return temperatures