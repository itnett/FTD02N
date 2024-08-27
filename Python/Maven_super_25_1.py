python
from collections import deque

# Definer en enkel kø med deque
printer_queue = deque()

# Legge til dokumenter i køen
printer_queue.append("Dokument 1")
printer_queue.append("Dokument 2")
printer_queue.append("Dokument 3")

# Simulerer printing ved å fjerne elementer fra køen
while printer_queue:
    current_document = printer_queue.popleft()
    print(f"Printer: {current_document}")