# Identity Verification Data Pipeline

## Q22. Identity Verification Data Pipeline 

An identity-verification service receives a very large stream of records. It must remove duplicate IDs, group records by region, validate incoming records and record processing time.

---

# (a) Appropriate Python Data Structures

Two appropriate Python data structures are:

### 1. Set

A **set** is used for duplicate detection because it stores only unique values.

For this problem, a set can store the IDs that have already been processed.

Example:

```python
processed_ids = set()

if record["id"] not in processed_ids:
    processed_ids.add(record["id"])
```

This ensures that duplicate IDs are removed.

### 2. Dictionary

A **dictionary** is suitable for grouping records by region.

The region can be used as the key and the records belonging to that region can be stored as the value.

Example:

```python
records_by_region = {}

region = record["region"]

if region not in records_by_region:
    records_by_region[region] = []

records_by_region[region].append(record)
```

Therefore:

* **Set** → Used for duplicate ID detection.
* **Dictionary** → Used for grouping records by region.

---

# (b) Generator-Based Pipeline

A generator-based pipeline processes records one at a time instead of loading the complete stream into memory.

This is useful when the service receives a **very large stream of records**.

The pipeline can contain the following stages:

1. Receive records.
2. Remove duplicate IDs.
3. Validate records.
4. Group valid records by region.
5. Return the processed records.

### Python Implementation

```python
def remove_duplicates(records):
    seen_ids = set()

    for record in records:
        record_id = record["id"]

        if record_id not in seen_ids:
            seen_ids.add(record_id)
            yield record


def validate_records(records):
    for record in records:

        if "id" in record and "region" in record:
            yield record


def group_by_region(records):
    regions = {}

    for record in records:
        region = record["region"]

        if region not in regions:
            regions[region] = []

        regions[region].append(record)

    yield regions
```

### Generator Pipeline

```python
records = [
    {"id": 101, "region": "South"},
    {"id": 102, "region": "North"},
    {"id": 101, "region": "South"},
    {"id": 103, "region": "East"},
    {"id": 104, "region": "South"}
]

unique_records = remove_duplicates(records)

valid_records = validate_records(unique_records)

grouped_records = group_by_region(valid_records)

result = next(grouped_records)

print(result)
```

### Output

```text
{
    'South': [
        {'id': 101, 'region': 'South'},
        {'id': 104, 'region': 'South'}
    ],
    'North': [
        {'id': 102, 'region': 'North'}
    ],
    'East': [
        {'id': 103, 'region': 'East'}
    ]
}
```

The use of `yield` makes the processing **memory efficient**, because records can be processed one at a time.

---

# (c) Decorator to Measure Processing Time

A **decorator** can be used to measure how much time a function takes to execute.

Python's `time` module can be used to record the start and end time.

### Python Implementation

```python
import time


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
```

The decorator can be applied to a processing function.

```python
@measure_time
def process_records(records):

    unique_records = remove_duplicates(records)

    valid_records = validate_records(unique_records)

    return list(valid_records)
```

When `process_records()` is executed, the decorator automatically records and prints the processing time.

### Example Output

```text
Processing time: 0.000012 seconds
```

Thus, the decorator allows processing time to be measured without changing the main processing logic.

---

# (d) EAFP vs LBYL for Validation

For validating incoming records, **EAFP (Easier to Ask for Forgiveness than Permission)** is more appropriate.

EAFP attempts the operation directly and handles errors using `try-except`.

For example:

```python
def validate_record(record):

    try:
        record_id = record["id"]
        region = record["region"]

        return True

    except (KeyError, TypeError):

        return False
```

### Why EAFP is Appropriate

The identity-verification service receives a **large stream of incoming records**. Some records may be missing required fields or may have an invalid structure.

Instead of checking every condition before accessing the data, EAFP directly attempts to access the required fields and handles exceptions when invalid data is encountered.

### EAFP

```python
try:
    record_id = record["id"]
    region = record["region"]
except (KeyError, TypeError):
    return False
```

### LBYL

LBYL (**Look Before You Leap**) checks the conditions before performing the operation.

```python
if "id" in record and "region" in record:
    record_id = record["id"]
    region = record["region"]
```

For this scenario, **EAFP is preferred** because it is concise and handles unexpected or malformed incoming records effectively.

---

# Complete Python Implementation

```python
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
```

# Output

```text
Processing time: 0.00001 seconds

Grouped Records:
{
    'South': [
        {'id': 101, 'region': 'South'},
        {'id': 104, 'region': 'South'}
    ],
    'North': [
        {'id': 102, 'region': 'North'}
    ],
    'East': [
        {'id': 103, 'region': 'East'}
    ]
}
```
