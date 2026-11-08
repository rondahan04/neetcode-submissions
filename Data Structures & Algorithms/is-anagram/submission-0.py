class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_set = {}
        for char in s:
            if char not in freq_set:
                freq_set[char] = 1
            else:
                freq_set[char] += 1
        for char in t:
            if char not in freq_set:
                return False
            freq_set[char] -= 1
            if freq_set[char] < 0:
                return False
        
        return True