###############################################################################
# Pandas -  LOC & ILOC
###############################################################################


import pandas as pd
transactions = pd.read_excel("grocery_database.xlsx", sheet_name= "transactions")

transactions.loc[row_labels, column_label]
transactions.iloc[row_indexes, column_indexes]


# ILOC

transactions.iloc[0]
transactions.iloc[0: 4]

transactions.iloc[[0,30,51]]
transactions.iloc[[0,30,79]]


transactions.iloc[0:4,[0,3,-1]]

# LOC


transactions.loc[0]
transactions.set_index("customer_id", inplace =True)
transactions.reset_index(inplace = True)
transactions.loc[642]


transactions.reset_index(inplace = True)
list(transactions)


transactions["customer_id"] = 642

transactions.loc[transactions["customer_id"] == 642, ["customer_id", "sales_cost"]]

transactions.loc[(transactions["customer_id"] == 642) & (transactions["num_items"] > 5)]

transactions.loc[(transactions["customer_id"] == 642) | (transactions["num_items"] > 5)]


transactions.loc[transactions["customer_id"].isin([642,700])]