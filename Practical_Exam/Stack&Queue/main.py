
from collections import deque

# Create Queue and Stack
orders = deque()
cancelled = []

# Add orders
orders.append("O101")
orders.append("O102")
orders.append("O103")

print("Active orders:", list(orders))

# Process first order (FIFO)
processed = orders.popleft()
print("Processed order:", processed)

# Cancel remaining orders
cancelled.append(orders.popleft())
cancelled.append(orders.popleft())

print("Cancelled orders:", cancelled)

# Restore latest cancelled order (LIFO)
restored = cancelled.pop()
orders.append(restored)

print("Restored order:", restored)
print("Current active orders:", list(orders))
print("Current cancelled stack:", cancelled)
