class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_chr = ["(", "{", "["]
        close_chr = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        for i in s:
            if i in open_chr:
                stack.append(i)
            else:
                if not stack or close_chr.get(stack.pop()) != i:
                    return False
                
        if stack:
            return False
        
        return True