import pandas as pd
import argparse

def optimize_vending_machine(prices, weights, total_available):
    n = len(prices)
    dp = {0 : (0, [])}
    
    for i in range(n):
        temp_dp = dp.copy()
        for current_filled, (current_item_price, current_items) in dp.items():
            new_filled = current_filled + prices[i]
            
            if new_filled <= total_available:
                new_weight = current_item_price + weights[i]
                if new_filled not in temp_dp or new_weight > temp_dp[new_filled][0]:
                    temp_dp[new_filled] = (new_weight, current_items + [i])
        dp = temp_dp
    # print(dp)
    max_value = max(dp.values(), key=lambda x: x[0])
    # print(max_value)
    return max_value


def main(total_available):
    data = pd.read_csv("./sample_data_6_6_4.csv")
    data = data[['ItemID', 'ItemName', 'Cost', 'Weight']]
    data = data.drop_duplicates()
    data.sort_values('ItemID', inplace=True)
    item_names = data["ItemName"].tolist()
    prices = data["Cost"].tolist()
    weights = data["Weight"].tolist()

    max_value, included_items = optimize_vending_machine(prices, weights, total_available)
    included_item_names = [item_names[i] for i in included_items]
    total_cost = sum(prices[i] for i in included_items)
    leftover_money =  total_available - total_cost

    result = {
        "Items Retreived": included_item_names,
        "Total Cost" : total_cost,
        "Leftover Money": leftover_money,
        "Total Weight": max_value
    }

    print(result)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Optimise vending machine item retrieval")
    parser.add_argument('total_available', type=float, help="Total available money to buy items")
    args =  parser.parse_args()
    main(args.total_available)
