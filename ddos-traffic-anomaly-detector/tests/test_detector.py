
import unittest

from src.anomaly_detector import detect_anomalies


class TestAnomalyDetector(unittest.TestCase):

    def test_detects_high_traffic_spike(self):
        traffic = [40, 42, 41, 43, 45, 200]

        results = detect_anomalies(
            traffic,
            window_size=5,
            threshold=2.0,
        )

        self.assertTrue(results[-1]["anomaly"])

    def test_normal_traffic_is_not_flagged(self):
        traffic = [40, 42, 41, 43, 45, 44]

        results = detect_anomalies(
            traffic,
            window_size=5,
            threshold=2.0,
        )

        self.assertFalse(results[-1]["anomaly"])

    def test_empty_traffic(self):
        results = detect_anomalies([])

        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()
