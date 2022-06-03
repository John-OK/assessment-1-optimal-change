from optimal_change import optimal_change

print(optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

print(optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

# amount_paid less than optimal change
print(optimal_change(31.51, 5) == "Insufficient payment.")

# no cost
print(optimal_change(0, 50) == "No change due.")

# cost and paid equal
print(optimal_change(50, 50) == "No change due.")

# only one denomination returned
print(optimal_change(1, 2) == "The optimal change for an item that costs $1 with an amount paid of $2 is 1 $1 bill.")