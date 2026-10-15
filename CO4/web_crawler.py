import asyncio
import time

async def fetch_url(url, semaphore):
    async with semaphore:
        print(f"Starting download: {url}")
        await asyncio.sleep(1)
        print(f"Finished download: {url}")
        return f"Content of {url}"

async def worker(name, queue, semaphore):
    while True:
        url = await queue.get()
        try:
            await fetch_url(url, semaphore)
        finally:
            queue.task_done()

async def main():
    urls = [f"https://example.com/page/{i}" for i in range(1, 4)]
    queue = asyncio.Queue()
    semaphore = asyncio.Semaphore(2)
    
    for url in urls:
        await queue.put(url)

    workers = [asyncio.create_task(worker(f"Worker-{i}", queue, semaphore)) for i in range(2)]
    await queue.join()
    
    for w in workers:
        w.cancel()

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(f"Crawler finished in {time.time() - start:.2f} seconds.")
