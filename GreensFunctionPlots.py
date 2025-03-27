# Joshua Simpson
# CST 305 – Project 3: Green's Function and Homogeneous ODE Visualization
# This script compares homogeneous solutions (zero due to constants) and
# particular solutions using analytical expressions (Green's function style).

# ------------------- Import Required Libraries -------------------
import numpy as np                  # For numerical operations and time values
import matplotlib.pyplot as plt     # For plotting graphs
from scipy.integrate import odeint  # For solving ODEs numerically (not heavily used here)
# -----------------------------------------------------------------


# ---------------------- Time Setup -------------------------------
# Create an array of 100 time points from 0 to 10 seconds
t = np.linspace(0, 10, 100)
# -----------------------------------------------------------------


# ------------------ Homogeneous Constants ------------------------
# Constants for the homogeneous solution; set to 0 for simplicity
a = b = c = d = 0
# -----------------------------------------------------------------


# ----------- Homogeneous Solution Functions ----------------------
# These return solutions to the homogeneous ODEs.
# With a, b, c, d = 0, the result will be zero across all time.

def a1(x, t):
    return a * np.cos(2 * t) + b * np.sin(2 * t)

def a2(x, t):
    return c * np.cos(t) + d * np.sin(t)
# -----------------------------------------------------------------


# ----------- Particular Solution Functions -----------------------
# These functions represent exact (analytical) solutions to the same ODEs.
# These are derived using Green’s function techniques or direct integration.

def b1(t):
    return t / 4 - np.sin(2 * t) / 8

def b2(t):
    return 4 * (1 - np.cos(t))
# -----------------------------------------------------------------


# --------------- Solve Homogeneous with odeint -------------------
# Technically not necessary since the solution is 0, but done for completeness.

h1 = odeint(a1, 0, t)  # Homogeneous solution for ODE 1 (should be zeros)
h2 = odeint(a2, 0, t)  # Homogeneous solution for ODE 2 (should be zeros)
# -----------------------------------------------------------------


# ---------------- Evaluate Particular Solutions ------------------
g1 = b1(t)  # Particular solution for ODE 1
g2 = b2(t)  # Particular solution for ODE 2
# -----------------------------------------------------------------


# ------------------- Create Subplots -----------------------------
# Create a 2x2 grid of plots with size 12x6
fig, axs = plt.subplots(2, 2, figsize=(12, 6))
# -----------------------------------------------------------------


# -------------------- Plot Homogeneous Solutions -----------------
axs[0][0].plot(t, h1, label="c1*cos(2t) + c2*sin(2t)", color='blue')
axs[0][0].set_title("Homogeneous Solution for First ODE")
axs[0][0].set_xlabel("t")
axs[0][0].set_ylabel("y(t)")
axs[0][0].grid(True)
axs[0][0].legend()

axs[0][1].plot(t, h2, label="c1*cos(t) + c2*sin(t)", color='magenta')
axs[0][1].set_title("Homogeneous Solution for Second ODE")
axs[0][1].set_xlabel("t")
axs[0][1].set_ylabel("y(t)")
axs[0][1].grid(True)
axs[0][1].legend()
# -----------------------------------------------------------------


# ------------------ Plot Particular Solutions --------------------
axs[1][0].plot(t, g1, label="t/4 - sin(2t)/8", color='red')
axs[1][0].set_title("Particular Solution: t/4 - sin(2t)/8")
axs[1][0].set_xlabel("t")
axs[1][0].set_ylabel("y(t)")
axs[1][0].grid(True)
axs[1][0].legend()

axs[1][1].plot(t, g2, label="4(1 - cos(t))", color='green')
axs[1][1].set_title("Particular Solution: 4(1 - cos(t))")
axs[1][1].set_xlabel("t")
axs[1][1].set_ylabel("y(t)")
axs[1][1].grid(True)
axs[1][1].legend()
# -----------------------------------------------------------------


# -------------------- Display Final Layout -----------------------
plt.tight_layout()  # Makes sure plots don’t overlap
plt.show()          # Display the 4 graphs
# -----------------------------------------------------------------
