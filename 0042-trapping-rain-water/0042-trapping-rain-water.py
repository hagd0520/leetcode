class Solution:
    def trap(self, height: List[int]) -> int:
        def calculate(arr):
            res = 0
            hmax = 0
            for h in arr:
                if h < hmax:
                    res += hmax - h
                else:
                    hmax = h
            return res
        
        i = height.index(max(height))
        return calculate(height[:i]) + calculate(height[i+1:][::-1])