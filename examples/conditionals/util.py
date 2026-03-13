# utils.py - Utility functions

def format_price(amount, currency="$"):
    """Format a number as a price string."""
    return f"{currency}{amount:,.2f}"


def validate_email(email):
    """Basic email validation: must contain @ and a dot after @."""
    if "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    return "." in parts[1]


TAX_RATE = 0.20
