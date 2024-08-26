
#####################################################################
# Matplotlib - Highlighting Data
#####################################################################




import matplotlib.pyplot as plt
import pandas as pd

body_data = pd.read_csv("weights_and_heights.csv")


male   = body_data[body_data["Gender"] == "Male"]
female = body_data[body_data["Gender"] == "Female"]


male_sample = male.sample(200, random_state = 42)

patient = male_sample.loc[[705]]

plt.style.use("seaborn-poster")
plt.scatter(male_sample["Weight"], male_sample["Height"], color = "blue", s = 700, alpha= 0.5)
plt.scatter(patient["Weight"], patient["Height"], color = "red", s = 700, alpha= 1.0, edgecolor= "red", linewidths=2)
plt.scatter(patient["Weight"], patient["Height"], marker= "X", color = "pink", s = 250, alpha= 1.0,  linewidths=5) 
plt.title("Weight vs. Height for Males")
plt.xlabel("weight (lbs)")
plt.ylabel("Heightt (in)")
plt.axvline(x = male_sample["Weight"].median(), color = "black", linestyle = "--")
plt.axhline(y = male_sample["Height"].median(), color = "black", linestyle = "--")
plt.tight_layout()
plt.show()