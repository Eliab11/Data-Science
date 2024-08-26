########################################################################################
# Linear Regression - Basic Template
########################################################################################


# Import required Python package


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd


# Import sample data

my_df = pd.read_csv("sample_data_regression.csv")

# Split data into input and output objects

X = my_df.drop(["output"], axis = 1)
y = my_df["output"]

# Splitb data into training  and tes sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 42)

# Instantiate our model objects

regression = LinearRegression()

# Train our model

regression.fit(X_train, y_train)
# Assess model accuracy

y_pred = regression.predict(X_test)
r2_score(y_test, y_pred)
