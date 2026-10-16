
from collections import deque


class StreamingStatistics:
    """Maintain traffic statistics using an efficient sliding window."""

    def __init__(self, window_size: int = 5):
        if window_size <= 0:
            raise ValueError("window_size must be greater than zero")

        self.window: deque[int] = deque(maxlen=window_size)
        self.window_size = window_size
        self.window_total = 0
        self.total_packets = 0
        self.total_samples = 0

    def update(self, packet_count: int) -> dict:
        """Update statistics in constant time per sample."""

        if len(self.window) == self.window_size:
            self.window_total -= self.window[0]

        self.window.append(packet_count)
        self.window_total += packet_count

        self.total_packets += packet_count
        self.total_samples += 1

        window_average = self.window_total / len(self.window)

        return {
            "current": packet_count,
            "window_average": round(window_average, 2),
            "window_total": self.window_total,
            "samples_seen": self.total_samples,
        }
