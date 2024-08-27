python
from collections import deque

kø = deque()

# Legge til elementer i køen
kø.append("første")
kø.append("andre")
kø.append("tredje")

# Fjerne elementer fra køen
print(kø.popleft())  # Utskrift: første
print(kø.popleft())  # Utskrift: andre