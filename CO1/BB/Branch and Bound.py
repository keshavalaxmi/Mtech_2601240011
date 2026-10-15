# Branch & Bound + Complexity
# Choosing an Algorithm for a Large Application

# Algorithm A - O(n)
def algorithm_a(records):
    for record in records:
        print("Processing:", record)


# Algorithm B - O(n log n)
def algorithm_b(records):
    return sorted(records)


# Algorithm C - O(n²)
def algorithm_c(records):
    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            print("Comparing:", records[i], "and", records[j])


# E-commerce product records
products = ["Laptop", "Mobile", "Headphones", "Keyboard"]

# Algorithm A
print("Algorithm A - O(n)")
algorithm_a(products)

# Algorithm B
print("\nAlgorithm B - O(n log n)")
print("Sorted products:", algorithm_b(products))

# Algorithm C
print("\nAlgorithm C - O(n²)")
algorithm_c(products)

# Final conclusion
print("\nConclusion:")
print("Algorithm A - O(n) is the best choice for millions of records.")
print("Algorithm B - O(n log n) is also suitable for large data.")
print("Algorithm C - O(n²) is not suitable for very large data.")
