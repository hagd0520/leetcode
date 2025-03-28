class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        # 스택 
        
        counter, seen, stack = Counter(s), set(), []
        
        for char in s:
            print(seen)
            counter[char] -= 1
            if char in seen:
                continue
            
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
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