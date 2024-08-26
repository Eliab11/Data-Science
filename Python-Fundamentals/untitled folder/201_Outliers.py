import pandas as pd

my_df = pd.DataFrame({"input1" : [15,41,44,47, 50,53, 56, 59,99],
                      "input2" : [29,41,44,47,50,53,56,59,66]})


my_df.plot(kind = "box", vert = False)

outlieer_columns = ["input1", "input2"]

# Boxplot approach

for column in outlieer_columns:
    
    lower_quartile = my_df[column].quantile(0.25)
    upper_quartile = my_df[column].quantile(0.75)
    iqr = upper_quartile - lower_quartile
    iqr
    