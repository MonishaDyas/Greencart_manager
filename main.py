from members import calculate_balance, check_senior
from catalogue import display_products
from pricing import stock_value
from display import show_message

catalogue = [
    ["Soap", "Household", 5.50, 15],
    ["Rice", "Food", 15.00, 10]
]

show_message("Welcome to GreenCart Manager")

balance = calculate_balance(100)

print("Wallet Balance:", balance)

display_products(catalogue)






