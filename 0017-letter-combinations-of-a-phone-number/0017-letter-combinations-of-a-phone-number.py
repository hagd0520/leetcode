class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        answer = []
        letters_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def concat(letter: str, last_digits: List[str]):
            if not last_digits and answer:
                answer.append(letter)
                return
                
            for i in letters_dict[last_digits[0]]:
                next_letter = letter + i
                concat(next_letter, last_digits[1:])
        
        
        digits_list = list(digits)
        
        concat("", digits_list)
        
        return answer
