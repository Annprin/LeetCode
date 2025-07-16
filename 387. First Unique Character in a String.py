class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = [0] * 26

        for char in s:
            frequency[ord(char) - ord('a')] += 1
        
        for i, char in enumerate(s):
            if frequency[ord(char) - ord('a')] == 1:
                return i

        return -1