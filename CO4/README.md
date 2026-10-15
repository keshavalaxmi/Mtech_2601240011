## 1. High-Throughput Web Crawler

* **Objective:** Fetch multiple URLs concurrently using an asynchronous queue and semaphore to manage network throughput and rate limits efficiently.

* **Input:** A list of URL strings (e.g., `['https://example.com/page/1', ...]`).

* **Output:** Simulation logs showing start and finish times for each download, along with total execution time.

* **Algorithm:**
  1. Initialize an `asyncio.Queue` loaded with the target URLs and an `asyncio.Semaphore` to cap concurrent requests.
  2. Spawn multiple worker coroutines running concurrently.
  3. Each worker pulls a URL from the queue, acquires the semaphore lock, simulates network fetching via an asynchronous delay, and marks the queue task as done.
  4. Block the main execution using `queue.join()` until all items are processed, then cancel active workers.

* **Time Complexity:** O(N / C) where $N$ is the number of URLs and $C$ is the concurrency limit.

* **Space Complexity:** O(N + C) to store queue elements and worker task references.
