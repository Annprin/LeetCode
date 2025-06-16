class RecentCounter(object):

    def __init__(self):
        self.times = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.times.append(t)
        while self.times[0] + 3000 < t:
            self.times.popleft()
        return len(self.times)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)