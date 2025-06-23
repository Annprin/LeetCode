class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        p_count = [0] * 26
        s_count = [0] * 26

        for char in p:
            p_count[ord(char) - ord('a')] += 1
        
        ans = []
        for i, char in enumerate(s):
            s_count[ord(char) - ord('a')] += 1

            if i >= len(p):
                s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            
            if s_count == p_count:
                ans.append(i - len(p) + 1)

        return ans