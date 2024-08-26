###############################################################################
# Pandas -  Exporting Our Data
###############################################################################

import pandas as pd
import numpy as np

my_df = pd.DataFrame({"A" : [1,2,3],
                     "B" : ["one", np.nan, "three"]})

my_df.to_csv("tester_export.csv", index= False)

my_df.to_csv("tester_export.csv", index= False)
my_df.to_csv("tester_export.csv", index= False)

