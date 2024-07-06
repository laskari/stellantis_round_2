import pandas as pd
import os

data = pd.read_csv("./sample_data_6_6_4.csv")
data = data[['ItemID', 'ItemName', 'Cost', 'Weight']]
data = data.drop_duplicates()
print(data)

# unique_item_dict = {}
# for index, row in data.iterrows():
#     unique_item_dict[row['ItemName']] = [row['Cost'], row['Weight']]

# print(unique_item_dict)