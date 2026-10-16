
import csv
from pathlib import Path

from src.anomaly_detector import detect_anomalies
from src.parallel_processor import analyze_in_parallel

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "traffic.csv"
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_FILE = OUTPUT_DIR / "detection_results.csv"


def main():
    print("MAIN FILE STARTED")

    if not INPUT_FILE.exists():
        print(f"ERROR: Traffic file not found: {INPUT_FILE}")
        return

    timestamps = []
    traffic = []

    with INPUT_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            timestamps.append(row["timestamp"])
            traffic.append(int(row["packets"]))

    print(f"Loaded {len(traffic)} traffic samples.")

    results = detect_anomalies(
        traffic,
        window_size=5,
        threshold=2.0,
    )

    for index, result in enumerate(results):
        result["timestamp"] = timestamps[index]

    print("\n=== DDoS Traffic Anomaly Detector ===")
    print("-" * 55)
    print(f"{'Time':<10}{'Packets':<12}{'Baseline':<14}{'Status'}")
    print("-" * 55)

    for result in results:
        status = "ANOMALY" if result["anomaly"] else "NORMAL"
        print(
            f"{result['timestamp']:<10}"
            f"{result['packets']:<12}"
            f"{result['baseline']:<14}"
            f"{status}"
        )

    anomaly_count = sum(
        result["anomaly"] for result in results
    )

    print("-" * 55)
    print(f"Total samples: {len(traffic)}")
    print(f"Anomalies detected: {anomaly_count}")

    print("\n=== Multiprocessing Summary ===")

    summaries = analyze_in_parallel(traffic)

    for number, summary in enumerate(summaries, start=1):
        print(
            f"Chunk {number}: "
            f"samples={summary['samples']}, "
            f"average={summary['average']}, "
            f"maximum={summary['maximum']}, "
            f"total={summary['total_packets']}"
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        columns = [
            "timestamp",
            "packets",
            "baseline",
            "anomaly",
            "window_average",
        ]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to: {OUTPUT_FILE}")
    print("Detection completed successfully.")


if __name__ == "__main__":
    main()
