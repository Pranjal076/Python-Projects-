# Book pricing details
book_price = 24.95
discount_rate = 0.40
num_copies = 60
shipping_first_copy = 3.00
shipping_additional_copy = 0.75

# Calculate discounted price per book
discount_amount = book_price * discount_rate
discounted_price = book_price - discount_amount

# Total cost for books
total_book_cost = discounted_price * num_copies

# Total shipping cost
total_shipping_cost = shipping_first_copy + shipping_additional_copy * (num_copies - 1)

# Final wholesale cost
total_wholesale_cost = total_book_cost + total_shipping_cost

# Display results
print("📚 Wholesale Cost Calculation")
print(f"Discounted Price per Book: ${discounted_price:.2f}")
print(f"Total Book Cost for {num_copies} copies: ${total_book_cost:.2f}")
print(f"Total Shipping Cost: ${total_shipping_cost:.2f}")
print(f"✅ Final Wholesale Cost: ${total_wholesale_cost:.2f}")