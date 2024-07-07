import pandas as pd
import argparse

def optimize_vending_machine(prices, weights, total_available):
    n = len(prices)
    dp = {0: (0, [])}
    
    for i in range(n):
        temp_dp = dp.copy()
        for current_filled, (current_item_price, current_items) in dp.items():
            new_filled = current_filled + prices[i]
            
            if new_filled <= total_available:
                new_weight = current_item_price + weights[i]
                if new_filled not in temp_dp or new_weight > temp_dp[new_filled][0]:
                    temp_dp[new_filled] = (new_weight, current_items + [i])
        dp = temp_dp
    
    max_value = max(dp.values(), key=lambda x: x[0])
    
    return max_value

def main(coins, excluded_items):
    total_available = (
        coins['1'] * 1.0 +
        coins['0.5'] * 0.5 +
        coins['0.2'] * 0.2 +
        coins['0.05'] * 0.05
    )

    data = pd.read_csv("./sample_data_6_6_4.csv")
    data = data[['ItemID', 'ItemName', 'Cost', 'Weight']]
    data = data.drop_duplicates()
    data.sort_values('ItemID', inplace=True)
    
    # Exclude specified items
    data = data[~data['ItemName'].isin(excluded_items)]
    
    item_names = data["ItemName"].tolist()
    prices = data["Cost"].tolist()
    weights = data["Weight"].tolist()

    max_value, included_items = optimize_vending_machine(prices, weights, total_available)
    included_item_names = [item_names[i] for i in included_items]
    total_cost = sum(prices[i] for i in included_items)
    leftover_money = round((total_available - total_cost), 2)

    result = {
        "Items Retrieved": included_item_names,
        "Total Cost": total_cost,
        "Leftover Money": leftover_money,
        "Total Weight": max_value
    }

    print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimize vending machine item retrieval")
    parser.add_argument('--one-dollar-coins', type=int, required=True, help="Number of 1$ coins")
    parser.add_argument('--half-dollar-coins', type=int, required=True, help="Number of 0.5$ coins")
    parser.add_argument('--twenty-cent-coins', type=int, required=True, help="Number of 0.2$ coins")
    parser.add_argument('--five-cent-coins', type=int, required=True, help="Number of 0.05$ coins")
    parser.add_argument('--excluded-items', type=str, nargs='*', default=[], help="List of item names to exclude")
    args = parser.parse_args()
    excluded_items = args.excluded_items
    Fiend_allergic_items = list(excluded_items)

    Friend_budget = {
        '1': args.one_dollar_coins,
        '0.5': args.half_dollar_coins,
        '0.2': args.twenty_cent_coins,
        '0.05': args.five_cent_coins
    }

    main(Friend_budget, Fiend_allergic_items)
