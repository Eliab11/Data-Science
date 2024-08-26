import pandas as pd


# JOINING

df_a = pd.DataFrame({"A" : [1,2,3], "B" : [4,5,6]})
df_b = pd.DataFrame({"C" : [1,2,3], "B" : [4,5,6]})

df_c = pd.concat([df_a, df_b], axis = 1)

df_c = pd.concat([df_a, df_b], axis = 0)


df_a = pd.DataFrame({"A" : [1,2,3], "B" : [4,5,6]})
df_b = pd.DataFrame({"A" : [1,2,3], "B" : [4,5,6]})
df_c = pd.concat([df_a,df_a], axis = 0)

  
