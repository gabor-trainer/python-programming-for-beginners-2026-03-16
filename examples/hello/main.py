# order_calculator.py - Calculate order total with tax

TAX_RATE = 0.20  # 20% tax rate

print("=== Order calculator ===")
print()

item_name = input("Item name: ")
price_str = input("Price per unit: ")
quantity_str = input("Quantity: ")

price = float(price_str)
quantity = int(quantity_str)

subtotal = price * quantity
tax = subtotal * TAX_RATE
total = subtotal + tax

print()
print(f"Item:     {item_name}")
print(f"Price:    ${price:.2f} x {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (20%): ${tax:.2f}")
print(f"Total:    ${total:.2f}")
