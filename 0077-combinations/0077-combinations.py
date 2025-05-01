class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        # candidate = []

        # def dfs(k, index=1):
        #     if k == 0:
        #         answer.append(candidate[:])
        #         return

        #     for i in range(index, n + 1):
        #         if n - (i - 1) >= k:
        #             candidate.append(i)
        #             dfs(k - 1, i + 1)
        #             candidate.pop()

        # dfs(k)

        # return answer

        pool = tuple(range(1, n + 1))
        n = len(pool)
        if k > n:
            return []
        indices = list(range(k))
        answer.append(tuple(pool[i] for i in indices))
        while True:
            for i in reversed(range(k)):
                if indices[i]!= i + n - k:
                    break
            else:
                break
            indices[i] += 1
            for j in range(i + 1, k):
                indices[j] = indices[j - 1] + 1
            answer.append(tuple(pool[i] for i in indices))

        return answer
