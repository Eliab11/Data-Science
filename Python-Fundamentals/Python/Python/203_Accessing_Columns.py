###############################################################################
# Pandas -  Accessing Columns
###############################################################################

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")


new_df = transactions.customer_id

my_var = "customer_id"
transactions.my_var

new_df = transactions[["customer_id"]]
transactions[my_var]

