###############################################################################
# Pandas -  Sorting & Ranking
###############################################################################

import pandas as pd
customer_details = pd.read_excel("grocery_database.xlsx", sheet_name= "customer_details")

##product_areas = pd.read_excel("grocery_database.xlsx", sheet_name="product_areas")





customer_deatils = pd.read_excel("grocery_database.xlsx", sheet_name="customer_details")


# SORTING
customer_deatils.sort_values(by = "distance_from_store", inplace = True)
customer_deatils.sort_values(by = "distance_from_store", inplace = True, ascending = False )


customer_deatils.sort_values(by = ["distance_from_store", "credit_score"], inplace = True)

customer_deatils.sort_values(by = "distance_from_store", inplace = True, na_position = "first")

# RANKING

import numpy as np
X = pd.DataFrame({"column1" : [1,1,1,2,3,4,5,np.nan,6,8]})


X["column1"].rank()

X["column1_rank"] = X["column1"].rank()

X["average_rank"] = X["column1"].rank(method = "average")
X["min_rank"] = X["column1"].rank(method = "min")
X["max_rank"] = X["column1"].rank(method = "max")
X["first_rank"] = X["column1"].rank(method = "first")
X["dense_rank"] = X["column1"].rank(method = "dense")