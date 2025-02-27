class Solution:
    def trap(self, height: List[int]) -> int:
        filled_count = 0
        
        h_dict = defaultdict(list)
        hs = height[:]
        
        for i, j in enumerate(height):
            h_dict[j].append(i)
            
        h_list = sorted(h_dict.items(), key=lambda item:item[0], reverse=True)
                        
        prev_left = 10**5
        prev_right = 0
        
        for _h, indexes in h_list:
            
            left = indexes[0]
            right = indexes[-1]
                            
            if left > prev_left:
                left = prev_left
                
            if right < prev_right:
                right = prev_right
            
            for i in range(left, right):
                if hs[i] < _h:
                    filled_count += _h - hs[i]
                    hs[i] = _h
                    
            
            prev_left = left
            prev_right = right
        
        return filled_count