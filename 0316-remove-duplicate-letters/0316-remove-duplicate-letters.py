class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        # 스택 
        last = {c : i for i, c in enumerate(s)}
        seen, stack = set(), []
        
        for index, char in enumerate(s):
            if char in seen:
                continue
            
            while stack and char < stack[-1] and last[stack[-1]] > index:
                seen.remove(stack.pop())
                
            stack.append(char)
            seen.add(char)
            
        return ''.join(stack)
        
        # 재귀
        
        # for i in sorted(set(s)):
        #     suffix = s[s.index(i):]
            
        #     if set(suffix) == set(s):
        #         return i + self.removeDuplicateLetters(suffix.replace(i, ""))
            
        # return ""