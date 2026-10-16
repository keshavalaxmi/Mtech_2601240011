
# DDoS Traffic Anomaly Detector

## 1. Project Overview

The DDoS Traffic Anomaly Detector is a Python-based educational project that identifies unusually high network traffic using a sliding-window statistical approach. It processes traffic samples, calculates baseline statistics, flags potential anomalies, and saves detection results to a CSV file.

The project uses simulated traffic data for demonstration and testing.

## 2. Objectives

- Detect unusual traffic spikes.
- Calculate sliding-window traffic statistics.
- Analyze traffic chunks using multiprocessing.
- Store detection results in CSV format.
- Test correctness using unit tests.
- Evaluate execution time and throughput.

## 3. Technologies Used

- Python
- CSV data processing
- Collections and deque
- Multiprocessing
- Tkinter GUI
- unittest
- Ruff
- mypy

## 4. Project Structure

```text
ddos-traffic-anomaly-detector/
├── data/
│   └── traffic.csv
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── statistics_engine.py
│   ├── anomaly_detector.py
│   ├── parallel_processor.py
│   ├── benchmark.py
│   └── gui.py
├── tests/
│   ├── test_detector.py
│   └── test_statistics.py
├── output/
│   └── detection_results.csv
└── README.md
```

## 5. Algorithm

1. Read traffic samples from the CSV file.
2. Maintain a sliding window of recent traffic values.
3. Calculate the previous window's average.
4. Compare the current value against the configured threshold.
5. Mark unusually high values as potential anomalies.
6. Update the streaming statistics.
7. Generate a detection report.
8. Analyze independent traffic chunks using multiprocessing.
9. Save results to a CSV file.

## 6. Complexity Analysis

Let n represent the number of traffic samples and w represent the sliding-window size.

- Streaming statistics update: O(1) amortized time per sample.
- Streaming statistics storage: O(w).
- Current anomaly detection: O(n × w) time in the general case because the previous window is copied and summed for each sample.
- Detection result storage: O(n).
- Chunk summary analysis: O(n) total work across all chunks, excluding multiprocessing overhead.

## 7. Execution Instructions

Activate the project's virtual environment, then run:

```bash
python -m src.main
```

To launch the graphical interface:

```bash
python -m src.gui
```

To run unit tests:

```bash
python -m unittest discover -s tests -v
```

To run static type checking:

```bash
python -m mypy src
```

To run linting:

```bash
python -m ruff check src tests
```

To run the performance benchmark:

```bash
python -m src.benchmark
```

## 8. Testing Results

The project contains seven unit tests covering anomaly detection and streaming statistics.

Recorded test result:

- Tests executed: 7
- Status: Passed
- Ruff linting: Passed
- mypy: Run to verify static typing

## 9. Performance Evaluation

Recorded benchmark using 6,000 simulated traffic samples:

- Execution time: 0.013473 seconds
- Throughput: approximately 445,335 samples per second
- Reported anomalies: 1,000

These measurements describe one local benchmark run. Results can vary with hardware, Python version, and input data.

## 10. Limitations

- The traffic dataset is simulated and does not establish real-world DDoS detection accuracy.
- The detector uses a simple statistical threshold.
- Legitimate traffic spikes may be flagged as anomalies.
- The project does not automatically block malicious traffic.
- Larger real-world datasets and additional evaluation metrics are needed.

## 11. Future Enhancements

- Test with realistic network traffic datasets.
- Evaluate precision, recall, and false-positive rate.
- Improve the detection algorithm.
- Add live network traffic ingestion.
- Improve dashboard visualizations.
- Add automated testing to a CI/CD pipeline.

## 12. Conclusion

The project demonstrates a modular Python implementation of statistical traffic anomaly detection, sliding-window processing, multiprocessing summaries, CSV reporting, graphical visualization, and software quality checks. It provides a foundation for further experimentation with network traffic analysis.
