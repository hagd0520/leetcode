class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = defaultdict(list)
        for i,  word in enumerate(strs):
            _dict[str(sorted(word))].append(i)
        
        answer = []
        for i in _dict.values():
            _list = []
            for j in i:
                _list.append(strs[j])
            answer.append(_list)
            
        return answer