class Solution:
    def trap(self, height: List[int]) -> int:
        def get_filled_height(h: List[int]) -> List[int]:
            h_dict = defaultdict(list)
            hs = h[:]
            
            for i, j in enumerate(h):
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
                        hs[i] = _h
                
                prev_left = left
                prev_right = right
            
            return hs
                
        filled_height = get_filled_height(height)
                
        filled_count = 0
        
        for i in range(len(height)):
            filled_count += filled_height[i] - height[i]
            
        return filled_count