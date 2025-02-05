###################################################################################################
#   PCA - Code Template
##################################################################################################


#####################################################################################################################


import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np


from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import shuffle
from sklearn.model_selection import  train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

######################################################################################################################
# Import sample data
######################################################################################################################


# Imoport

data_for_model = pd.read_csv("data/sample_data_pca.csv")


# Drop uneccessary columns

data_for_model.drop("user_id", axis = 1, inplace = True)


# Shuffle data
data_for_model = shuffle(data_for_model, random_state= 42)


# class Balance

data_for_model["purchased_album"].value_counts(normalize = True)


######################################################################################################################
# Deal  with Missing Values
######################################################################################################################

data_for_model.isna().sum()
data_for_model.dropna(how = "any", inplace = True)
    

######################################################################################################################
# Split Input Variables & Output variables
######################################################################################################################

X = data_for_model.drop(["purchased_album"], axis = 1)
y = data_for_model["purchased_album"]

    
######################################################################################################################
# Split out training & Test sets
######################################################################################################################

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state= 42, stratify = y)


######################################################################################################################
# Feature Scaling
######################################################################################################################

scale_standard = StandardScaler()

X_train = scale_standard.fit_transform(X_train)
X_test  = scale_standard.transform(X_test)



############################################################################################
# Apply PCA
############################################################################################


# Instantiate & fit

pca = PCA(n_components= None, random_state= 42)
pca.fit(X_train)

# Extract the explained variance across components
explained_variance = pca.explained_variance_ratio_
explained_variance_cumulative = pca.explained_variance_ratio_.cumsum()


##############################################################################################
# Plot list for number of components
##############################################################################################

# create list for number of components

num_vars_list = list(range(1,101))
plt.figure(figsize= (15,10))

# plot the variance explained by each component
plt.subplot(2,1,1)
plt.bar(num_vars_list, explained_variance)
plt.title("Variance across Principle Components")
plt.xlabel("Number of Coimponents")
plt.ylabel("% Variance")
plt.tight_layout()


# plot the cumulative variance

plt.subplot(2,1,2)
plt.bar(num_vars_list, explained_variance_cumulative)
plt.title("Variance across Principle Components")
plt.xlabel("Number of Coimponents")
plt.ylabel("Cumulate % Variance")
plt.tight_layout()
plt.show()



#####################################################################################################
# Apply PCA with selected number of components
#####################################################################################################

pca = PCA(n_components= 0.75, random_state= 42)


X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

pca.n_components


#####################################################################################################
# Apply PCA with selected number of components
#####################################################################################################

clf = RandomForestClassifier(random_state= 42)
clf.fit(X_train, y_train)



#####################################################################################################
# Sssess Model Accuracy
#####################################################################################################

y_pred_class = clf.predict(X_test)
accuracy_score(y_test,y_pred_class)