# Branch & Bound + Complexity

## Choosing an Algorithm for a Large Application

An e-commerce application needs to process millions of records.

We have three algorithms with the following complexities:

- Algorithm A → O(n)
- Algorithm B → O(n log n)
- Algorithm C → O(n²)

## Question

a) Which algorithm would generally be preferred for very large n?

b) Why is O(n²) potentially problematic?

c) Give a real-world situation where each complexity might occur.

## Solution

According to the scenario, the e-commerce application has to process millions of records.

Therefore, we need to select an algorithm that takes less time for a large input size.

The given complexities are:

O(n) < O(n log n) < O(n²)

Therefore, Algorithm A with O(n) complexity is generally preferred.

## 1. Choosing the Best Algorithm

### Algorithm A → O(n)

Algorithm A is preferred because it has linear time complexity.

It processes the records approximately one by one.

For example:

1,000 records → approximately 1,000 operations

1,000,000 records → approximately 1,000,000 operations

Therefore, O(n) is suitable for processing millions of records.

### Algorithm B → O(n log n)

Algorithm B is also efficient for large data.

However, it performs more operations than O(n).

A common example of O(n log n) is Merge Sort.

### Algorithm C → O(n²)

Algorithm C is not suitable for millions of records because the number of operations increases very quickly.

For example:

If n = 1,000

n² = 1,000 × 1,000

n² = 1,000,000 operations

If n = 1,000,000

n² = 1,000,000 × 1,000,000

n² = 1,000,000,000,000 operations

Therefore, O(n²) can become very slow for a large input.

## 2. Real-World Examples

### O(n) Example

Suppose an e-commerce application wants to count the total number of products.

Each product is checked once.

    for each product:
        process product

Time Complexity: O(n)

### O(n log n) Example

Suppose an e-commerce application wants to sort millions of products according to their price.

Merge Sort can be used for this operation.

Time Complexity: O(n log n)

### O(n²) Example

Suppose an e-commerce application wants to compare every product with every other product to find duplicate products.

    for each product:
        compare with every other product

Time Complexity: O(n²)

This becomes very slow when the number of products is very large.

## 3. Algorithm

### Input

- Number of records n
- Three algorithms with different time complexities

### Steps

1. Identify the number of records.
2. Since the application has millions of records, choose an efficient algorithm.
3. Compare the complexities:
   - Algorithm A → O(n)
   - Algorithm B → O(n log n)
   - Algorithm C → O(n²)
4. Compare their growth rates.
5. Select the algorithm with the lowest complexity.
6. Therefore, select Algorithm A.

## 4. Python Implementation

```python
def process_records(records):
    for record in records:
        print("Processing:", record)


records = ["Product1", "Product2", "Product3", "Product4"]

process_records(records)
```

## Output

```text
Processing: Product1
Processing: Product2
Processing: Product3
Processing: Product4
```

## 5. Complexity Comparison

| Algorithm | Complexity | Suitability for Millions of Records |
|-----------|------------|-------------------------------------|
| Algorithm A | O(n) | Best |
| Algorithm B | O(n log n) | Good |
| Algorithm C | O(n²) | Poor |

## 6. Final Conclusion

Algorithm A with O(n) complexity is generally preferred for an e-commerce application that processes millions of records.

O(n) is more efficient because the number of operations increases linearly with the input size.

O(n log n) is also suitable for large inputs, but it is slower than O(n).

O(n²) is potentially problematic because the number of operations grows very rapidly as the input size increases.

Therefore:

Best choice → Algorithm A → O(n)
