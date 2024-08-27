python
import heapq

kø = []
heapq.heappush(kø, (1, "lav prioritet"))
heapq.heappush(kø, (5, "høy prioritet"))
heapq.heappush(kø, (3, "middels prioritet"))

print(heapq.heappop(kø))  # Utdata: (1, "lav prioritet")