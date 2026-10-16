
from concurrent.futures import ProcessPoolExecutor
from statistics import mean


def analyze_chunk(chunk: list[int]) -> dict:
    """Calculate summary statistics for one traffic chunk."""
    return {
        "samples": len(chunk),
        "average": round(mean(chunk), 2) if chunk else 0,
        "maximum": max(chunk) if chunk else 0,
        "total_packets": sum(chunk),
    }


def analyze_in_parallel(
    traffic: list[int], workers: int = 2
) -> list[dict]:
    """Analyze separate traffic chunks using multiple processes."""
    if not traffic:
        return []

    chunk_size = max(1, (len(traffic) + workers - 1) // workers)

    chunks = [
        traffic[i:i + chunk_size]
        for i in range(0, len(traffic), chunk_size)
    ]

    with ProcessPoolExecutor(
        max_workers=min(workers, len(chunks))
    ) as executor:
        return list(executor.map(analyze_chunk, chunks))
