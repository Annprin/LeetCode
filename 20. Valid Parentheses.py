class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sc = {'(':')', '{':'}', '[':']'}
        st = []

        for c in s:
            if c in sc:
                st.append(c)
            elif st and sc[st[-1]] == c:
                st.pop()
            else:
                return False
        return not st  