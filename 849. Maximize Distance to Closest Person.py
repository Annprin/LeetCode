class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_free, free, start = 0, 0, 0
        for i, seat in enumerate(seats):
            if seat == 0:
                free += 1
            else:
                if (start == 0 and free > max_free):
                    max_free = free
                elif (free + 1) // 2 > max_free:
                    max_free = (free + 1) // 2
                free = 0
                start = i + 1
        if free > max_free:
            max_free = free
        return max_free