class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        count_s1, count_s2 = [0] * 26, [0] * 26
        for i, c in enumerate(s1):
            count_s1[ord(c) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s2) - len(s1)):
            if count_s1 == count_s2:
                return True
            count_s2[ord(s2[i]) - ord('a')] -= 1
            count_s2[ord(s2[i + len(s1)]) - ord('a')] += 1
        return count_s1 == count_s2