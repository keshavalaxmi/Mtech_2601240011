
import time

from src.anomaly_detector import detect_anomalies


def main():
    traffic = [40, 42, 41, 43, 45, 200] * 1000

    start_time = time.perf_counter()
    results = detect_anomalies(traffic)
    elapsed = time.perf_counter() - start_time

    anomalies = sum(result["anomaly"] for result in results)

    print("=== Performance Benchmark ===")
    print(f"Traffic samples: {len(traffic)}")
    print(f"Anomalies detected: {anomalies}")
    print(f"Execution time: {elapsed:.6f} seconds")
    print(f"Throughput: {len(traffic) / elapsed:.2f} samples/second")


if __name__ == "__main__":
    main()
