class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = s.lower()
        res = re.sub(r'[^a-zA-Z0-9]','',res)

        start = 0
        end = len(res) - 1
        ans = True
        while start < end:
            if (res[start] != res[end]):
                ans = False
                break
            start += 1
            end -= 1
        return ans