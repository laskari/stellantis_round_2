import pandas as pd
import argparse
import json

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

def process_friend(data, friend_info):
    excluded_items = friend_info["excluded_items"]
    coins = friend_info["coins"]
    
    total_available = (
        coins['1'] * 1.0 +
        coins['0.5'] * 0.5 +
        coins['0.2'] * 0.2 +
        coins['0.05'] * 0.05
    )
    
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

    return result

def main(friends_info):
    data = pd.read_csv("./sample_data_6_6_4.csv")
    data = data[['ItemID', 'ItemName', 'Cost', 'Weight']]
    data = data.drop_duplicates()
    data.sort_values('ItemID', inplace=True)
    
    results = {}
    global_summary = {
        "Total Products Bought": [],
        "Total Money Spent": 0,
        "Total Money Leftover": 0,
        "Total Weight": 0
    }
    
    for friend_name, friend_info in friends_info.items():
        result = process_friend(data, friend_info)
        results[friend_name] = result
        
        global_summary["Total Products Bought"].extend(result["Items Retrieved"])
        global_summary["Total Money Spent"] += result["Total Cost"]
        global_summary["Total Money Leftover"] += result["Leftover Money"]
        global_summary["Total Weight"] += result["Total Weight"]
    
    global_summary["Total Products Bought"] = list(set(global_summary["Total Products Bought"]))
    
    print(json.dumps(results, indent=4))
    print(json.dumps(global_summary, indent=4))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimize vending machine item retrieval")
    parser.add_argument('friends_info', type=str, help="Path to JSON file containing friends' information")
    args = parser.parse_args()

    with open(args.friends_info, 'r') as file:
        friends_info = json.load(file)

    main(friends_info)
