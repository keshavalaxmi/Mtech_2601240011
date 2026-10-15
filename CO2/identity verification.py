
import time


# Generator to remove duplicate IDs
def remove_duplicates(records):

    seen_ids = set()

    for record in records:

        record_id = record["id"]

        if record_id not in seen_ids:

            seen_ids.add(record_id)

            yield record


# Generator to validate records
def validate_records(records):

    for record in records:

        try:
            record["id"]
            record["region"]

            yield record

        except (KeyError, TypeError):

            continue


# Group records by region
def group_by_region(records):

    regions = {}

    for record in records:

        region = record["region"]

        if region not in regions:
            regions[region] = []

        regions[region].append(record)

    return regions


# Decorator to measure processing time
def measure_time(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(
            "Processing time:",
            end_time - start_time,
            "seconds"
        )

        return result


    return wrapper


# Complete processing pipeline
@measure_time
def process_records(records):

    unique_records = remove_duplicates(records)

    valid_records = validate_records(unique_records)

    grouped_records = group_by_region(valid_records)

    return grouped_records


# Incoming records
records = [
    {"id": 101, "region": "South"},
    {"id": 102, "region": "North"},
    {"id": 101, "region": "South"},
    {"id": 103, "region": "East"},
    {"id": 104, "region": "South"},
    {"id": 102, "region": "North"}
]


# Process the records
result = process_records(records)

print("Grouped Records:")
print(result)
