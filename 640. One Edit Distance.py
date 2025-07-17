class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def is_one_edit_distance(self, s: str, t: str) -> bool:
        # write your code here
        m, n = len(s), len(t)
        if m > n:
            return self.is_one_edit_distance(t, s)
        
        if n - m > 1:
            return False
        
        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    return s[i + 1:] == t[i + 1:]
                return s[i:] == t[i + 1:]
        return m != n
            