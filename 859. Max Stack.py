import heapq

class MaxStack:

    def __init__(self):
        self.heap = []
        self.stack = []
        self.popped_set = set()
        self.count = 0
        
    def push(self, x):
        item = (-x, -self.count)
        self.stack.append(item)
        heapq.heappush(self.heap, item)
        self.count += 1
        
    def _clear_popped_in_stack(self):
        while self.stack and self.stack[-1] in self.popped_set:
            self.popped_set.remove(self.stack[-1])
            self.stack.pop()
    
    def _clear_popped_in_heap(self):
        while self.heap and self.heap[0] in self.popped_set:
            self.popped_set.remove(self.heap[0])
            heapq.heappop(self.heap)

    def pop(self):
        self._clear_popped_in_stack()
        item = self.stack.pop()
        self.popped_set.add(item)
        return -item[0]

    def top(self):
        self._clear_popped_in_stack()
        item = self.stack[-1]
        return -item[0]

    def peekMax(self):
        self._clear_popped_in_heap()
        item = self.heap[0]
        return -item[0]

    def popMax(self):
        self._clear_popped_in_heap()
        item = heapq.heappop(self.heap)
        self.popped_set.add(item)
        return -item[0]