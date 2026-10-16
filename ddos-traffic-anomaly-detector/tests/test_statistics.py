
import unittest

from src.statistics_engine import StreamingStatistics


class TestStreamingStatistics(unittest.TestCase):

    def test_window_average(self):
        stats = StreamingStatistics(window_size=3)

        stats.update(10)
        stats.update(20)
        result = stats.update(30)

        self.assertEqual(result["window_total"], 60)
        self.assertEqual(result["window_average"], 20.0)

    def test_sliding_window_removes_oldest_value(self):
        stats = StreamingStatistics(window_size=3)

        stats.update(10)
        stats.update(20)
        stats.update(30)
        result = stats.update(40)

        self.assertEqual(result["window_total"], 90)
        self.assertEqual(result["window_average"], 30.0)

    def test_sample_count(self):
        stats = StreamingStatistics(window_size=2)

        stats.update(15)
        result = stats.update(25)

        self.assertEqual(result["samples_seen"], 2)
        self.assertEqual(stats.total_packets, 40)

    def test_invalid_window_size(self):
        with self.assertRaises(ValueError):
            StreamingStatistics(window_size=0)


if __name__ == "__main__":
    unittest.main()
