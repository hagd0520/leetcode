class Solution:
    def trap(self, height: List[int]) -> int:
        max_h = height.index(max(height))
        
        left = height[:max_h + 1]
        right = height[max_h:][::-1]
        
        def cal(arr: List[int]):
            volume = 0
            max_h = 0
            for i in arr:
                if i <= max_h:
                    volume += max_h - i
                else:
                    max_h = i
            return volume
        
        return cal(left) + cal(right)