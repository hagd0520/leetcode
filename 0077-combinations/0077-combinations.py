class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        candidate = []

        def dfs(k, index=1):
            if k:
                for i in range(index, n + 1):
                    candidate.append(i)
                    dfs(k - 1, i + 1)
            else:
                if len(candidate) >= k:
                    answer.append(candidate[:])

            if candidate:
                candidate.pop()

        dfs(k)

        return answer