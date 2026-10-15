# Exercise: Property-Based Testing with Hypothesis

## Objective

To implement simple mathematical functions and test them using Python and the Hypothesis property-based testing framework.

## Files

* `app.py` – Contains the `add()` and `multiply()` functions.
* `test_app.py` – Contains normal unit tests and a Hypothesis property-based test.

## Functions

### add()

The `add()` function takes two numbers and returns their sum.

### multiply()

The `multiply()` function takes two numbers and returns their product.

## Testing

The project uses:

* `pytest` – For running the tests.
* `hypothesis` – For property-based testing.

The normal tests check specific values:

* `add(2, 3)` returns `5`.
* `multiply(3, 4)` returns `12`.

The Hypothesis test checks the `add()` function with automatically generated integer values.

## Installation

Install the required packages using:

```bash
pip install pytest hypothesis
```

## Run Tests

Run the following command:

```bash
pytest
```

## Expected Result

All tests should pass successfully.

Example:

```text
3 passed
```

## Conclusion

The Python functions were successfully tested using normal unit testing and Hypothesis property-based testing. Hypothesis automatically generates different integer inputs to verify that the `add()` function works correctly.
