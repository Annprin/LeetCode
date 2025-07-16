class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}
        for i, c in enumerate(s):
            pos[c] = i
        l, r = 0, 0
        res = []
        for i, c in enumerate(s):
            r = max(r, pos[c])
            if i == r:
                res.append(r - l + 1)
                l = i + 1
        return res