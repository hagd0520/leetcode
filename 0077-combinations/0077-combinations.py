class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        candidate = []

        def dfs(k, index=1):
            if k == 0:
                answer.append(candidate[:])
                return

            for i in range(index, n + 1):
                if n - (i - 1) >= k:
                    candidate.append(i)
                    dfs(k - 1, i + 1)
                    candidate.pop()

        dfs(k)

        return answer
