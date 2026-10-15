def process_transaction(account_id: str, amount: float, is_deposit: bool) -> str:
    """
    Processes a banking transaction with PEP 484 type hints.
    """
    if amount <= 0:
        raise ValueError("Transaction amount must be greater than zero.")
    
    action = "deposited into" if is_deposit else "withdrawn from"
    return f"Successfully {action} account {account_id}: ${amount:.2f}"

# --- Example Usage ---
if __name__ == "__main__":
    result = process_transaction("ACC-98765", 1500.75, True)
    print(result)
