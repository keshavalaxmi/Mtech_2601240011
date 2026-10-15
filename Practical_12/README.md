# Exercise: Calculate Average

## Objective

To create a Python program that calculates the average of a list of numbers using a function.

## Files

* `average.py` – Contains the function to calculate the average.
* `README.md` – Contains the project description and instructions.

## Function

### calculate_average()

The `calculate_average()` function takes a list of integers and calculates their average.

If the list is empty, the function returns `0.0`.

## Example

Given the numbers:

`[10, 20, 30, 40]`

The average is:

`(10 + 20 + 30 + 40) / 4 = 25.0`

## Expected Output

```text
Numbers: [10, 20, 30, 40]
Average: 25.0
```

## Concepts Used

* Python functions
* Lists
* Type hints
* `sum()` function
* `len()` function
* `main()` function
* Conditional execution using `if __name__ == "__main__"`

## How to Run

Run the following command:

```bash
python average.py
```

## Conclusion

The program successfully calculates the average of a list of numbers and handles an empty list safely by returning `0.0`.
