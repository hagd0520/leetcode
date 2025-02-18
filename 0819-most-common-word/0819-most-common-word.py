class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count_dict = dict()
        for word in paragraph.split():
            _word = re.sub("[^a-z]", "", word.lower())
            count_dict[_word] = count_dict.get(_word, 0) + 1
            
        sorted_list = sorted(count_dict.items(), key=lambda x: (x[1]), reverse=True)
        
        banned_set = set(banned)
        
        for i in sorted_list:
            if i[0] not in banned_set:
                return i[0]