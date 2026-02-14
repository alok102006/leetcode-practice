class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        for word in words:
            lower_word = word.lower()
    
    
            if lower_word[0] in row1:
                row = row1
            elif lower_word[0] in row2:
                row = row2
            else:
                row = row3
    
            valid = True
    
    
            for char in lower_word:
                if char not in row:
                    valid = False
                    break
    
            if valid:
                result.append(word)     
        return result