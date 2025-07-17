# time - O(max(n, m)), space - O(n + m)

class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        # do intialization if necessary
        self.queue = [v for v in (v1, v2) if v]
    """
    @return: An integer
    """
    def _next(self):
        # write your code here
        v = self.queue.pop(0)
        value = v.pop(0)
        if v:
            self.queue.append(v)
        return value

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return len(self.queue) > 0


# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result