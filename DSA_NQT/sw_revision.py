from typing import List

def longestKSubstr( s, k):
    freq = {}
    left, right = 0,0
    res = -1
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right],0)+ 1
        
        while len(freq) > k :
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left +=1
                
        if len(freq) == k:
            res = max(res,right - left + 1)
            
    return res

def totalFruit(fruits: List[int]) -> int:
        freq = {}
        left, right = 0,0
        res = 0

        for right in range(len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right],0) + 1

            while len(freq) > 2:
                freq[fruits[left]] -=1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left +=1
            
            res = max(res,right - left + 1)
        
        return res