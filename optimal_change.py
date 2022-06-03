from math import floor

# Map of denominations (in cents to avoid decimal errors).
denominations = {
    '$100'   : 10000,
    '$50'    : 5000,
    '$20'    : 2000,
    '$10'    : 1000,
    '$5'     : 500,
    '$1'     : 100,
    'quarter': 25,
    'dime'   : 10,
    'nickel' : 5,
    'penny'  : 1,
}

# Order to cycle through when giving change.
denom_order = ['$100', '$50', '$20',
               '$10', '$5', '$1', 'quarter', 'dime', 'nickel', 'penny']

# Logic to format return text with proper punctuation and noun pluralization.
def text_formatter(item_cost, amount_paid, denomination_map):
    change_message = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is"

    # Need these to separate from paper denominations (i.e., "bills")
    coins = ['quarter', 'dime', 'nickel', 'penny']

    for denom in denom_order:
        if denom in denomination_map:
            number = denomination_map[denom]
            if denom == 'penny' and number > 1:
                change_message += f" {number} pennies,"
            elif denom in coins and number > 1:
                change_message += f" {number} {denom}s,"
            elif number > 1:
                change_message += f" {number} {denom} bills,"
            elif denom in coins:
                change_message += f" {number} {denom},"
            else:
                change_message += f" {number} {denom} bill,"

    change_message = change_message[:-1] + "."
    idx_last_comma = change_message.rfind(',')
    if idx_last_comma > 0:
        change_message = change_message[0:idx_last_comma + 2] + "and " + change_message[idx_last_comma + 2:]

    return change_message
    
# Main function to calulate proper optimal change and return properly formatted and grammatically correct string of optimal change to return.
def optimal_change(item_cost, amount_paid):
    if amount_paid < item_cost:
        return "Insufficient payment."
    elif item_cost == 0 or item_cost == amount_paid:
        return "No change due."

    # Convert to cents in order to avoid decimal errors
    change_due_in_cents = (amount_paid * 100) - (item_cost * 100)

    # dict of number of each denomination given in change
    return_denominations = {}

    # Loop through denominations from highest to lowest to determine how many of each denomination to return and store result in "return_denominations" to be passed to "text_formatter."
    for denom in denom_order:
        value = denominations[denom]
        num_to_give = floor(change_due_in_cents / value)
        remaining_change_due = change_due_in_cents % value
        if num_to_give >= 1:
            return_denominations[denom] = num_to_give
            change_due_in_cents = remaining_change_due

    return text_formatter(item_cost, amount_paid, return_denominations)