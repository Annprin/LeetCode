class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp = 0
        ns, nt = len(s), len(t)
        while sp < ns and tp < nt:
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        return sp == len(s)