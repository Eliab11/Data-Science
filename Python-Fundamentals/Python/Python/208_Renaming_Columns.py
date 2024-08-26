###############################################################################
# Pandas -  Renaming & Columns
###############################################################################

import pandas as pd
transactions = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")

list(transactions)

transactions.rename(columns = {"customer_is" : "friend_id"}, inplace = True)
list(transactions)

columns_names = ['customer_id',
                 'transaction_date',
                 'transaction_id',
                 'product_area_id',
                 'num_items', 
                 'sales_cost']

