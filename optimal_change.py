from math import floor

# map of denominations (in cents to avoid decimal errors)
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

# order to cycle through when giving change
denom_order = ['$100', '$50', '$20',
               '$10', '$5', '$1', 'quarter', 'dime', 'nickel', 'penny']


def text_formatter(item_cost, amount_paid, denomination_map):
    change_message = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is"

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
    change_message = change_message[0:idx_last_comma + 2] + "and " + change_message[idx_last_comma + 2:]

    return change_message
    

def optimal_change(item_cost, amount_paid):
    change_due_in_cents = (amount_paid * 100) - (item_cost * 100)

    # dict of number of each denomination given in change
    return_denominations = {}

    for denom in denom_order:
        value = denominations[denom]
        num_to_give = floor(change_due_in_cents / value)
        remaining_change_due = change_due_in_cents % value
        if num_to_give >= 1:
            return_denominations[denom] = num_to_give
            change_due_in_cents = remaining_change_due

    return text_formatter(item_cost, amount_paid, return_denominations)


print(optimal_change(31.51, 50))