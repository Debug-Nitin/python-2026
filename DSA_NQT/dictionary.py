class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        idx_map = {}

        for i in range(len(word)):
            ch = word[i]
            if ch.isupper() :
                if ch not in idx_map:
                    idx_map[ch] = i
            else :
                idx_map[ch] = i
        
        count = 0

        for i in range(97,123):
            value = chr(i)
            if value in idx_map and value.upper() in idx_map:
                if idx_map[value] < idx_map[value.upper()]:
                    count +=1
        
        return count
                