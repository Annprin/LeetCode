class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        def expand(i, j):
            left, right = i, j
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                
            return right - left - 1

        ans = [0, 0]
        for i in range(n):
            odd = expand(i, i)
            if odd > ans[1] - ans[0] + 1:
                dist = odd // 2
                ans = [i - dist, i + dist]
            
            even = expand(i, i + 1)
            if even > ans[1] - ans[0] + 1:
                dist = even // 2 - 1
                ans = [i - dist, i + dist + 1]
            
        i, j = ans
        return s[i : j + 1]