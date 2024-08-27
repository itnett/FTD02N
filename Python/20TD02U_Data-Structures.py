python
import time

class Node:
    def __init__(self, key, value, expire_time):
        self.key = key
        self.value = value
        self.expire_time = expire_time
        self.prev = None
        self.next = None

class ExpiringCache:
    def __init__(self, ttl):
        self.ttl = ttl
        self.cache = {}
        self.head = None
        self.tail = None
    
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            if time.time() < node.expire_time:
                self._move_to_head(node)
                return node.value
            else:
                self._remove(node)
        return None
    
    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            node.expire_time = time.time() + self.ttl
            self._move_to_head(node)
        else:
            new_node = Node(key, value, time.time() + self.ttl)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            if len(self.cache) > self.capacity:
                self._remove_tail()
    
    def _move_to_head(self, node):
        if node is self.head:
            return
        self._remove(node)
        self._add_to_head(node)
    
    def _add_to_head(self, node):
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node
    
    def _remove(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev
        del self.cache[node.key]
    
    def _remove_tail(self):
        if self.tail:
            self._remove(self.tail)

# Example usage
cache = ExpiringCache(ttl=5)
cache.set("key1", "value1")
print(cache.get("key1"))  # Output: "value1"
time.sleep(6)
print(cache.get("key1"))  # Output: None (expired)