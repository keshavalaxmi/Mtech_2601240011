# Exercise: Asynchronous URL Fetching Using Python

## Objective

Implement asynchronous URL fetching using Python's `asyncio` and `aiohttp` libraries to retrieve data from multiple URLs concurrently, with timeout and retry mechanisms.

## Concepts Used

* Asynchronous programming
* `asyncio` library
* `aiohttp` library
* Async and await
* Concurrent execution
* HTTP requests and response status codes
* Timeout handling
* Retry mechanism
* Execution time measurement

## Asynchronous URL Fetching

The `fetch()` function sends an HTTP GET request to a given URL using an asynchronous session.

The program reads the response content and returns the URL, HTTP status code, and content length.

If a request fails, the program retries up to three times, waiting one second between attempts.

## Concurrent Execution

The `main()` function uses `asyncio.gather()` to fetch data from multiple URLs concurrently.

The total execution time is measured using the `time` module.

## Comparison

| Feature          | Sequential Execution    | Asynchronous Execution         |
| ---------------- | ----------------------- | ------------------------------ |
| Request handling | One request at a time   | Multiple requests concurrently |
| Execution time   | May take longer         | Can reduce waiting time        |
| Library          | `requests`              | `asyncio` and `aiohttp`        |
| Waiting          | Blocks the next request | Allows other tasks to run      |
| Use case         | Simple HTTP requests    | Multiple network requests      |

## Algorithm

1. Import the `asyncio`, `aiohttp`, and `time` libraries.
2. Define a list of URLs to fetch.
3. Create an asynchronous `fetch()` function.
4. Send an HTTP GET request using an asynchronous session.
5. Set a timeout of 10 seconds for each request.
6. Read the response content and obtain the status code.
7. Retry failed requests up to three times.
8. Create an asynchronous `main()` function.
9. Use `asyncio.gather()` to fetch all URLs concurrently.
10. Measure the total execution time.
11. Display the URL, status code, and content length.
12. Print the total time taken.

## Input

URLs:

* https://example.com
* https://www.python.org
* https://www.google.com

Maximum Attempts: 3

Timeout: 10 seconds

## Output

```text
('https://example.com', 200, 1256)
('https://www.python.org', 200, 50000)
('https://www.google.com', 200, 20000)
Time taken: 1.52 seconds
```

Note: The content lengths and execution time shown above are sample values. Actual results may vary depending on the websites and internet connection.

## Result

Successfully implemented asynchronous URL fetching using Python's `asyncio` and `aiohttp` libraries with concurrent execution, timeout handling, and retry mechanisms.
