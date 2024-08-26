

#####################################################################################################
# K Means Clustering - Advanced Template
#####################################################################################################



# Import required Python packages

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt

###################################################################################################
# Create the data
###################################################################################################

# Import tables


transactions = pd.read_excel("data/grocery_database.xlsx", sheet_name= "transactions")
product_areas = pd.read_excel("data/grocery_database.xlsx", sheet_name= "product_areas")

# merge on product area name

transactions = pd.merge(transactions, product_areas, how= "inner", on="product_area_id")

# drop the non-food category

transactions.drop(transactions[transactions["product_area_name"] == "Non_Food"].index, inplace = True)

# aggregate sales at customer level (by product area)

transactions_summary = transactions.groupby(["customer_id", "product_area_name"])["sales_cost"].sum().reset_index()

# pivot data to place product areas as columns

transactions_summary_pivot = transactions.pivot_table(index = "customer_id",
                                                      columns = "product_area_name",
                                                      values = "sales_cost",
                                                      fill_value = 0,
                                                      margins = True,
                                                      margins_name = "Total"
                                                      ).rename_axis(None, axis = 1)


# Turn sales into % sales

transactions_summary_pivot = transactions_summary_pivot.div(transactions_summary_pivot["Total"], axis = 0)

# drop the "total" column

data_for_clustering = transactions_summary_pivot.drop(["Total"], axis = 1)


####################################################################################################
#  Data Preparation & Cleaning
####################################################################################################


# Check for missing values

data_for_clustering.isna().sum()


# Normalise data

scale_norm = MinMaxScaler()

data_for_clustering_scaled = pd.DataFrame(scale_norm.fit_transform(data_for_clustering), columns = data_for_clustering.columns)


###################################################################################################
# Use WCSS to find a good value for k 
###################################################################################################


k_values = list(range(1,10))
wcss_list = []

for k in k_values:
    Kmeans = KMeans(n_clusters = k, random_state = 42)
    Kmeans.fit(data_for_clustering_scaled)
    wcss_list.append(Kmeans.inertia_)
    
    
plt.plot(k_values, wcss_list)
plt.title("Within Cluster Sum of Squares -  by k")
plt.xlabel("K")
plt.ylabel("WCSS Score")
plt.tight_layout()
plt.show()
###################################################################################################
# Instantiate & fit model
###################################################################################################

Kmeans = KMeans(n_clusters = 3, random_state = 42)
Kmeans.fit(data_for_clustering_scaled)


###################################################################################################
# Use cluster information
###################################################################################################

# Add cluster labels to our data

data_for_clustering["cluster"] = Kmeans.labels_

# check cluster sizes


data_for_clustering["cluster"].value_counts()


###################################################################################################
# Profile our clusters
###################################################################################################

cluster_summary = data_for_clustering.groupby("cluster")[["Dairy", "Fruit", "Meat", "Vegetables"]].mean()
