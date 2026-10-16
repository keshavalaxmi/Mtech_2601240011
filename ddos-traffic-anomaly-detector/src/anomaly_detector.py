
from src.statistics_engine import StreamingStatistics


def detect_anomalies(
    traffic: list[int],
    window_size: int = 5,
    threshold: float = 2.0,
) -> list[dict]:
    """Detect unusually high traffic using a sliding window."""

    statistics = StreamingStatistics(window_size)
    results = []

    for timestamp, packet_count in enumerate(traffic, start=1):
        # Compare against the previous window, not the current sample.
        previous_window = list(statistics.window)

        if len(previous_window) == window_size:
            baseline = sum(previous_window) / window_size
        elif previous_window:
            baseline = sum(previous_window) / len(previous_window)
        else:
            baseline = 0

        is_anomaly = (
            len(previous_window) > 0
            and packet_count > baseline * threshold
        )

        stats = statistics.update(packet_count)

        results.append(
            {
                "timestamp": timestamp,
                "packets": packet_count,
                "baseline": round(baseline, 2),
                "anomaly": is_anomaly,
                "window_average": stats["window_average"],
            }
        )

    return results
