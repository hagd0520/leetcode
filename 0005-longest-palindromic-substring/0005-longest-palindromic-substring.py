class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s))[::-1]:
            for j in range(len(s) - i):
                target = s[j : j + i + 1]
                if target == target[::-1]:
                    return target