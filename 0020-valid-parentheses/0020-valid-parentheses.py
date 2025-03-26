class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        for i in s:
            if i in brackets.keys():
                stack.append(i)
            else:
                if not stack or brackets.get(stack.pop()) != i:
                    return False
                
        if stack:
            return False
        
        return True