from math import floor
def optimal_change(item_cost, amount_paid):
    formatted_change_msg = "<FORMATTING FUNCTION>"
    change_message = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is {formatted_change_msg}."

    change_due_in_cents = (amount_paid * 100) - (item_cost * 100)

    # map of denominations (in cents to avoid decimal errors)
    denominations = {
        '$100'    : 10000,
        '$50'     : 5000,
        '$20'     : 2000,
        '$10'     : 1000,
        '$5'      : 500,
        '$1'      : 100,
        'quarter' : 25,
        'dime'    : 10,
        'nickel'  : 5,
        'penny'   : 1,
    }

    denom_order = ['$100', '$50', '$20',
                   '$10', '$5', '$1', 'quarter', 'dime', 'nickel', 'penny', ]

    # dict of number of each denomination given in change
    return_denominations = {}

    for denom in denom_order:
        value = denominations[denom]
        num_to_give = floor(change_due_in_cents / value)
        remaining_change_due = change_due_in_cents % value
        if num_to_give >= 1:
            return_denominations[denom] = num_to_give
            change_due_in_cents = remaining_change_due
            print(value, num_to_give, remaining_change_due, return_denominations)






    return change_message

print(optimal_change(62.13, 100))