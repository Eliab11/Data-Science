#####################################################################

# Matplotlib - Subplots

#####################################################################


import matplotlib.pyplot as plt

X_values = [0,1,2,3,4,5,6,7,8,9,10]
X_Squared = [x**2 for x in X_values]
X_cubed   = [x**3 for x in X_values]

plt.subplot(2,1,1)
plt.plot(X_values, X_Squared, label = "X Squared")
plt.title("Squared Values")
plt.xlabel("X")
plt.ylabel("X Squared")


plt.subplot(2,1,2)
plt.bar(X_values, X_Squared, label = "X Cubed")
plt.title("Cubed Values")
plt.xlabel("X")
plt.ylabel("X Cubed")
plt.tight_layout()
plt.show()



plt.subplot(2,2,1)
plt.plot(X_values, X_Squared, label = "X Squared")
plt.title("Squared Values")
plt.xlabel("X")
plt.ylabel("X Squared")


plt.subplot(2,2,2)
plt.bar(X_values, X_Squared, label = "X Cubed")
plt.title("Cubed Values")
plt.xlabel("X")
plt.ylabel("X Cubed")

plt.subplot(2,2,3)
plt.plot(X_values, X_Squared, label = "X Squared")
plt.title("Squared Values")
plt.xlabel("X")
plt.ylabel("X Squared")


plt.subplot(2,2,4)
plt.bar(X_values, X_Squared, label = "X Cubed")
plt.title("Cubed Values")
plt.xlabel("X")
plt.ylabel("X Cubed")


plt.tight_layout()
plt.show()











