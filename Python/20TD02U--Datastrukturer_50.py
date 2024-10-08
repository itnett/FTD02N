python
import heapq

# Min-heap
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush

(min_heap, 2)
print(heapq.heappop(min_heap))  # Output: 1

# Max-heap (bruk av negative tall)
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -2)
print(-heapq.heappop(max_heap))  # Output: 3