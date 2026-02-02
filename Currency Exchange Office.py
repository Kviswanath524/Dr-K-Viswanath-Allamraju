# Currency Exchange Office

# Input available currencies (comma-separated)
available_currencies = input("Enter available currencies: ").split(", ")

# Input currencies to order (comma-separated)
currencies_to_order = input("Enter currencies to order: ").split(", ")

# Customer's requested currency
requested_currency = input("Enter the currency requested by the customer: ")

# Check if the requested currency is available
if requested_currency in available_currencies:
    print(f'Yes, "{requested_currency}" is available.')
    available_currencies.remove(requested_currency)
    currencies_to_order.append(requested_currency)
else:
    print(f'Sorry, "{requested_currency}" is not available.')
    currencies_to_order.append(requested_currency)

# Display updated lists
print("Updated available currencies:", available_currencies)
print("Updated currencies to order:", currencies_to_order)
