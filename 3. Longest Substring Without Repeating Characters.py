class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        maxLength = 0
        left = 0

        for c in s:
            if c not in charSet:
                charSet.add(c)
            else:
                maxLength = max(len(charSet), maxLength)
                while s[left] != c:
                    charSet.remove(s[left])
                    left += 1
                left += 1

        maxLength = max(len(charSet), maxLength)
        return maxLength