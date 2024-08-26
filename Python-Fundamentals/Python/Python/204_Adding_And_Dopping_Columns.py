###############################################################################
# Pandas -  Adding & Dropping Columns
###############################################################################


import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")

transactions["store_id"] = 1

transactions["profit"] = transactions["sales_cost"] * 2

import numpy as np


transactions["sales_type"] = np.where(transactions["sales_cost"] > 20, "large", "small")


condition_rules = [transactions["sales_cost"] > 50, transactions["sales_cost"] > 20, transactions["sales_cost"] > 10]
outcomes = ["XL-Large", " Large", "Medium"]
transactions["sales_type"] = np.select(condition_rules, outcomes, default = "small")


new_df = transactions.drop(["sales_cost"], axis = 1)



