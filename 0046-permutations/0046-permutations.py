class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(nums: List[int], candidate: List[int] = []):
            for i, num in enumerate(nums):
                temp_nums = nums[:]
                temp_candidate = candidate[:]
                temp_candidate.append(temp_nums.pop(i))

                if not temp_nums:
                    answer.append(temp_candidate)
                    break

                dfs(temp_nums, temp_candidate)

        dfs(nums)

        return answer