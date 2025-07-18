# Design a hit counter which counts the number of hits received in the past 5 minutes.

# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being 
# made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that 
# the earliest timestamp starts at 1.

# It is possible that several hits arrive roughly at the same time.
from collections import deque

class HitCounter:
    def __init__(self):
        self.times = deque()
    
    def hit(self, time):
        self.times.append(time)
    
    def getHits(self, time):
        while self.times and time - self.times[0] >= 300:
            self.times.popleft()
        return len(self.times)