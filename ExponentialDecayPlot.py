# Joshua Simpson
# CST 305 – Project 4: Plotting Exponential Functions e^(-5t) and -e^(-5t)
# This project visualizes the solution x(t) = e^(At) * C by plotting both
# positive and negative versions of e^(-5t) over a given time range.

# -------------------- Import Required Libraries ---------------------
import numpy as np                  # For numerical calculations and arrays
import matplotlib.pyplot as plt     # For plotting graphs
# --------------------------------------------------------------------


# ------------------------ Create Time Values -------------------------
# Generate 1000 evenly spaced values from -0.5 to 1.5
t = np.linspace(-0.5, 1.5, 1000)
# --------------------------------------------------------------------


# ---------------------- Calculate Function Values -------------------
# e^(-5t) decays quickly as t increases
ans1 = np.exp(-5 * t)

# -e^(-5t) is just the flipped version across the x-axis
ans2 = -ans1
# --------------------------------------------------------------------


# -------------------------- Plot the Graphs --------------------------
plt.figure(figsize=(10, 6))  # Set figure size

# Plot e^(-5t) in blue
plt.plot(t, ans1, label='e^(-5t)', color='blue')

# Plot -e^(-5t) in orange
plt.plot(t, ans2, label='-e^(-5t)', color='orange')

# Add labels and title
plt.xlabel('t')
plt.ylabel('Function Value')
plt.title('x(t) = e^(At) * C')

# Add legend to distinguish curves
plt.legend()

# Set vertical limits of the y-axis
plt.ylim(-3, 3)

# Show gridlines for better visibility
plt.grid()

# Show the final graph
plt.show()
# --------------------------------------------------------------------
