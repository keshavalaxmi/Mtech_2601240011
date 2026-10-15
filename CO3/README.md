Question 2: PEP 604 Union Type Syntax for Contact Information

#1. Algorithm
Define Function Signature: Create a function named process_contact that accepts a parameter contact using the PEP 604 union syntax (str | int), meaning it can accept either a string (for emails or formatted phone numbers) or an integer (for numeric mobile numbers).

Evaluate Contact Type/Content:

If the contact is an integer, categorize it as a numeric mobile number.

If the contact string contains an "@", categorize it as an email address.

Otherwise, categorize it as a string-based mobile number.

Return Result: Return a formatted string detailing the contact type and value.

#2. Pseudocode
Plaintext
FUNCTION process_contact(contact: str | int) -> str
    IF TYPE OF contact IS int THEN
        RETURN "Mobile Number (Integer): " + contact
    ELSE IF "@" IN contact THEN
        RETURN "Email Address: " + contact
    ELSE
        RETURN "Mobile Number (String): " + contact
    END IF
END FUNCTION
