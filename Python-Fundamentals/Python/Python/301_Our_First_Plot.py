-- Matplotlib - Our First Plot 

import matplotlib.pyplot ast

X_values = [0,1,2,3,4,5,6,7,8,9,10]

X_Squared = [x**2 for x in X_values]

plt.plot(X_values, X_Squared)
plt.title("Exponenttial Growth")
plt.xlabel("The values of x")
plt.ylabel("The values of y")
plt.show()
