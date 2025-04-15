class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set(s)
        seen = set()
        _deque = deque()
        answer = 0
        
        for i in s:
            while i in seen:
                seen.remove(_deque.popleft())
            seen.add(i)
            _deque.append(i)
            answer = max(answer, len(_deque))
            
        return answer