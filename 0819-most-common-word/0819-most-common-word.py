class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count_dict = dict()
        paragraph = re.sub("[^a-z]", " ", paragraph.lower())
        for word in paragraph.split():
            count_dict[word] = count_dict.get(word, 0) + 1
            
        sorted_list = sorted(count_dict.items(), key=lambda x: (x[1]), reverse=True)
        
        banned_set = set(banned)
        
        for i in sorted_list:
            if i[0] not in banned_set:
                return i[0]