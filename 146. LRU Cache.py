class LRUCache(object):

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.prev = self.tail
        self.tail.next = self.head
        self.map_nodes = {}

    def delNode(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def addNode(self, node):
        tmp = self.head.prev
        self.head.prev = node
        node.next = self.head
        node.prev = tmp
        tmp.next = node
        return node


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = None
        if key in self.map_nodes:
            node = self.map_nodes[key]
            self.delNode(node)
            self.addNode(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map_nodes:
            node = self.map_nodes[key]
            node.value = value
            self.map_nodes[key] = node
            self.delNode(node)
            self.addNode(node)
        else:
            if self.capacity == len(self.map_nodes):
                oldKey = self.tail.next.key
                self.delNode(self.tail.next)
                del self.map_nodes[oldKey]
            node = self.addNode(self.Node(key, value))
            self.map_nodes[key] = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)