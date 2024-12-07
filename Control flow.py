def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to be applied.

    Returns:
    - float: The final price after applying the discount if applicable.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate and print the final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    if discount_percentage >= 20:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")