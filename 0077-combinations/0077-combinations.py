class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        candidate = []

        nums = list(range(1, n + 1))

        def dfs(index=0):
            if len(candidate) < k:
                for i in range(index, len(nums) - (k - len(candidate) - 1)):
                    candidate.append(nums[i])
                    dfs(i + 1)
            else:
                if len(candidate) >= k:
                    answer.append(candidate[:])

            if candidate:
                candidate.pop()

        dfs()

        return answer