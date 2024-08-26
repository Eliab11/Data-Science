###############################################################################
# Pandas - Creating DataFrame
###############################################################################


import pandas as pd

my_df = pd.DataFrame()

my_df = pd.DataFrame({"Name" : ["Tom", "Dick", "Harry"]})

my_df = pd.DataFrame({"Name" : ["Tom", "Dick", "Harry"],
                      "ID"  : [101, 102, 1203]})



my_list = [["Tom", 101], ["Dick", 102],["Harry", 103]]

my_df = pd.DataFrame(my_list, columns = ["Name", "ID"])


my_data = pd.read_csv("tester_csv.csv")

transactions = pd.read_excel("grocery_database.xlsx", sheet_name="transactions")
