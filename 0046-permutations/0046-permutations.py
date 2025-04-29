class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return list(itertools.permutations(nums))

        answer = []
        temp_candidate = []

        def dfs(nums: List[int]):
            for i in range(len(nums)):
                temp_nums = nums[:]
                temp_candidate.append(temp_nums.pop(i))

                if not temp_nums:
                    answer.append(temp_candidate[:])

                dfs(temp_nums)
                temp_candidate.pop()

        dfs(nums)

        return answer