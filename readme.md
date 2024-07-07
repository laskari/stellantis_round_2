This repo having solution to optimization task for the vending machine

## Problem statement

Given a vending machine information with the prices of various items, weights of the available items, the total money available to purchase, find the items can be purchased in the given money.

# Execution steps:

# Task-1:
python optimize_task_1.py <the_total_moeny_available>
<br><\n>
python optimize_task_1.py 3

Solution:
{'Items Retreived': ['Water', 'Energy Drink'], 'Total Cost': 3.0, 'Leftover Money': 0.0, 'Total Weight': 900}

# Task-2:
python optimize_task_2.py --one-dollar-coins 3 --half-dollar-coins 2 --twenty-cent-coins 5 --five-cent-coins 10

Solution:
{'Items Retrieved': ['Soda', 'Candy', 'Water', 'Energy Drink'], 'Total Cost': 5.25, 'Leftover Money': 0.25, 'Total Weight': 1300}

# Task-3:
python optimize_task_3c.py friends_info.json

Solution:
{
    "friend1": {
        "Items Retrieved": [
            "Soda",
            "Chips",
            "Water",
            "Chocolate"
        ],
        "Total Cost": 5.2,
        "Leftover Money": 0.3,
        "Total Weight": 1150
    },
    "friend2": {
        "Items Retrieved": [
            "Water",
            "Gum",
            "Energy Drink"
        ],
        "Total Cost": 3.5,
        "Leftover Money": 0.15,
        "Total Weight": 905
    },
    "friend3": {
        "Items Retrieved": [
            "Soda",
            "Water",
            "Chocolate"
        ],
        "Total Cost": 4.0,
        "Leftover Money": 0.45,
        "Total Weight": 1050
    }
}
{
    "Total Products Bought": [
        "Energy Drink",
        "Gum",
        "Soda",
        "Chips",
        "Chocolate",
        "Water"
    ],
    "Total Money Spent": 12.7,
    "Total Money Leftover": 0.8999999999999999,
    "Total Weight": 3105
}
