def calculate_average(numbers: list[int]) -> float:
    if not numbers:
        return 0.0

    return sum(numbers) / len(numbers)


def main() -> None:
    numbers = [10, 20, 30, 40]
    average = calculate_average(numbers)

    print("Numbers:", numbers)
    print("Average:", average)


if __name__ == "__main__":
    main()
