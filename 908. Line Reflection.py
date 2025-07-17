# время - О(n), память - О(n)

from typing import (
    List,
)

class Solution:
    """
    @param points: n points on a 2D plane
    @return: if there is such a line parallel to y-axis that reflect the given points
    """
    def is_reflected(self, points: List[List[int]]) -> bool:
        # Write your code here
        if not points:
            return True
        s = max(points, key = lambda x: x[0])[0] + min(points, key = lambda x:x[0])[0]
        
        mid = s / 2
        r, l = set(), set()
        for x, y in points:
            if x < mid:
                l.add((s - x, y))
            elif x > mid:
                r.add((x, y))
        return r == l