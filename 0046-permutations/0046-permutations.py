class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answer = []

        def dfs(indexes: List[int], permutation: List[int] = []):

            if not indexes:
                answer.append(permutation)
            
            for i in range(len(indexes)):
                new_indexes = indexes[:]
                new_permutation = permutation[:]
                
                new_permutation.append(nums[new_indexes.pop(i)])
                
                dfs(new_indexes, new_permutation)
                
        dfs(list(range(len(nums))))
        
        return answer