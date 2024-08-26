import pandas as pd
from sklearn.preprocessing import OneHotEncoder

X = pd.DataFrame({"input1" : [1,2,3,4,5],
                  "input2" : ["A","A","B","B","C"],
                  "input3" : ["X","X","X","X","X"]})

categorical_vars = ["input1", "input3"]

one_hot_encoder = OneHotEncoder(sparse=False)

encoder_vars_array = one_hot_encoder.fit_transform(X[categorical_vars])


