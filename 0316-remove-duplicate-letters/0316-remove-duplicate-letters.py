class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c : i for i, c in enumerate(s)}
        stack = []
        seen = set()

        for index, c in enumerate(s):
            if c in seen:
                continue

            while stack and index < last[stack[-1]] and c < stack[-1]:
                a = stack.pop()
                seen.remove(a)

            stack.append(c)
            seen.add(c)

        return "".join(stack)