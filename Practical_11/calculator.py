def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


def main() -> None:
    price = 100.0
    quantity = 3

    total = calculate_total(price, quantity)

    print("Price:", price)
    print("Quantity:", quantity)
    print("Total:", total)


if __name__ == "__main__":
    main()
